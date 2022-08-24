import io
import os
from pathlib import Path

import pytest

import PyPDF2._utils
from PyPDF2._utils import (
    _get_max_pdf_version_header,
    deprecate_bookmark,
    mark_location,
    matrix_multiply,
    read_block_backwards,
    read_previous_line,
    read_until_regex,
    read_until_whitespace,
    skip_over_comment,
    skip_over_whitespace,
)
from PyPDF2.errors import PdfReadError, PdfStreamError

TESTS_ROOT = Path(__file__).parent.resolve()
PROJECT_ROOT = TESTS_ROOT.parent
RESOURCE_ROOT = PROJECT_ROOT / "resources"


@pytest.mark.parametrize(
    ("stream", "expected"),
    [
        (io.BytesIO(b"foo"), False),
        (io.BytesIO(b""), False),
        (io.BytesIO(b" "), True),
        (io.BytesIO(b"  "), True),
        (io.BytesIO(b"  \n"), True),
        (io.BytesIO(b"    \n"), True),
    ],
)
def test_skip_over_whitespace(stream, expected):
    assert skip_over_whitespace(stream) == expected


def test_read_until_whitespace():
    assert read_until_whitespace(io.BytesIO(b"foo"), maxchars=1) == b"f"


@pytest.mark.parametrize(
    ("stream", "remainder"),
    [
        (io.BytesIO(b"% foobar\n"), b""),
        (io.BytesIO(b""), b""),
        (io.BytesIO(b" "), b" "),
        (io.BytesIO(b"% foo%\nbar"), b"bar"),
    ],
)
def test_skip_over_comment(stream, remainder):
    skip_over_comment(stream)
    assert stream.read() == remainder


def test_read_until_regex_premature_ending_raise():
    import re

    stream = io.BytesIO(b"")
    with pytest.raises(PdfStreamError) as exc:
        read_until_regex(stream, re.compile(b"."))
    assert exc.value.args[0] == "Stream has ended unexpectedly"


def test_read_until_regex_premature_ending_name():
    import re

    stream = io.BytesIO(b"")
    assert read_until_regex(stream, re.compile(b"."), ignore_eof=True) == b""


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (((3,),), ((7,),), ((21,),)),
        (((3, 7),), ((5,), (13,)), ((3 * 5.0 + 7 * 13,),)),
        (((3,), (7,)), ((5, 13),), ((3 * 5, 3 * 13), (7 * 5, 7 * 13))),
    ],
)
def test_matrix_multiply(a, b, expected):
    assert matrix_multiply(a, b) == expected


def test_mark_location():
    stream = io.BytesIO(b"abde" * 6000)
    mark_location(stream)
    os.remove("PyPDF2_pdfLocation.txt")  # cleanup


def test_hex_str():
    assert PyPDF2._utils.hex_str(10) == "0xa"


def test_b():
    assert PyPDF2._utils.b_("foo") == b"foo"
    assert PyPDF2._utils.b_("😀") == "😀".encode()
    assert PyPDF2._utils.b_("‰") == "‰".encode()
    assert PyPDF2._utils.b_("▷") == "▷".encode()
    assert PyPDF2._utils.b_("世") == "世".encode()


def test_deprecate_no_replacement():
    with pytest.raises(PendingDeprecationWarning) as exc:
        PyPDF2._utils.deprecate_no_replacement("foo")
    error_msg = "foo is deprecated and will be removed in PyPDF2 3.0.0."
    assert exc.value.args[0] == error_msg


@pytest.mark.parametrize(
    ("left", "up", "upleft", "expected"),
    [
        (0, 0, 0, 0),
        (1, 0, 0, 1),
        (0, 1, 0, 1),
        (0, 0, 1, 0),
        (1, 2, 3, 1),
        (2, 1, 3, 1),
        (1, 3, 2, 2),
        (3, 1, 2, 2),
        (3, 2, 1, 3),
    ],
)
def test_paeth_predictor(left, up, upleft, expected):
    assert PyPDF2._utils.paeth_predictor(left, up, upleft) == expected


@pytest.mark.parametrize(
    ("dat", "pos", "to_read"),
    [
        (b"", 0, 1),
        (b"a", 0, 1),
        (b"abc", 0, 10),
    ],
)
def test_read_block_backwards_errs(dat, pos, to_read):
    with pytest.raises(PdfStreamError) as _:
        s = io.BytesIO(dat)
        s.seek(pos)
        read_block_backwards(s, to_read)


@pytest.mark.parametrize(
    ("dat", "pos", "to_read", "expected", "expected_pos"),
    [
        (b"abc", 1, 0, b"", 1),
        (b"abc", 1, 1, b"a", 0),
        (b"abc", 2, 1, b"b", 1),
        (b"abc", 2, 2, b"ab", 0),
        (b"abc", 3, 1, b"c", 2),
        (b"abc", 3, 2, b"bc", 1),
        (b"abc", 3, 3, b"abc", 0),
    ],
)
def test_read_block_backwards(dat, pos, to_read, expected, expected_pos):
    s = io.BytesIO(dat)
    s.seek(pos)
    assert read_block_backwards(s, to_read) == expected
    assert s.tell() == expected_pos


def test_read_block_backwards_at_start():
    s = io.BytesIO(b"abc")
    with pytest.raises(PdfStreamError) as _:
        read_previous_line(s)


@pytest.mark.parametrize(
    ("dat", "pos", "expected", "expected_pos"),
    [
        (b"abc", 1, b"a", 0),
        (b"abc", 2, b"ab", 0),
        (b"abc", 3, b"abc", 0),
        (b"abc\n", 3, b"abc", 0),
        (b"abc\n", 4, b"", 3),
        (b"abc\n\r", 4, b"", 3),
        (b"abc\nd", 5, b"d", 3),
        # Skip over multiple CR/LF bytes
        (b"abc\n\r\ndef", 9, b"def", 3),
    ],
    ids=list(range(8)),
)
def test_read_previous_line(dat, pos, expected, expected_pos):
    s = io.BytesIO(dat)
    s.seek(pos)
    assert read_previous_line(s) == expected
    assert s.tell() == expected_pos


# for unknown reason if the parameters are passed through pytest, errors are reported
def test_read_previous_line2():
    # Include a block full of newlines...
    test_read_previous_line(
        b"abc" + b"\n" * (2 * io.DEFAULT_BUFFER_SIZE) + b"d",
        2 * io.DEFAULT_BUFFER_SIZE + 4,
        b"d",
        3,
    )
    # Include a block full of non-newline characters
    test_read_previous_line(
        b"abc\n" + b"d" * (2 * io.DEFAULT_BUFFER_SIZE),
        2 * io.DEFAULT_BUFFER_SIZE + 4,
        b"d" * (2 * io.DEFAULT_BUFFER_SIZE),
        3,
    )
    # Both
    test_read_previous_line(
        b"abcxyz"
        + b"\n" * (2 * io.DEFAULT_BUFFER_SIZE)
        + b"d" * (2 * io.DEFAULT_BUFFER_SIZE),
        4 * io.DEFAULT_BUFFER_SIZE + 6,
        b"d" * (2 * io.DEFAULT_BUFFER_SIZE),
        6,
    )


def test_get_max_pdf_version_header():
    with pytest.raises(ValueError) as exc:
        _get_max_pdf_version_header(b"", b"PDF-1.2")
    assert exc.value.args[0] == "neither b'' nor b'PDF-1.2' are proper headers"


def test_read_block_backwards_exception():
    stream = io.BytesIO(b"foobar")
    stream.seek(6)
    with pytest.raises(PdfReadError) as exc:
        read_block_backwards(stream, 7)
    assert exc.value.args[0] == "Could not read malformed PDF file"


def test_deprecate_bookmark():
    @deprecate_bookmark(old_param="new_param")
    def foo(old_param=1, baz=2):
        return old_param * baz

    with pytest.raises(TypeError) as exc:
        foo(old_param=12, new_param=13)
    expected_msg = (
        "foo received both old_param and new_param as an argument. "
        "old_param is deprecated. Use new_param instead."
    )
    assert exc.value.args[0] == expected_msg
