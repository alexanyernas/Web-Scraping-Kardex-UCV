import os
from io import BytesIO
from pathlib import Path
from unittest.mock import patch

import pytest

from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from PyPDF2.constants import CheckboxRadioButtonAttributes
from PyPDF2.constants import TypFitArguments as TF
from PyPDF2.errors import PdfReadError, PdfStreamError
from PyPDF2.generic import (
    AnnotationBuilder,
    ArrayObject,
    BooleanObject,
    ByteStringObject,
    Destination,
    DictionaryObject,
    FloatObject,
    IndirectObject,
    NameObject,
    NullObject,
    NumberObject,
    OutlineItem,
    RectangleObject,
    TextStringObject,
    TreeObject,
    create_string_object,
    encode_pdfdocencoding,
    read_hex_string_from_stream,
    read_object,
    read_string_from_stream,
)

from . import ReaderDummy, get_pdf_from_url

TESTS_ROOT = Path(__file__).parent.resolve()
PROJECT_ROOT = TESTS_ROOT.parent
RESOURCE_ROOT = PROJECT_ROOT / "resources"


def test_float_object_exception():
    assert FloatObject("abc") == 0


def test_number_object_exception():
    with pytest.raises(OverflowError):
        NumberObject(1.5 * 2**10000)


def test_create_string_object_exception():
    with pytest.raises(TypeError) as exc:
        create_string_object(123)
    assert (  # typeguard is not running
        exc.value.args[0] == "create_string_object should have str or unicode arg"
    ) or (  # typeguard is enabled
        'type of argument "string" must be one of (str, bytes); got int instead'
        in exc.value.args[0]
    )


@pytest.mark.parametrize(
    ("value", "expected", "tell"), [(b"true", b"true", 4), (b"false", b"false", 5)]
)
def test_boolean_object(value, expected, tell):
    stream = BytesIO(value)
    assert BooleanObject.read_from_stream(stream).value == (expected == b"true")
    stream.seek(0, 0)
    assert stream.read() == expected
    assert stream.tell() == tell


def test_boolean_object_write():
    stream = BytesIO()
    boolobj = BooleanObject(None)
    boolobj.write_to_stream(stream, encryption_key=None)
    stream.seek(0, 0)
    assert stream.read() == b"false"


def test_boolean_eq():
    boolobj = BooleanObject(True)
    assert (boolobj == True) is True  # noqa: E712
    assert (boolobj == False) is False  # noqa: E712
    assert (boolobj == "True") is False

    boolobj = BooleanObject(False)
    assert (boolobj == True) is False  # noqa: E712
    assert (boolobj == False) is True  # noqa: E712
    assert (boolobj == "True") is False


def test_boolean_object_exception():
    stream = BytesIO(b"False")
    with pytest.raises(PdfReadError) as exc:
        BooleanObject.read_from_stream(stream)
    assert exc.value.args[0] == "Could not read Boolean object"


def test_array_object_exception():
    stream = BytesIO(b"False")
    with pytest.raises(PdfReadError) as exc:
        ArrayObject.read_from_stream(stream, None)
    assert exc.value.args[0] == "Could not read array"


def test_null_object_exception():
    stream = BytesIO(b"notnull")
    with pytest.raises(PdfReadError) as exc:
        NullObject.read_from_stream(stream)
    assert exc.value.args[0] == "Could not read Null object"


@pytest.mark.parametrize("value", [b"", b"False", b"foo ", b"foo  ", b"foo bar"])
def test_indirect_object_premature(value):
    stream = BytesIO(value)
    with pytest.raises(PdfStreamError) as exc:
        IndirectObject.read_from_stream(stream, None)
    assert exc.value.args[0] == "Stream has ended unexpectedly"


def test_readHexStringFromStream():
    stream = BytesIO(b"a1>")
    assert read_hex_string_from_stream(stream) == "\x10"


def test_readHexStringFromStream_exception():
    stream = BytesIO(b"")
    with pytest.raises(PdfStreamError) as exc:
        read_hex_string_from_stream(stream)
    assert exc.value.args[0] == "Stream has ended unexpectedly"


def test_readStringFromStream_exception():
    stream = BytesIO(b"x")
    with pytest.raises(PdfStreamError) as exc:
        read_string_from_stream(stream)
    assert exc.value.args[0] == "Stream has ended unexpectedly"


def test_readStringFromStream_not_in_escapedict_no_digit():
    stream = BytesIO(b"x\\y")
    with pytest.raises(PdfReadError) as exc:
        read_string_from_stream(stream)
    assert exc.value.args[0] == "Stream has ended unexpectedly"


def test_readStringFromStream_multichar_eol():
    stream = BytesIO(b"x\\\n )")
    assert read_string_from_stream(stream) == " "


def test_readStringFromStream_multichar_eol2():
    stream = BytesIO(b"x\\\n\n)")
    assert read_string_from_stream(stream) == ""


def test_readStringFromStream_excape_digit():
    stream = BytesIO(b"x\\1a )")
    assert read_string_from_stream(stream) == "\x01a "


def test_readStringFromStream_excape_digit2():
    stream = BytesIO(b"(hello \\1\\2\\3\\4)")
    assert read_string_from_stream(stream) == "hello \x01\x02\x03\x04"


def test_NameObject():
    stream = BytesIO(b"x")
    with pytest.raises(PdfReadError) as exc:
        NameObject.read_from_stream(stream, None)
    assert exc.value.args[0] == "name read error"


def test_destination_fit_r():
    d = Destination(
        NameObject("title"),
        NullObject(),
        NameObject(TF.FIT_R),
        FloatObject(0),
        FloatObject(0),
        FloatObject(0),
        FloatObject(0),
    )
    assert d.title == NameObject("title")
    assert d.typ == "/FitR"
    assert d.zoom is None
    assert d.left == FloatObject(0)
    assert d.right == FloatObject(0)
    assert d.top == FloatObject(0)
    assert d.bottom == FloatObject(0)
    assert list(d) == []
    d.empty_tree()


def test_destination_fit_v():
    Destination(NameObject("title"), NullObject(), NameObject(TF.FIT_V), FloatObject(0))

    # Trigger Exception
    Destination(NameObject("title"), NullObject(), NameObject(TF.FIT_V), None)


def test_destination_exception():
    with pytest.raises(PdfReadError) as exc:
        Destination(
            NameObject("title"), NullObject(), NameObject("foo"), FloatObject(0)
        )
    assert exc.value.args[0] == "Unknown Destination Type: 'foo'"


def test_outline_item_write_to_stream():
    stream = BytesIO()
    oi = OutlineItem(
        NameObject("title"), NullObject(), NameObject(TF.FIT_V), FloatObject(0)
    )
    oi.write_to_stream(stream, None)
    stream.seek(0, 0)
    assert stream.read() == b"<<\n/Title title\n/Dest [ null /FitV 0 ]\n>>"


def test_encode_pdfdocencoding_keyerror():
    with pytest.raises(UnicodeEncodeError) as exc:
        encode_pdfdocencoding("😀")
    assert exc.value.args[0] == "pdfdocencoding"


def test_read_object_comment_exception():
    stream = BytesIO(b"% foobar")
    pdf = None
    with pytest.raises(PdfStreamError) as exc:
        read_object(stream, pdf)
    assert exc.value.args[0] == "File ended unexpectedly."


def test_read_object_comment():
    stream = BytesIO(b"% foobar\n1 ")
    pdf = None
    out = read_object(stream, pdf)
    assert out == 1


def test_ByteStringObject():
    bo = ByteStringObject("stream", encoding="utf-8")
    stream = BytesIO(b"")
    bo.write_to_stream(stream, encryption_key="foobar")
    stream.seek(0, 0)
    assert stream.read() == b"<1cdd628b972e>"  # TODO: how can we verify this?


def test_DictionaryObject_key_is_no_pdfobject():
    do = DictionaryObject({NameObject("/S"): NameObject("/GoTo")})
    with pytest.raises(ValueError) as exc:
        do["foo"] = NameObject("/GoTo")
    assert exc.value.args[0] == "key must be PdfObject"


def test_DictionaryObject_xmp_meta():
    do = DictionaryObject({NameObject("/S"): NameObject("/GoTo")})
    assert do.xmp_metadata is None


def test_DictionaryObject_value_is_no_pdfobject():
    do = DictionaryObject({NameObject("/S"): NameObject("/GoTo")})
    with pytest.raises(ValueError) as exc:
        do[NameObject("/S")] = "/GoTo"
    assert exc.value.args[0] == "value must be PdfObject"


def test_DictionaryObject_setdefault_key_is_no_pdfobject():
    do = DictionaryObject({NameObject("/S"): NameObject("/GoTo")})
    with pytest.raises(ValueError) as exc:
        do.setdefault("foo", NameObject("/GoTo"))
    assert exc.value.args[0] == "key must be PdfObject"


def test_DictionaryObject_setdefault_value_is_no_pdfobject():
    do = DictionaryObject({NameObject("/S"): NameObject("/GoTo")})
    with pytest.raises(ValueError) as exc:
        do.setdefault(NameObject("/S"), "/GoTo")
    assert exc.value.args[0] == "value must be PdfObject"


def test_DictionaryObject_setdefault_value():
    do = DictionaryObject({NameObject("/S"): NameObject("/GoTo")})
    do.setdefault(NameObject("/S"), NameObject("/GoTo"))


def test_DictionaryObject_read_from_stream():
    stream = BytesIO(b"<< /S /GoTo >>")
    pdf = None
    out = DictionaryObject.read_from_stream(stream, pdf)
    assert out.get_object() == {NameObject("/S"): NameObject("/GoTo")}


def test_DictionaryObject_read_from_stream_broken():
    stream = BytesIO(b"< /S /GoTo >>")
    pdf = None
    with pytest.raises(PdfReadError) as exc:
        DictionaryObject.read_from_stream(stream, pdf)
    assert (
        exc.value.args[0]
        == "Dictionary read error at byte 0x2: stream must begin with '<<'"
    )


def test_DictionaryObject_read_from_stream_unexpected_end():
    stream = BytesIO(b"<< \x00/S /GoTo")
    pdf = None
    with pytest.raises(PdfStreamError) as exc:
        DictionaryObject.read_from_stream(stream, pdf)
    assert exc.value.args[0] == "Stream has ended unexpectedly"


def test_DictionaryObject_read_from_stream_stream_no_newline():
    stream = BytesIO(b"<< /S /GoTo >>stream")
    pdf = None
    with pytest.raises(PdfReadError) as exc:
        DictionaryObject.read_from_stream(stream, pdf)
    assert exc.value.args[0] == "Stream data must be followed by a newline"


@pytest.mark.parametrize(("strict"), [(True), (False)])
def test_DictionaryObject_read_from_stream_stream_no_stream_length(strict):
    stream = BytesIO(b"<< /S /GoTo >>stream\n")

    class Tst:  # to replace pdf
        strict = False

    pdf = Tst()
    pdf.strict = strict
    with pytest.raises(PdfReadError) as exc:
        DictionaryObject.read_from_stream(stream, pdf)
    assert exc.value.args[0] == "Stream length not defined"


@pytest.mark.parametrize(
    ("strict", "length", "should_fail"),
    [
        (True, 6, False),
        (True, 10, False),
        (True, 4, True),
        (False, 6, False),
        (False, 10, False),
    ],
)
def test_DictionaryObject_read_from_stream_stream_stream_valid(
    strict, length, should_fail
):
    stream = BytesIO(b"<< /S /GoTo /Length %d >>stream\nBT /F1\nendstream\n" % length)

    class Tst:  # to replace pdf
        strict = True

    pdf = Tst()
    pdf.strict = strict
    with pytest.raises(PdfReadError) as exc:
        do = DictionaryObject.read_from_stream(stream, pdf)
        # TODO: What should happen with the stream?
        assert do == {"/S": "/GoTo"}
        if length in (6, 10):
            assert b"BT /F1" in do._StreamObject__data
        raise PdfReadError("__ALLGOOD__")
    assert should_fail ^ (exc.value.args[0] == "__ALLGOOD__")


def test_RectangleObject():
    ro = RectangleObject((1, 2, 3, 4))
    assert ro.lower_left == (1, 2)
    assert ro.lower_right == (3, 2)
    assert ro.upper_left == (1, 4)
    assert ro.upper_right == (3, 4)

    ro.lower_left = (5, 6)
    assert ro.lower_left == (5, 6)

    ro.lower_right = (7, 8)
    assert ro.lower_right == (7, 8)

    ro.upper_left = (9, 11)
    assert ro.upper_left == (9, 11)

    ro.upper_right = (13, 17)
    assert ro.upper_right == (13, 17)


def test_TextStringObject_exc():
    tso = TextStringObject("foo")
    with pytest.raises(Exception) as exc:
        tso.get_original_bytes()
    assert exc.value.args[0] == "no information about original bytes"


def test_TextStringObject_autodetect_utf16():
    tso = TextStringObject("foo")
    tso.autodetect_utf16 = True
    assert tso.get_original_bytes() == b"\xfe\xff\x00f\x00o\x00o"


def test_remove_child_not_in_tree():
    tree = TreeObject()
    with pytest.raises(ValueError) as exc:
        tree.remove_child(NameObject("foo"))
    assert exc.value.args[0] == "Removed child does not appear to be a tree item"


def test_remove_child_not_in_that_tree():
    class ChildDummy:
        def __init__(self, parent):
            self.parent = parent

        def get_object(self):
            tree = DictionaryObject()
            tree[NameObject("/Parent")] = self.parent
            return tree

    tree = TreeObject()
    child = ChildDummy(TreeObject())
    tree.add_child(child, ReaderDummy())
    with pytest.raises(ValueError) as exc:
        tree.remove_child(child)
    assert exc.value.args[0] == "Removed child is not a member of this tree"


def test_remove_child_not_found_in_tree():
    class ChildDummy:
        def __init__(self, parent):
            self.parent = parent

        def get_object(self):
            tree = DictionaryObject()
            tree[NameObject("/Parent")] = self.parent
            return tree

    tree = TreeObject()
    child = ChildDummy(tree)
    tree.add_child(child, ReaderDummy())
    with pytest.raises(ValueError) as exc:
        tree.remove_child(child)
    assert exc.value.args[0] == "Removal couldn't find item in tree"


def test_remove_child_found_in_tree():
    writer = PdfWriter()

    # Add Tree
    tree = TreeObject()
    writer._add_object(tree)

    # Add first child
    # It's important to set a value, otherwise the writer.get_reference will
    # return the same object when a second child is added.
    child1 = TreeObject()
    child1[NameObject("/Foo")] = TextStringObject("bar")
    child1_ref = writer._add_object(child1)
    tree.add_child(child1_ref, writer)
    assert tree[NameObject("/Count")] == 1
    assert len([el for el in tree.children()]) == 1

    # Add second child
    child2 = TreeObject()
    child2[NameObject("/Foo")] = TextStringObject("baz")
    child2_ref = writer._add_object(child2)
    tree.add_child(child2_ref, writer)
    assert tree[NameObject("/Count")] == 2
    assert len([el for el in tree.children()]) == 2

    # Remove last child
    tree.remove_child(child2)
    assert tree[NameObject("/Count")] == 1
    assert len([el for el in tree.children()]) == 1

    # Add new child
    child3 = TreeObject()
    child3[NameObject("/Foo")] = TextStringObject("3")
    child3_ref = writer._add_object(child3)
    tree.add_child(child3_ref, writer)
    assert tree[NameObject("/Count")] == 2
    assert len([el for el in tree.children()]) == 2

    # Remove first child
    child1 = tree[NameObject("/First")]
    tree.remove_child(child1)
    assert tree[NameObject("/Count")] == 1
    assert len([el for el in tree.children()]) == 1

    child4 = TreeObject()
    child4[NameObject("/Foo")] = TextStringObject("4")
    child4_ref = writer._add_object(child4)
    tree.add_child(child4_ref, writer)
    assert tree[NameObject("/Count")] == 2
    assert len([el for el in tree.children()]) == 2

    child5 = TreeObject()
    child5[NameObject("/Foo")] = TextStringObject("5")
    child5_ref = writer._add_object(child5)
    tree.add_child(child5_ref, writer)
    assert tree[NameObject("/Count")] == 3
    assert len([el for el in tree.children()]) == 3

    # Remove middle child
    tree.remove_child(child4)
    assert tree[NameObject("/Count")] == 2
    assert len([el for el in tree.children()]) == 2

    tree.empty_tree()


def test_remove_child_in_tree():
    pdf = RESOURCE_ROOT / "form.pdf"

    tree = TreeObject()
    reader = PdfReader(pdf)
    writer = PdfWriter()
    writer.add_page(reader.pages[0])
    writer.add_outline_item("foo", pagenum=0)
    obj = writer._objects[-1]
    tree.add_child(obj, writer)
    tree.remove_child(obj)
    tree.add_child(obj, writer)
    tree.empty_tree()


def test_dict_read_from_stream(caplog):
    url = "https://corpora.tika.apache.org/base/docs/govdocs1/984/984877.pdf"
    name = "tika-984877.pdf"

    reader = PdfReader(BytesIO(get_pdf_from_url(url, name=name)))
    for page in reader.pages:
        page.extract_text()
    assert (
        "Multiple definitions in dictionary at byte 0x1084 for key /Length"
        in caplog.text
    )


def test_parse_content_stream_peek_percentage():
    url = "https://corpora.tika.apache.org/base/docs/govdocs1/985/985770.pdf"
    name = "tika-985770.pdf"

    reader = PdfReader(BytesIO(get_pdf_from_url(url, name=name)))
    for page in reader.pages:
        page.extract_text()


def test_read_inline_image_no_has_q():
    # pdf/df7e1add3156af17a372bc165e47a244.pdf
    url = "https://corpora.tika.apache.org/base/docs/govdocs1/998/998719.pdf"
    name = "tika-998719.pdf"

    reader = PdfReader(BytesIO(get_pdf_from_url(url, name=name)))
    for page in reader.pages:
        page.extract_text()


def test_read_inline_image_loc_neg_1():
    url = "https://corpora.tika.apache.org/base/docs/govdocs1/935/935066.pdf"
    name = "tika-935066.pdf"

    reader = PdfReader(BytesIO(get_pdf_from_url(url, name=name)))
    for page in reader.pages:
        page.extract_text()


def test_text_string_write_to_stream():
    url = "https://corpora.tika.apache.org/base/docs/govdocs1/924/924562.pdf"
    name = "tika-924562.pdf"

    reader = PdfReader(BytesIO(get_pdf_from_url(url, name=name)))
    for page in reader.pages:
        page.compress_content_streams()


def test_name_object_read_from_stream_unicode_error():  # L588
    url = "https://corpora.tika.apache.org/base/docs/govdocs1/974/974966.pdf"
    name = "tika-974966.pdf"

    reader = PdfReader(BytesIO(get_pdf_from_url(url, name=name)))
    for page in reader.pages:
        page.extract_text()


def test_bool_repr():
    url = "https://corpora.tika.apache.org/base/docs/govdocs1/932/932449.pdf"
    name = "tika-932449.pdf"

    reader = PdfReader(BytesIO(get_pdf_from_url(url, name=name)))
    with open("tmp-fields-report.txt", "w") as fp:
        fields = reader.get_fields(fileobj=fp)
    assert fields

    # cleanup
    os.remove("tmp-fields-report.txt")


@patch("PyPDF2._reader.logger_warning")
def test_issue_997(mock_logger_warning):
    url = "https://github.com/py-pdf/PyPDF2/files/8908874/Exhibit_A-2_930_Enterprise_Zone_Tax_Credits_final.pdf"
    name = "gh-issue-997.pdf"

    merger = PdfMerger()
    merged_filename = "tmp-out.pdf"
    merger.append(BytesIO(get_pdf_from_url(url, name=name)))  # here the error raises
    with open(merged_filename, "wb") as f:
        merger.write(f)
    merger.close()

    mock_logger_warning.assert_called_with(
        "Overwriting cache for 0 4", "PyPDF2._reader"
    )

    # Strict
    merger = PdfMerger(strict=True)
    merged_filename = "tmp-out.pdf"
    with pytest.raises(PdfReadError) as exc:
        merger.append(
            BytesIO(get_pdf_from_url(url, name=name))
        )  # here the error raises
    assert exc.value.args[0] == "Could not find object."
    with open(merged_filename, "wb") as f:
        merger.write(f)
    merger.close()

    # cleanup
    os.remove(merged_filename)


def test_annotation_builder_free_text():
    # Arrange
    pdf_path = RESOURCE_ROOT / "crazyones.pdf"
    reader = PdfReader(pdf_path)
    page = reader.pages[0]
    writer = PdfWriter()
    writer.add_page(page)

    # Act
    free_text_annotation = AnnotationBuilder.free_text(
        "Hello World - bold and italic\nThis is the second line!",
        rect=(50, 550, 200, 650),
        font="Arial",
        bold=True,
        italic=True,
        font_size="20pt",
        font_color="00ff00",
        border_color="0000ff",
        background_color="cdcdcd",
    )
    writer.add_annotation(0, free_text_annotation)

    free_text_annotation = AnnotationBuilder.free_text(
        "Another free text annotation (not bold, not italic)",
        rect=(500, 550, 200, 650),
        font="Arial",
        bold=False,
        italic=False,
        font_size="20pt",
        font_color="00ff00",
        border_color="0000ff",
        background_color="cdcdcd",
    )
    writer.add_annotation(0, free_text_annotation)

    # Assert: You need to inspect the file manually
    target = "annotated-pdf.pdf"
    with open(target, "wb") as fp:
        writer.write(fp)

    os.remove(target)  # comment this out for manual inspection


def test_annotation_builder_line():
    # Arrange
    pdf_path = RESOURCE_ROOT / "crazyones.pdf"
    reader = PdfReader(pdf_path)
    page = reader.pages[0]
    writer = PdfWriter()
    writer.add_page(page)

    # Act
    line_annotation = AnnotationBuilder.line(
        text="Hello World\nLine2",
        rect=(50, 550, 200, 650),
        p1=(50, 550),
        p2=(200, 650),
    )
    writer.add_annotation(0, line_annotation)

    # Assert: You need to inspect the file manually
    target = "annotated-pdf.pd"
    with open(target, "wb") as fp:
        writer.write(fp)

    os.remove(target)  # comment this out for manual inspection


def test_annotation_builder_link():
    # Arrange
    pdf_path = RESOURCE_ROOT / "outline-without-title.pdf"
    reader = PdfReader(pdf_path)
    page = reader.pages[0]
    writer = PdfWriter()
    writer.add_page(page)

    # Act
    # Part 1: Too many args
    with pytest.raises(ValueError) as exc:
        AnnotationBuilder.link(
            rect=(50, 550, 200, 650),
            url="https://martin-thoma.com/",
            target_page_index=3,
        )
    assert (
        exc.value.args[0]
        == "Either 'url' or 'target_page_index' have to be provided. url=https://martin-thoma.com/, target_page_index=3"
    )

    # Part 2: Too few args
    with pytest.raises(ValueError) as exc:
        AnnotationBuilder.link(
            rect=(50, 550, 200, 650),
        )
    assert (
        exc.value.args[0]
        == "Either 'url' or 'target_page_index' have to be provided. Both were None."
    )

    # Part 3: External Link
    link_annotation = AnnotationBuilder.link(
        rect=(50, 50, 100, 100),
        url="https://martin-thoma.com/",
        border=[1, 0, 6, [3, 2]],
    )
    writer.add_annotation(0, link_annotation)

    # Part 4: Internal Link
    link_annotation = AnnotationBuilder.link(
        rect=(100, 100, 300, 200),
        target_page_index=1,
        border=[50, 10, 4],
    )
    writer.add_annotation(0, link_annotation)

    for page in reader.pages[1:]:
        writer.add_page(page)

    # Assert: You need to inspect the file manually
    target = "annotated-pdf-link.pdf"
    with open(target, "wb") as fp:
        writer.write(fp)

    os.remove(target)  # comment this out for manual inspection


def test_annotation_builder_text():
    # Arrange
    pdf_path = RESOURCE_ROOT / "outline-without-title.pdf"
    reader = PdfReader(pdf_path)
    page = reader.pages[0]
    writer = PdfWriter()
    writer.add_page(page)

    # Act
    text_annotation = AnnotationBuilder.text(
        text="Hello World\nThis is the second line!",
        rect=(50, 550, 500, 650),
        open=True,
    )
    writer.add_annotation(0, text_annotation)

    # Assert: You need to inspect the file manually
    target = "annotated-pdf-popup.pdf"
    with open(target, "wb") as fp:
        writer.write(fp)

    os.remove(target)  # comment this out for manual inspection


def test_CheckboxRadioButtonAttributes_opt():
    assert "/Opt" in CheckboxRadioButtonAttributes.attributes_dict()


def test_name_object_invalid_decode():
    stream = BytesIO(b"/\x80\x02\x03")

    # strict:
    with pytest.raises(PdfReadError) as exc:
        NameObject.read_from_stream(stream, ReaderDummy(strict=True))
    assert exc.value.args[0] == "Illegal character in Name Object"

    # non-strict:
    stream.seek(0)
    NameObject.read_from_stream(stream, ReaderDummy(strict=False))


def test_indirect_object_invalid_read():
    stream = BytesIO(b"0 1 s")
    with pytest.raises(PdfReadError) as exc:
        IndirectObject.read_from_stream(stream, ReaderDummy())
    assert exc.value.args[0] == "Error reading indirect object reference at byte 0x5"


def test_create_string_object_force():
    assert create_string_object(b"Hello World", []) == "Hello World"
    assert create_string_object(b"Hello World", {72: "A"}) == "Aello World"
    assert create_string_object(b"Hello World", "utf8") == "Hello World"
