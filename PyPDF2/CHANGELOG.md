# CHANGELOG

## Version 2.10.3, 2022-08-21

### Robustness (ROB)
-  Decrypt returns empty bytestring (#1258)

### Developer Experience (DEV)
-  Modify CI to better verify built package contents (#1244)

### Maintenance (MAINT)
-  Remove 'mine' as PdfMerger always creates the stream (#1261)
-  Let PdfMerger._create_stream raise NotImplemented (#1251)
-  password param of _security._alg32(...) is only a string, not bytes (#1259)
-  Remove unreachable code in read_block_backwards (#1250)
   and sign function in _extract_text (#1262)

### Testing (TST)
-  Delete annotations (#1263)
-  Close PdfMerger in tests (#1260)
-  PdfReader.xmp_metadata workflow (#1257)
-  Various PdfWriter (Layout, Bookmark deprecation) (#1249)

Full Changelog: https://github.com/py-pdf/PyPDF2/compare/2.10.2...2.10.3

## Version 2.10.2, 2022-08-15

BUG: Add PyPDF2.generic to PyPI distribution

## Version 2.10.1, 2022-08-15

### Bug Fixes (BUG)
-  TreeObject.remove_child had a non-PdfObject assignment for Count (#1233, #1234)
-  Fix stream truncated prematurely (#1223)

### Documentation (DOC)
-  Fix docstring formatting (#1228)

### Maintenance (MAINT)
-  Split generic.py (#1229)

### Testing (TST)
-  Decrypt AlgV4 with owner password (#1239)
-  AlgV5.generate_values (#1238)
-  TreeObject.remove_child / empty_tree (#1235, #1236)
-  create_string_object (#1232)
-  Free-Text annotations (#1231)
-  generic._base (#1230)
-  Strict get fonts (#1226)
-  Increase PdfReader coverage (#1219, #1225)
-  Increase PdfWriter coverage (#1237)
-  100% coverage for utils.py (#1217)
-  PdfWriter exception non-binary stream (#1218)
-  Don't check coverage for deprecated code (#1216)

Full Changelog: https://github.com/py-pdf/PyPDF2/compare/2.10.0...2.10.1


## Version 2.10.0, 2022-08-07

### New Features (ENH)
-  "with" support for PdfMerger and PdfWriter (#1193)
-  Add AnnotationBuilder.text(...) to build text annotations (#1202)

### Bug Fixes (BUG)
-  Allow IndirectObjects as stream filters (#1211)

### Documentation (DOC)
-  Font scrambling
-  Page vs Content scaling (#1208)
-  Example for orientation parameter of extract_text (#1206)
-  Fix AnnotationBuilder parameter formatting (#1204)

### Developer Experience (DEV)
-  Add flake8-print (#1203)

### Maintenance (MAINT)
-  Introduce WrongPasswordError / FileNotDecryptedError / EmptyFileError  (#1201)

Full Changelog: https://github.com/py-pdf/PyPDF2/compare/2.9.0...2.10.0

## Version 2.9.0, 2022-07-31

### New Features (ENH)
-  Add ability to add hex encoded colors to outline items (#1186)
-  Add support for pathlib.Path in PdfMerger.merge (#1190)
-  Add link annotation (#1189)
-  Add capability to filter text extraction by orientation (#1175)

### Bug Fixes (BUG)
-  Named Dest in PDF1.1 (#1174)
-  Incomplete Graphic State save/restore (#1172)

### Documentation (DOC)
-  Update changelog url in package metadata (#1180)
-  Mantion camelot for table extraction (#1179)
-  Mention pyHanko for signing PDF documents (#1178)
-  Weow have CMAP support since a while (#1177)

### Maintenance (MAINT)
-  Consistant usage of warnings / log messages (#1164)
-  Consistent terminology for outline items (#1156)


Full Changelog: https://github.com/py-pdf/PyPDF2/compare/2.8.1...2.9.0

## Version 2.8.1, 2022-07-25

### Bug Fixes (BUG)
-  u_hash in AlgV4.compute_key (#1170)

### Robustness (ROB)
-  Fix loading of file from #134 (#1167)
-  Cope with empty DecodeParams (#1165)

### Documentation (DOC)
-  Typo in merger deprecation warning message (#1166)

### Maintenance (MAINT)
-  Package updates; solve mypy strict remarks (#1163)

### Testing (TST)
-  Add test from #325 (#1169)

Full Changelog: https://github.com/py-pdf/PyPDF2/compare/2.8.0...2.8.1


## Version 2.8.0, 2022-07-24

### New Features (ENH)
-  Add writer.add_annotation, page.annotations, and generic.AnnotationBuilder (#1120)

### Bug Fixes (BUG)
-  Set /AS for /Btn form fields in writer (#1161)
-  Ignore if /Perms verify failed (#1157)

### Robustness (ROB)
-  Cope with utf16 character for space calculation (#1155)
-  Cope with null params for FitH / FitV destination (#1152)
-  Handle outlines without valid destination (#1076)

### Developer Experience (DEV)
-  Introduce _utils.logger_warning (#1148)

### Maintenance (MAINT)
-  Break up parse_to_unicode (#1162)
-  Add diagnostic output to exception in read_from_stream (#1159)
-  Reduce PdfReader.read complexity (#1151)

### Testing (TST)
-  Add workflow tests found by arc testing (#1154)
-  Decrypt file which is not encrypted (#1149)
-  Test CryptRC4 encryption class; test image extraction filters (#1147)

Full Changelog: https://github.com/py-pdf/PyPDF2/compare/2.7.0...2.8.0

## Version 2.7.0, 2022-07-21

### New Features (ENH)
-  Add `outline_count` property (#1129)

### Bug Fixes (BUG)
-  Make reader.get_fields also return dropdowns with options (#1114)
-  Add deprecated EncodedStreamObject functions back until PyPDF2==3.0.0 (#1139)

### Robustness (ROB)
-  Cope with missing /W entry (#1136)
-  Cope with invalid parent xref (#1133)

### Documentation (DOC)
-  Contributors file (#1132)
-  Fix type in signature of PdfWriter.add_uri (#1131)

### Developer Experience (DEV)
-  Add .git-blame-ignore-revs (#1141)

### Code Style (STY)
-  Fixing typos (#1137)
-  Re-use code via get_outlines_property in tests (#1130)

Full Changelog: https://github.com/py-pdf/PyPDF2/compare/2.6.0...2.7.0

## Version 2.6.0, 2022-07-17

### New Features (ENH)
-  Add color and font_format to PdfReader.outlines[i] (#1104)
-  Extract Text Enhancement (whitespaces) (#1084)

### Bug Fixes (BUG)
-  Use `build_destination` for named destination outlines (#1128)
-  Avoid a crash when a ToUnicode CMap has an empty dstString in beginbfchar (#1118)
-  Prevent deduplication of PageObject (#1105)
-  None-check in DictionaryObject.read_from_stream (#1113)
-  Avoid IndexError in _cmap.parse_to_unicode (#1110)

### Documentation (DOC)
-  Explanation for git submodule
-  Watermark and stamp (#1095)

### Maintenance (MAINT)
-  Text extraction improvements (#1126)
-  Destination.color returns ArrayObject instead of tuple as fallback (#1119)
-  Use add_bookmark_destination in add_bookmark (#1100)
-  Use add_bookmark_destination in add_bookmark_dict (#1099)

### Testing (TST)
-  Add test for arab text (#1127)
-  Add xfail for decryption fail (#1125)
-  Add xfail test for IndexError when extracting text (#1124)
-  Add MCVE showing outline title issue (#1123)

### Code Style (STY)
-  Use IntFlag for permissions_flag / update_page_form_field_values (#1094)
-  Simplify code (#1101)

Full Changelog: https://github.com/py-pdf/PyPDF2/compare/2.5.0...2.6.0

## Version 2.5.0, 2022-07-10

### New Features (ENH)
-  Add support for indexed color spaces / BitsPerComponent for decoding PNGs (#1067)
-  Add PageObject._get_fonts (#1083)

### Performance Improvements (PI)
-  Use iterative DFS in PdfWriter._sweep_indirect_references (#1072)

### Bug Fixes (BUG)
-  Let Page.scale also scale the crop-/trim-/bleed-/artbox (#1066)
-  Column default for CCITTFaxDecode (#1079)

### Robustness (ROB)
-  Guard against None-value in _get_outlines (#1060)

### Documentation (DOC)
-  Stamps and watermarks (#1082)
-  OCR vs PDF text extraction (#1081)
-  Python Version support
-  Formatting of CHANGELOG

### Developer Experience (DEV)
-  Cache downloaded files (#1070)
-  Speed-up for CI (#1069)

### Maintenance (MAINT)
-  Set page.rotate(angle: int) (#1092)
-  Issue #416 was fixed by #1015 (#1078)

### Testing (TST)
-  Image extraction (#1080)
-  Image extraction (#1077)

### Code Style (STY)
-  Apply black
-  Typo in Changelog

Full Changelog: https://github.com/py-pdf/PyPDF2/compare/2.4.2...2.5.0

## Version 2.4.2, 2022-07-05

### New Features (ENH)
-  Add PdfReader.xfa attribute (#1026)

### Bug Fixes (BUG)
-  Wrong page inserted when PdfMerger.merge is done (#1063)
-  Resolve IndirectObject when it refers to a free entry (#1054)

### Developer Experience (DEV)
-  Added {posargs} to tox.ini (#1055)

### Maintenance (MAINT)
-  Remove PyPDF2._utils.bytes_type (#1053)

### Testing (TST)
-  Scale page (indirect rect object) (#1057)
-  Simplify pathlib PdfReader test (#1056)
-  IndexError of VirtualList (#1052)
-  Invalid XML in xmp information (#1051)
-  No pycryptodome (#1050)
-  Increase test coverage (#1045)

### Code Style (STY)
-  DOC of compress_content_streams (#1061)
-  Minimize diff for #879 (#1049)

[Full Changelog](https://github.com/py-pdf/PyPDF2/compare/2.4.1...2.4.2)

## Version 2.4.1, 2022-06-30

### New Features (ENH)
-  Add writer.pdf_header property (getter and setter) (#1038)

### Performance Improvements (PI)
-  Remove b_ call in FloatObject.write_to_stream (#1044)
-  Check duplicate objects in writer._sweep_indirect_references (#207)

### Documentation (DOC)
-  How to surppress exceptions/warnings/log messages (#1037)
-  Remove hyphen from lossless (#1041)
-  Compression of content streams (#1040)
-  Fix inconsistent variable names in add-watermark.md (#1039)
-  File size reduction
-  Add CHANGELOG to the rendered docs (#1023)

### Maintenance (MAINT)
-  Handle XML error when reading XmpInformation (#1030)
-  Deduplicate Code / add mutmut config (#1022)

### Code Style (STY)
-  Use unnecessary one-line function / class attribute (#1043)
-  Docstring formatting (#1033)

[Full Changelog](https://github.com/py-pdf/PyPDF2/compare/2.4.0...2.4.1)

## Version 2.4.0, 2022-06-26

### New Features (ENH):
-  Support R6 decrypting (#1015)
-  Add PdfReader.pdf_header (#1013)

### Performance Improvements (PI):
-  Remove ord_ calls (#1014)

### Bug Fixes (BUG):
-  Fix missing page for bookmark (#1016)

### Robustness (ROB):
-  Deal with invalid Destinations (#1028)

### Documentation (DOC):
-  get_form_text_fields does not extract dropdown data (#1029)
-  Adjust PdfWriter.add_uri docstring
-  Mention crypto extra_requires for installation (#1017)

### Developer Experience (DEV):
-  Use /n line endings everywhere (#1027)
-  Adjust string formatting to be able to use mutmut (#1020)
-  Update Bug report template

[Full Changelog](https://github.com/py-pdf/PyPDF2/compare/2.3.1...2.4.0)

## Version 2.3.1, 2022-06-19

BUG: Forgot to add the interal `_codecs` subpackage.

[Full Changelog](https://github.com/py-pdf/PyPDF2/compare/2.3.0...2.3.1)

## Version 2.3.0, 2022-06-19

The highlight of this release is improved support for file encryption
(AES-128 and AES-256, R5 only). See #749 for the amazing work of
@exiledkingcc 🎊 Thank you 🤗

### Deprecations (DEP)
-  Rename names to be PEP8-compliant (#967)
  - `PdfWriter.get_page`: the pageNumber parameter is renamed to page_number
  - `PyPDF2.filters`:
    * For all classes, a parameter rename: decodeParms ➔ decode_parms
    * decodeStreamData ➔ decode_stream_data
  - `PyPDF2.xmp`:
    * XmpInformation.rdfRoot ➔ XmpInformation.rdf_root
    * XmpInformation.xmp_createDate ➔ XmpInformation.xmp_create_date
    * XmpInformation.xmp_creatorTool ➔ XmpInformation.xmp_creator_tool
    * XmpInformation.xmp_metadataDate ➔ XmpInformation.xmp_metadata_date
    * XmpInformation.xmp_modifyDate ➔ XmpInformation.xmp_modify_date
    * XmpInformation.xmpMetadata ➔ XmpInformation.xmp_metadata
    * XmpInformation.xmpmm_documentId ➔ XmpInformation.xmpmm_document_id
    * XmpInformation.xmpmm_instanceId ➔ XmpInformation.xmpmm_instance_id
  - `PyPDF2.generic`:
    * readHexStringFromStream ➔ read_hex_string_from_stream
    * initializeFromDictionary ➔ initialize_from_dictionary
    * createStringObject ➔ create_string_object
    * TreeObject.hasChildren ➔ TreeObject.has_children
    * TreeObject.emptyTree ➔ TreeObject.empty_tree

### New Features (ENH)
-  Add decrypt support for V5 and AES-128, AES-256 (R5 only) (#749)

### Robustness (ROB)
-  Fix corrupted (wrongly) linear PDF (#1008)

### Maintenance (MAINT)
-  Move PDF_Samples folder into ressources
-  Fix typos (#1007)

### Testing (TST)
-  Improve encryption/decryption test (#1009)
-  Add merger test cases with real PDFs (#1006)
-  Add mutmut config

### Code Style (STY)
-  Put pure data mappings in separate files (#1005)
-  Make encryption module private, apply pre-commit (#1010)

[Full Changelog](https://github.com/py-pdf/PyPDF2/compare/2.2.1...2.3.0)

## Version 2.2.1, 2022-06-17

### Performance Improvements (PI)
-  Remove b_ calls (#992, #986)
-  Apply improvements to _utils suggested by perflint (#993)

### Robustness (ROB)
-  utf-16-be\' codec can\'t decode (...) (#995)

### Documentation (DOC)
-  Remove reference to Scripts (#987)

### Developer Experience (DEV)
-  Fix type annotations for add_bookmarks (#1000)

### Testing (TST)
-  Add test for PdfMerger (#1001)
-  Add tests for XMP information (#996)
-  reader.get_fields / zlib issue / LZW decode issue (#1004)
-  reader.get_fields with report generation (#1002)
-  Improve test coverage by extracting texts (#998)

### Code Style (STY)
-  Apply fixes suggested by pylint (#999)

[Full Changelog](https://github.com/py-pdf/PyPDF2/compare/2.2.0...2.2.1)

## Version 2.2.0, 2022-06-13

The 2.2.0 release improves text extraction again via (#969):

* Improvements around /Encoding / /ToUnicode
* Extraction of CMaps improved
* Fallback for font def missing
* Support for /Identity-H and /Identity-V: utf-16-be
* Support for /GB-EUC-H / /GB-EUC-V / GBp/c-EUC-H / /GBpc-EUC-V (beta release for evaluation)
* Arabic (for evaluation)
* Whitespace extraction improvements

Those changes should mainly improve the text extraction for non-ASCII alphabets,
e.g. Russian / Chinese / Japanese / Korean / Arabic.

[Full Changelog](https://github.com/py-pdf/PyPDF2/compare/2.1.1...2.2.0)

## Version 2.1.1, 2022-06-12

### New Features (ENH)
-  Add support for pathlib as input for PdfReader (#979)

### Performance Improvements (PI)
-  Optimize read_next_end_line (#646)

### Bug Fixes (BUG)
-  Adobe Acrobat \'Would you like to save this file?\' (#970)

### Documentation (DOC)
-  Notes on annotations (#982)
-  Who uses PyPDF2
-  intendet \xe2\x9e\x94 in robustness page  (#958)

### Maintenance (MAINT)
-  pre-commit / requirements.txt updates (#977)
-  Mark read_next_end_line as deprecated (#965)
-  Export `PageObject` in PyPDF2 root (#960)

### Testing (TST)
-  Add MCVE of issue #416 (#980)
-  FlateDecode.decode decodeParms (#964)
-  Xmp module (#962)
-  utils.paeth_predictor (#959)

### Code Style (STY)
-  Use more tuples and list/dict comprehensions (#976)

[Full Changelog](https://github.com/py-pdf/PyPDF2/compare/2.1.0...2.1.1)


## Version 2.1.0, 2022-06-06

The highlight of the 2.1.0 release is the most massive improvement to the
text extraction capabilities of PyPDF2 since 2016 🥳🎊 A very big thank you goes
to [pubpub-zz](https://github.com/pubpub-zz) who took a lot of time and
knowledge about the PDF format to finally get those improvements into PyPDF2.
Thank you 🤗💚

In case the new function causes any issues, you can use `_extract_text_old`
for the old functionality. Please also open a bug ticket in that case.

There were several people who have attempted to bring similar improvements to
PyPDF2. All of those were valuable. The main reason why they didn't get merged
is the big amount of open PRs / issues. pubpub-zz was the most comprehensive
PR which also incorporated the latest changes of PyPDF2 2.0.0.

Thank you to [VictorCarlquist](https://github.com/VictorCarlquist) for #858 and
[asabramo](https://github.com/asabramo) for #464 🤗

### New Features (ENH)
-  Massive text extraction improvement (#924). Closed many open issues:
    - Exceptions / missing spaces in extract_text() method (#17) 🕺
      - Whitespace issues in extract_text() (#42) 💃
      - pypdf2 reads the hifenated words in a new line (#246)
    - PyPDF2 failing to read unicode character (#37)
      - Unable to read bullets (#230)
    - ExtractText yields nothing for apparently good PDF (#168) 🎉
    - Encoding issue in extract_text() (#235)
    - extractText() doesn't work on Chinese PDF (#252)
    - encoding error (#260)
    - Trouble with apostophes in names in text "O'Doul" (#384)
    - extract_text works for some PDF files, but not the others (#437)
    - Euro sign not being recognized by extractText (#443)
    - Failed extracting text from French texts (#524)
    - extract_text doesn't extract ligatures correctly (#598)
    - reading spanish text - mark convert issue (#635)
    - Read PDF changed from text to random symbols (#654)
    - .extractText() reads / as 1. (#789)
-  Update glyphlist (#947) - inspired by #464
-  Allow adding PageRange objects (#948)

### Bug Fixes (BUG)
-  Delete .python-version file (#944)
-  Compare StreamObject.decoded_self with None (#931)

### Robustness (ROB)
-  Fix some conversion errors on non conform PDF (#932)

### Documentation (DOC)
-  Elaborate on PDF text extraction difficulties (#939)
-  Add logo (#942)
-  rotate vs Transformation().rotate (#937)
-  Example how to use PyPDF2 with AWS S3 (#938)
-  How to deprecate (#930)
-  Fix typos on robustness page (#935)
-  Remove scripts (pdfcat) from docs (#934)

### Developer Experience (DEV)
-  Ignore .python-version file
-  Mark deprecated code with no-cover (#943)
-  Automatically create Github releases from tags (#870)

### Testing (TST)
-  Text extraction for non-latin alphabets (#954)
-  Ignore PdfReadWarning in benchmark (#949)
-  writer.remove_text (#946)
-  Add test for Tree and _security (#945)

### Code Style (STY)
-  black, isort, Flake8, splitting buildCharMap (#950)

[Full Changelog](https://github.com/py-pdf/PyPDF2/compare/2.0.0...2.1.0)

## Version 2.0.0, 2022-06-01

The 2.0.0 release of PyPDF2 includes three core changes:

1. Dropping support for Python 3.5 and older.
2. Introducing type annotations.
3. Interface changes, mostly to have PEP8-compliant names

We introduced a [deprecation process](https://github.com/py-pdf/PyPDF2/pull/930)
that hopefully helps users to avoid unexpected breaking changes.

### Breaking Changes (DEP)
- PyPDF2 2.0 requires Python 3.6+. Python 2.7 and 3.5 support were dropped.
- PdfFileReader: The "warndest" parameter was removed
- PdfFileReader and PdfFileMerger no longer have the `overwriteWarnings`
  parameter. The new behavior is `overwriteWarnings=False`.
- merger: OutlinesObject was removed without replacement.
- merger.py ➔ _merger.py: You must import PdfFileMerger from PyPDF2 directly.
- utils:
  * `ConvertFunctionsToVirtualList` was removed
  * `formatWarning` was removed
  * `isInt(obj)`: Use `instance(obj, int)` instead
  * `u_(s)`: Use `s` directly
  * `chr_(c)`: Use `chr(c)` instead
  * `barray(b)`: Use `bytearray(b)` instead
  * `isBytes(b)`: Use `instance(b, type(bytes()))` instead
  * `xrange_fn`: Use `range` instead
  * `string_type`: Use `str` instead
  * `isString(s)`: Use `instance(s, str)` instead
  * `_basestring`: Use `str` instead
  * All Exceptions are now in `PyPDF2.errors`:
    - PageSizeNotDefinedError
    - PdfReadError
    - PdfReadWarning
    - PyPdfError
- `PyPDF2.pdf` (the `pdf` module) no longer exists. The contents were moved with
  the library. You should most likely import directly from `PyPDF2` instead.
  The `RectangleObject` is in `PyPDF2.generic`.
- The `Resources`, `Scripts`, and `Tests` will no longer be part of the distribution
  files on PyPI. This should have little to no impact on most people. The
  `Tests` are renamed to `tests`, the `Resources` are renamed to `resources`.
  Both are still in the git repository. The `Scripts` are now in
  [cpdf](https://github.com/py-pdf/cpdf). `Sample_Code` was moved to the `docs`.

For a full list of deprecated functions, please see the changelog of version
1.28.0.

### New Features (ENH)
-  Improve space setting for text extraction (#922)
-  Allow setting the decryption password in `PdfReader.__init__` (#920)
-  Add Page.add_transformation (#883)

### Bug Fixes (BUG)
-  Fix error adding transformation to page without /Contents (#908)

### Robustness (ROB)
-  Cope with invalid length in streams (#861)

### Documentation (DOC)
-  Fix style of 1.25 and 1.27 patch notes (#927)
-  Transformation (#907)

### Developer Experience (DEV)
-  Create flake8 config file (#916)
-  Use relative imports (#875)

### Maintenance (MAINT)
-  Use Python 3.6 language features (#849)
-  Add wrapper function for PendingDeprecationWarnings (#928)
-  Use new PEP8 compliant names (#884)
-  Explicitly represent transformation matrix (#878)
-  Inline PAGE_RANGE_HELP string (#874)
-  Remove unnecessary generics imports (#873)
-  Remove star imports (#865)
-  merger.py ➔ _merger.py (#864)
-  Type annotations for all functions/methods (#854)
-  Add initial type support with mypy (#853)

### Testing (TST)
-  Regression test for xmp_metadata converter (#923)
-  Checkout submodule sample-files for benchmark
-  Add text extracting performance benchmark
-  Use new PyPDF2 API in benchmark (#902)
-  Make test suite fail for uncaught warnings (#892)
-  Remove -OO testrun from CI (#901)
-  Improve tests for convert_to_int (#899)

[Full Changelog](https://github.com/py-pdf/PyPDF2/compare/1.28.4...2.0.0)

## Version 1.28.4, 2022-05-29

Bug Fixes (BUG):
-  XmpInformation._converter_date was unusable (#921)

[Full Changelog](https://github.com/py-pdf/PyPDF2/compare/1.28.3...1.28.4)

## Version 1.28.3, 2022-05-28

### Deprecations (DEP)
-  PEP8 renaming (#905)

### Bug Fixes (BUG)
-  XmpInformation missing method _getText (#917)
-  Fix PendingDeprecationWarning on _merge_page (#904)

[Full Changelog](https://github.com/py-pdf/PyPDF2/compare/1.28.2...1.28.3)

## Version 1.28.2, 2022-05-23

### Bug Fixes (BUG)
-  PendingDeprecationWarning for getContents (#893)
-  PendingDeprecationWarning on using PdfMerger (#891)

[Full Changelog](https://github.com/py-pdf/PyPDF2/compare/1.28.1...1.28.2)

## Version 1.28.1, 2022-05-22

### Bug Fixes (BUG)
-  Incorrectly show deprecation warnings on internal usage (#887)

### Maintenance (MAINT)
-  Add stacklevel=2 to deprecation warnings (#889)
-  Remove duplicate warnings imports (#888)

[Full Changelog](https://github.com/py-pdf/PyPDF2/compare/1.28.0...1.28.1)

## Version 1.28.0, 2022-05-22

This release adds a lot of deprecation warnings in preparation of the
PyPDF2 2.0.0 release. The changes are mostly using snake_case function-, method-,
and variable-names as well as using properties instead of getter-methods.

Maintenance (MAINT):
-  Remove IronPython Fallback for zlib (#868)

[Full Changelog](https://github.com/py-pdf/PyPDF2/compare/1.27.12...1.27.13)

### Deprecations (DEP)

* Make the `PyPDF2.utils` module private
* Rename of core classes:
  * PdfFileReader ➔ PdfReader
  * PdfFileWriter ➔ PdfWriter
  * PdfFileMerger ➔ PdfMerger
* Use PEP8 conventions for function names and parameters
* If a property and a getter-method are both present, use the property

#### Details

In many places:
  - getObject ➔ get_object
  - writeToStream ➔ write_to_stream
  - readFromStream ➔ read_from_stream

PyPDF2.generic
  - readObject ➔ read_object
  - convertToInt ➔ convert_to_int
  - DocumentInformation.getText ➔ DocumentInformation._get_text :
    This method should typically not be used; please let me know if you need it.

PdfReader class:
  - `reader.getPage(pageNumber)` ➔ `reader.pages[page_number]`
  - `reader.getNumPages()` / `reader.numPages` ➔ `len(reader.pages)`
  - getDocumentInfo ➔ metadata
  - flattenedPages attribute ➔ flattened_pages
  - resolvedObjects attribute ➔ resolved_objects
  - xrefIndex attribute ➔ xref_index
  - getNamedDestinations / namedDestinations attribute ➔ named_destinations
  - getPageLayout / pageLayout ➔ page_layout attribute
  - getPageMode / pageMode ➔ page_mode attribute
  - getIsEncrypted / isEncrypted ➔ is_encrypted attribute
  - getOutlines ➔ get_outlines
  - readObjectHeader ➔ read_object_header
  - cacheGetIndirectObject ➔ cache_get_indirect_object
  - cacheIndirectObject ➔ cache_indirect_object
  - getDestinationPageNumber ➔ get_destination_page_number
  - readNextEndLine ➔ read_next_end_line
  - _zeroXref ➔ _zero_xref
  - _authenticateUserPassword ➔ _authenticate_user_password
  - _pageId2Num attribute ➔ _page_id2num
  - _buildDestination ➔ _build_destination
  - _buildOutline ➔ _build_outline
  - _getPageNumberByIndirect(indirectRef) ➔ _get_page_number_by_indirect(indirect_ref)
  - _getObjectFromStream ➔ _get_object_from_stream
  - _decryptObject ➔ _decrypt_object
  - _flatten(..., indirectRef) ➔ _flatten(..., indirect_ref)
  - _buildField ➔ _build_field
  - _checkKids ➔ _check_kids
  - _writeField ➔ _write_field
  - _write_field(..., fieldAttributes) ➔ _write_field(..., field_attributes)
  - _read_xref_subsections(..., getEntry, ...) ➔ _read_xref_subsections(..., get_entry, ...)

PdfWriter class:
  - `writer.getPage(pageNumber)` ➔ `writer.pages[page_number]`
  - `writer.getNumPages()` ➔ `len(writer.pages)`
  - addMetadata ➔ add_metadata
  - addPage ➔ add_page
  - addBlankPage ➔ add_blank_page
  - addAttachment(fname, fdata) ➔ add_attachment(filename, data)
  - insertPage ➔ insert_page
  - insertBlankPage ➔ insert_blank_page
  - appendPagesFromReader ➔ append_pages_from_reader
  - updatePageFormFieldValues ➔ update_page_form_field_values
  - cloneReaderDocumentRoot ➔ clone_reader_document_root
  - cloneDocumentFromReader ➔ clone_document_from_reader
  - getReference ➔ get_reference
  - getOutlineRoot ➔ get_outline_root
  - getNamedDestRoot ➔ get_named_dest_root
  - addBookmarkDestination ➔ add_bookmark_destination
  - addBookmarkDict ➔ add_bookmark_dict
  - addBookmark ➔ add_bookmark
  - addNamedDestinationObject ➔ add_named_destination_object
  - addNamedDestination ➔ add_named_destination
  - removeLinks ➔ remove_links
  - removeImages(ignoreByteStringObject) ➔ remove_images(ignore_byte_string_object)
  - removeText(ignoreByteStringObject) ➔ remove_text(ignore_byte_string_object)
  - addURI ➔ add_uri
  - addLink ➔ add_link
  - getPage(pageNumber) ➔ get_page(page_number)
  - getPageLayout / setPageLayout / pageLayout ➔ page_layout attribute
  - getPageMode / setPageMode / pageMode ➔ page_mode attribute
  - _addObject ➔ _add_object
  - _addPage ➔ _add_page
  - _sweepIndirectReferences ➔ _sweep_indirect_references

PdfMerger class
  - `__init__` parameter: strict=True ➔ strict=False (the PdfFileMerger still has the old default)
  - addMetadata ➔ add_metadata
  - addNamedDestination ➔ add_named_destination
  - setPageLayout ➔ set_page_layout
  - setPageMode ➔ set_page_mode

Page class:
  - artBox / bleedBox/ cropBox/ mediaBox / trimBox ➔ artbox / bleedbox/ cropbox/ mediabox / trimbox
    - getWidth, getHeight  ➔ width / height
    - getLowerLeft_x / getUpperLeft_x ➔ left
    - getUpperRight_x / getLowerRight_x ➔ right
    - getLowerLeft_y / getLowerRight_y ➔ bottom
    - getUpperRight_y / getUpperLeft_y ➔ top
    - getLowerLeft / setLowerLeft ➔ lower_left property
    - upperRight ➔ upper_right
  - mergePage ➔ merge_page
  - rotateClockwise / rotateCounterClockwise ➔ rotate_clockwise
  - _mergeResources ➔ _merge_resources
  - _contentStreamRename ➔ _content_stream_rename
  - _pushPopGS ➔ _push_pop_gs
  - _addTransformationMatrix ➔ _add_transformation_matrix
  - _mergePage ➔ _merge_page

XmpInformation class:
  - getElement(..., aboutUri, ...) ➔ get_element(..., about_uri, ...)
  - getNodesInNamespace(..., aboutUri, ...) ➔ get_nodes_in_namespace(..., aboutUri, ...)
  - _getText ➔ _get_text

utils.py:
  - matrixMultiply ➔ matrix_multiply
  - RC4_encrypt is moved to the security module

## Version 1.27.12, 2022-05-02

### Bug Fixes (BUG)
-  _rebuild_xref_table expects trailer to be a dict (#857)

### Documentation (DOC)
-  Security Policy

[Full Changelog](https://github.com/py-pdf/PyPDF2/compare/1.27.11...1.27.12)

## Version 1.27.11, 2022-05-02

### Bug Fixes (BUG)
-  Incorrectly issued xref warning/exception (#855)

[Full Changelog](https://github.com/py-pdf/PyPDF2/compare/1.27.10...1.27.11)

## Version 1.27.10, 2022-05-01

### Robustness (ROB)
-  Handle missing destinations in reader (#840)
-  warn-only in readStringFromStream (#837)
-  Fix corruption in startxref or xref table (#788 and #830)

### Documentation (DOC)
-  Project Governance (#799)
-  History of PyPDF2
-  PDF feature/version support (#816)
-  More details on text parsing issues (#815)

### Developer Experience (DEV)
-  Add benchmark command to Makefile
-  Ignore IronPython parts for code coverage (#826)

### Maintenance (MAINT)
-  Split pdf module (#836)
-  Separated CCITTFax param parsing/decoding (#841)
-  Update requirements files

### Testing (TST)
-  Use external repository for larger/more PDFs for testing (#820)
-  Swap incorrect test names (#838)
-  Add test for PdfFileReader and page properties (#835)
-  Add tests for PyPDF2.generic (#831)
-  Add tests for utils, form fields, PageRange (#827)
-  Add test for ASCII85Decode (#825)
-  Add test for FlateDecode (#823)
-  Add test for filters.ASCIIHexDecode (#822)

### Code Style (STY)
-  Apply pre-commit (black, isort) + use snake_case variables (#832)
-  Remove debug code (#828)
-  Documentation, Variable names (#839)

[Full Changelog](https://github.com/py-pdf/PyPDF2/compare/1.27.9...1.27.10)

## Version 1.27.9, 2022-04-24

A change I would like to highlight is the performance improvement for
large PDF files (#808) 🎉

### New Features (ENH)
-  Add papersizes (#800)
-  Allow setting permission flags when encrypting (#803)
-  Allow setting form field flags (#802)

### Bug Fixes (BUG)
-  TypeError in xmp._converter_date (#813)
-  Improve spacing for text extraction (#806)
-  Fix PDFDocEncoding Character Set (#809)

### Robustness (ROB)
-  Use null ID when encrypted but no ID given (#812)
-  Handle recursion error (#804)

### Documentation (DOC)
-  CMaps (#811)
-  The PDF Format + commit prefixes (#810)
-  Add compression example (#792)

### Developer Experience (DEV)
-  Add Benchmark for Performance Testing (#781)

### Maintenance (MAINT)
-  Validate PDF magic byte in strict mode (#814)
-  Make PdfFileMerger.addBookmark() behave life PdfFileWriters\' (#339)
-  Quadratic runtime while parsing reduced to linear  (#808)

### Testing (TST)
-  Newlines in text extraction (#807)

[Full Changelog](https://github.com/py-pdf/PyPDF2/compare/1.27.8...1.27.9)

## Version 1.27.8, 2022-04-21

### Bug Fixes (BUG)
-  Use 1MB as offset for readNextEndLine (#321)
-  'PdfFileWriter' object has no attribute 'stream' (#787)

### Robustness (ROB)
-  Invalid float object; use 0 as fallback (#782)

### Documentation (DOC)
-  Robustness (#785)

[Full Changelog](https://github.com/py-pdf/PyPDF2/compare/1.27.7...1.27.8)

## Version 1.27.7, 2022-04-19

### Bug Fixes (BUG)
- Import exceptions from PyPDF2.errors in PyPDF2.utils (#780)

### Code Style (STY)
-  Naming in 'make_changelog.py'

## Version 1.27.6, 2022-04-18

### Deprecations (DEP)
-  Remove support for Python 2.6 and older (#776)

### New Features (ENH)
-  Extract document permissions (#320)

### Bug Fixes (BUG)
-  Clip by trimBox when merging pages, which would otherwise be ignored (#240)
-  Add overwriteWarnings parameter PdfFileMerger (#243)
-  IndexError for getPage() of decryped file (#359)
-  Handle cases where decodeParms is an ArrayObject (#405)
-  Updated PDF fields don't show up when page is written (#412)
-  Set Linked Form Value (#414)
-  Fix zlib -5 error for corrupt files (#603)
-  Fix reading more than last1K for EOF (#642)
-  Acciental import

### Robustness (ROB)
-  Allow extra whitespace before "obj" in readObjectHeader (#567)

### Documentation (DOC)
-  Link to pdftoc in Sample_Code (#628)
-  Working with annotations (#764)
-  Structure history

### Developer Experience (DEV)
-  Add issue templates (#765)
-  Add tool to generate changelog

### Maintenance (MAINT)
-  Use grouped constants instead of string literals (#745)
-  Add error module (#768)
-  Use decorators for @staticmethod (#775)
-  Split long functions (#777)

### Testing (TST)
-  Run tests in CI once with -OO Flags (#770)
-  Filling out forms (#771)
-  Add tests for Writer (#772)
-  Error cases (#773)
-  Check Error messages (#769)
-  Regression test for issue #88
-  Regression test for issue #327

### Code Style (STY)
-  Make variable naming more consistent in tests


[Full changelog](https://github.com/py-pdf/PyPDF2/compare/1.27.5...1.27.6)

## Version 1.27.5, 2022-04-15

### Security (SEC)

- ContentStream_readInlineImage had potential infinite loop (#740)

### Bug fixes (BUG)

- Fix merging encrypted files (#757)
- CCITTFaxDecode decodeParms can be an ArrayObject (#756)

### Robustness improvements (ROBUST)

- title sometimes None (#744)

### Documentation (DOC)

- Adjust short description of the package

### Tests and Test setup (TST)

- Rewrite JS tests from unittest to pytest (#746)
- Increase Test coverage, mainly with filters (#756)
- Add test for inline images (#758)

### Developer Experience Improvements (DEV)

- Remove unused Travis-CI configuration (#747)
- Show code coverage (#754, #755)
- Add mutmut (#760)

### Miscellaneous

- STY: Closing file handles, explicit exports, ... (#743)

[Full Changelog](https://github.com/py-pdf/PyPDF2/compare/1.27.4...1.27.5)


## Version 1.27.4, 2022-04-12

### Bug fixes (BUG)

- Guard formatting of `__init__.__doc__` string (#738)

### Packaging (PKG)

- Add more precise license field to setup (#733)

### Testing (TST)

- Add test for issue #297

### Miscellaneous

- DOC: Miscallenious ➔ Miscellaneous (Typo)
- TST: Fix CI triggering (master ➔ main) (#739)
- STY: Fix various style issues (#742)

[Full Changelog](https://github.com/py-pdf/PyPDF2/compare/1.27.3...1.27.4)

## Version 1.27.3, 2022-04-10

- PKG: Make Tests not a subpackage (#728)
- BUG: Fix ASCII85Decode.decode assertion (#729)
- BUG: Error in Chinese character encoding (#463)
- BUG: Code duplication in Scripts/2-up.py
- ROBUST: Guard 'obj.writeToStream' with 'if obj is not None'
- ROBUST: Ignore a /Prev entry with the value 0 in the trailer
- MAINT: Remove Sample_Code (#726)
- TST: Close file handle in test_writer (#722)
- TST: Fix test_get_images (#730)
- DEV: Make tox use pytest and add more Python versions (#721)
- DOC: Many (#720, #723-725, #469)

[Full Changelog](https://github.com/py-pdf/PyPDF2/compare/1.27.2...1.27.3)

## Version 1.27.2, 2022-04-09

- Add Scripts (including `pdfcat`), Resources, Tests, and Sample_Code back to
  PyPDF2. It was removed by accident in 1.27.0, but might get removed with 2.0.0
  See [discussions/718](https://github.com/py-pdf/PyPDF2/discussions/718).

[Full Changelog](https://github.com/py-pdf/PyPDF2/compare/1.27.1...1.27.2)

## Version 1.27.1, 2022-04-08

- Fixed project links on PyPI page after migration from mstamy2
  to MartinThoma to the py-pdf organization on GitHub
- Documentation is now at [pypdf2.readthedocs.io](https://pypdf2.readthedocs.io/en/latest/)

[Full Changelog](https://github.com/py-pdf/PyPDF2/compare/1.27.0...1.27.1)

## Version 1.27.0, 2022-04-07

Features:

 - Add alpha channel support for png files in Script (#614)

### Bug fixes (BUG)

 - Fix formatWarning for filename without slash (#612)
 - Add whitespace between words for extractText() (#569, #334)
 - "invalid escape sequence" SyntaxError (#522)
 - Avoid error when printing warning in pythonw (#486)
 - Stream operations can be List or Dict (#665)

### Documentation (DOC)

 - Added Scripts/pdf-image-extractor.py
 - Documentation improvements (#550, #538, #324, #426, #394)

### Tests and Test setup (TST)

 - Add Github Action which automatically run unit tests via pytest and
   static code analysis with Flake8 (#660)
 - Add several unit tests (#661, #663)
 - Add .coveragerc to create coverage reports

### Developer Experience Improvements (DEV)

 - Pre commit: Developers can now `pre-commit install` to avoid tiny issues
               like trailing whitespaces

### Miscellaneous

 - Add the LICENSE file to the distributed packages (#288)
 - Use setuptools instead of distutils (#599)
 - Improvements for the PyPI page (#644)
 - Python 3 changes (#504, #366)

[Full Changelog](https://github.com/py-pdf/PyPDF2/compare/1.26.0...1.27.0)

## Version 1.26.0, 2016-05-18

 - NOTE: Active maintenance on PyPDF2 is resuming after a hiatus

 - Fixed a bug where image resources where incorrectly
   overwritten when merging pages

 - Added dictionary for JavaScript actions to the root (louib)

 - Added unit tests for the JS functionality (louib)

 - Add more Python 3 compatibility when reading inline images (im2703
   and (VyacheslavHashov)

 - Return NullObject instead of raising error when failing to resolve
   object (ctate)

 - Don't output warning for non-zeroed xref table when strict=False
   (BenRussert)

 - Remove extraneous zeroes from output formatting (speedplane)

 - Fix bug where reading an inline image would cut off prematurely
   in certain cases (speedplane)

## Version 1.25.1, 2015-07-20

 - Fix bug when parsing inline images. Occurred when merging
   certain pages with inline images

 - Fixed type error when creating outlines by utilizing the
   isString() test

## Version 1.25, 2015-07-07

BUGFIXES:

 - Added Python 3 algorithm for ASCII85Decode. Fixes issue when
   reading reportlab-generated files with Py 3 (jerickbixly)

 - Recognize more escape sequence which would otherwise throw an
   exception (manuelzs, robertsoakes)

 - Fixed overflow error in generic.py. Occurred
   when reading a too-large int in Python 2 (by Raja Jamwal)

 - Allow access to files which were encrypted with an empty
   password. Previously threw a "File has not been decrypted"
   exception (Elena Williams)

 - Do not attempt to decode an empty data stream. Previously
   would cause an error in decode algorithms (vladir)

 - Fixed some type issues specific to Py 2 or Py 3

 - Fix issue when stream data begins with whitespace (soloma83)

 - Recognize abbreviated filter names (AlmightyOatmeal and
   Matthew Weiss)

 - Copy decryption key from PdfFileReader to PdfFileMerger.
   Allows usage of PdfFileMerger with encrypted files (twolfson)

 - Fixed bug which occurred when a NameObject is present at end
   of a file stream. Threw a "Stream has ended unexpectedly"
   exception (speedplane)

FEATURES:

 - Initial work on a test suite; to be expanded in future.
   Tests and Resources directory added, README updated (robertsoakes)

 - Added document cloning methods to PdfFileWriter:
   appendPagesFromReader, cloneReaderDocumentRoot, and
   cloneDocumentFromReader. See official documentation (robertsoakes)

 - Added method for writing to form fields: updatePageFormFieldValues.
   This will be enhanced in the future. See official documentation
   (robertsoakes)

 - New addAttachment method. See documentation. Support for adding
   and extracting embedded files to be enhanced in the future
   (moshekaplan)

 - Added methods to get page number of given PageObject or
   Destination: getPageNumber and getDestinationPageNumber.
   See documentation (mozbugbox)

OTHER ENHANCEMENTS:

 - Enhanced type handling (Brent Amrhein)

 - Enhanced exception handling in NameObject (sbywater)

 - Enhanced extractText method output (peircej)

 - Better exception handling

 - Enhanced regex usage in NameObject class (speedplane)


## Version 1.24, 2014-12-31

 - Bugfixes for reading files in Python 3 (by Anthony Tuininga and
   pqqp)

 - Appropriate errors are now raised instead of infinite loops (by
   naure and Cyrus Vafadari)

 - Bugfix for parsing number tokens with leading spaces (by Maxim
   Kamenkov)

 - Don't crash on bad /Outlines reference (by eshellman)

 - Conform tabs/spaces and blank lines to PEP 8 standards

 - Utilize the readUntilRegex method when reading Number Objects
   (by Brendan Jurd)

 - More bugfixes for Python 3 and clearer exception handling

 - Fixed encoding issue in merger (with eshellman)

 - Created separate folder for scripts


## Version 1.23, 2014-08-11

 - Documentation now available at pythonhosted.org

 - Bugfix in pagerange.py for when `__init__.__doc__` has no value (by
   Vladir Cruz)

 - Fix typos in OutlinesObject().add() (by shilluc)

 - Re-added a missing return statement in a utils.py method

 - Corrected viewing mode names (by Jason Scheirer)

 - New PdfFileWriter method: addJS() (by vfigueiro)

 - New bookmark features: color, boldness, italics, and page fit
   (by Joshua Arnott)

 - New PdfFileReader method: getFields(). Used to extract field
   information from PDFs with interactive forms. See documentation
   for details

 - Converted README file to markdown format (by Stephen Bussard)

 - Several improvements to overall performance and efficiency
   (by mozbugbox)

 - Fixed a bug where geospatial information was not scaling along with
   its page

 - Fixed a type issue and a Python 3 issue in the decryption algorithms
   (with Francisco Vieira and koba-ninkigumi)

 - Fixed a bug causing an infinite loop in the ASCII 85 decoding
   algorithm (by madmaardigan)

 - Annotations (links, comment windows, etc.) are now preserved when
   pages are merged together

 - Used the Destination class in addLink() and addBookmark() so that
   the page fit option could be properly customized


## Version 1.22, 2014-05-29

 - Added .DS_Store to .gitignore (for Mac users) (by Steve Witham)

 - Removed `__init__()` implementation in NameObject (by Steve Witham)

 - Fixed bug (inf. loop) when merging pages in Python 3 (by commx)

 - Corrected error when calculating height in scaleTo()

 - Removed unnecessary code from DictionaryObject (by Georges Dubus)

 - Fixed bug where an exception was thrown upon reading a NULL string
   (by speedplane)

 - Allow string literals (non-unicode strings in Python 2) to be passed
   to PdfFileReader

 - Allow ConvertFunctionsToVirtualList to be indexed with slices and
   longs (in Python 2) (by Matt Gilson)

 - Major improvements and bugfixes to addLink() method (see documentation
   in source code) (by Henry Keiter)

 - General code clean-up and improvements (with Steve Witham and Henry Keiter)

 - Fixed bug that caused crash when comments are present at end of
   dictionary


## Version 1.21, 2014-04-21

 - Fix for when /Type isn't present in the Pages dictionary (by Rob1080)

 - More tolerance for extra whitespace in Indirect Objects

 - Improved Exception handling

 - Fixed error in getHeight() method (by Simon Kaempflein)

 - implement use of utils.string_type to resolve Py2-3 compatibility issues

 - Prevent exception for multiple definitions in a dictionary (with carlosfunk)
   (only when strict = False)

 - Fixed errors when parsing a slice using pdfcat on command line (by
   Steve Witham)

 - Tolerance for EOF markers within 1024 bytes of the actual end of the
   file (with David Wolever)

 - Added overwriteWarnings parameter to PdfFileReader constructor, if False
   PyPDF2 will NOT overwrite methods from Python's warnings.py module with
   a custom implementation.

 - Fix NumberObject and NameObject constructors for compatibility with PyPy
   (Rüdiger Jungbeck, Xavier Dupré, shezadkhan137, Steven Witham)

 - Utilize  utils.Str in pdf.py and pagerange.py to resolve type issues (by
   egbutter)

 - Improvements in implementing StringIO for Python 2 and BytesIO for
   Python 3 (by Xavier Dupré)

 - Added /x00 to Whitespaces, defined utils.WHITESPACES to clarify code (by
   Maxim Kamenkov)

 - Bugfix for merging 3 or more resources with the same name (by lucky-user)

 - Improvements to Xref parsing algorithm (by speedplane)


## Version 1.20, 2014-01-27

 - Official Python 3+ support (with contributions from TWAC and cgammans)
   Support for Python versions 2.6 and 2.7 will be maintained

 - Command line concatenation (see pdfcat in sample code) (by Steve Witham)

 - New FAQ; link included in README

 - Allow more (although unnecessary) escape sequences

 - Prevent exception when reading a null object in decoding parameters

 - Corrected error in reading destination types (added a slash since they
   are name objects)

 - Corrected TypeError in scaleTo() method

 - addBookmark() method in PdfFileMerger now returns bookmark (so nested
   bookmarks can be created)

 - Additions to Sample Code and Sample PDFs

 - changes to allow 2up script to work (see sample code) (by Dylan McNamee)

 - changes to metadata encoding (by Chris Hiestand)

 - New methods for links: addLink() (by Enrico Lambertini) and removeLinks()

 - Bugfix to handle nested bookmarks correctly (by Jamie Lentin)

 - New methods removeImages() and removeText() available for PdfFileWriter
   (by Tien Haï)

 - Exception handling for illegal characters in Name Objects


## Version 1.19, 2013-10-08

BUGFIXES:
 - Removed pop in sweepIndirectReferences to prevent infinite loop
   (provided by ian-su-sirca)

 - Fixed bug caused by whitespace when parsing PDFs generated by AutoCad

 - Fixed a bug caused by reading a 'null' ASCII value in a dictionary
   object (primarily in PDFs generated by AutoCad).

FEATURES:
 - Added new folders for PyPDF2 sample code and example PDFs; see README
   for each folder

 - Added a method for debugging purposes to show current location while
   parsing

 - Ability to create custom metadata (by jamma313)

 - Ability to access and customize document layout and view mode
   (by Joshua Arnott)

OTHER:
 - Added and corrected some documentation

 - Added some more warnings and exception messages

 - Removed old test/debugging code

UPCOMING:
 - More bugfixes (We have received many problematic PDFs via email, we
   will work with them)

 - Documentation - It's time for PyPDF2 to get its own documentation
   since it has grown much since the original pyPdf

 - A FAQ to answer common questions


## Version 1.18, 2013-08-19

 - Fixed a bug where older verions of objects were incorrectly added to the
   cache, resulting in outdated or missing pages, images, and other objects
   (from speedplane)

 - Fixed a bug in parsing the xref table where new xref values were
   overwritten; also cleaned up code (from speedplane)

 - New method mergeRotatedAroundPointPage which merges a page while rotating
   it around a point (from speedplane)

 - Updated Destination syntax to respect PDF 1.6 specifications (from
   jamma313)

 - Prevented infinite loop when a PdfFileReader object was instantiated
   with an empty file (from Jerome Nexedi)

Other Changes:

 - Downloads now available via PyPI
 - Installation through pip library is fixed


## Version 1.17, 2013-07-25

 - Removed one (from pdf.py) of the two Destination classes. Both
   classes had the same name, but were slightly different in content,
   causing some errors. (from Janne Vanhala)

 - Corrected and Expanded README file to demonstrate PdfFileMerger

 - Added filter for LZW encoded streams (from Michal Horejsek)

 - PyPDF2 issue tracker enabled on Github to allow community
   discussion and collaboration


## Versions -1.16, -2013-06-30

 - Note: This ChangeLog has not been kept up-to-date for a while.
   Hopefully we can keep better track of it from now on. Some of the
   changes listed here come from previous versions 1.14 and 1.15; they
   were only vaguely defined. With the new _version.py file we should
   have more structured and better documented versioning from now on.

 - Defined `PyPDF2.__version__`

 - Fixed encrypt() method (from Martijn The)

 - Improved error handling on PDFs with truncated streams (from cecilkorik)

 - Python 3 support (from kushal-kumaran)

 - Fixed example code in README (from Jeremy Bethmont)

 - Fixed an bug caused by DecimalError Exception (from Adam Morris)

 - Many other bug fixes and features by:

	jeansch
	Anton Vlasenko
	Joseph Walton
	Jan Oliver Oelerich
	Fabian Henze
	And any others I missed.
	Thanks for contributing!


## Version 1.13, 2010-12-04

 - Fixed a typo in code for reading a "\b" escape character in strings.

 - Improved `__repr__` in FloatObject.

 - Fixed a bug in reading octal escape sequences in strings.

 - Added getWidth and getHeight methods to the RectangleObject class.

 - Fixed compatibility warnings with Python 2.4 and 2.5.

 - Added addBlankPage and insertBlankPage methods on PdfFileWriter class.

 - Fixed a bug with circular references in page's object trees (typically
   annotations) that prevented correctly writing out a copy of those pages.

 - New merge page functions allow application of a transformation matrix.

 - To all patch contributors: I did a poor job of keeping this ChangeLog
   up-to-date for this release, so I am missing attributions here for any
   changes you submitted.  Sorry!  I'll do better in the future.


## Version 1.12, 2008-09-02

 - Added support for XMP metadata.

 - Fix reading files with xref streams with multiple /Index values.

 - Fix extracting content streams that use graphics operators longer than 2
   characters.  Affects merging PDF files.


## Version 1.11, 2008-05-09

 - Patch from Hartmut Goebel to permit RectangleObjects to accept NumberObject
   or FloatObject values.

 - PDF compatibility fixes.

 - Fix to read object xref stream in correct order.

 - Fix for comments inside content streams.


## Version 1.10, 2007-10-04

 - Text strings from PDF files are returned as Unicode string objects when
 pyPdf determines that they can be decoded (as UTF-16 strings, or as
 PDFDocEncoding strings).  Unicode objects are also written out when
 necessary.  This means that string objects in pyPdf can be either
 generic.ByteStringObject instances, or generic.TextStringObject instances.

 - The extractText method now returns a unicode string object.

 - All document information properties now return unicode string objects.  In
 the event that a document provides docinfo properties that are not decoded by
 pyPdf, the raw byte strings can be accessed with an "_raw" property (ie.
 title_raw rather than title)

 - generic.DictionaryObject instances have been enhanced to be easier to use.
 Values coming out of dictionary objects will automatically be de-referenced
 (.getObject will be called on them), unless accessed by the new "raw_get"
 method.  DictionaryObjects can now only contain PdfObject instances (as keys
 and values), making it easier to debug where non-PdfObject values (which
 cannot be written out) are entering dictionaries.

 - Support for reading named destinations and outlines in PDF files.  Original
 patch by Ashish Kulkarni.

 - Stream compatibility reading enhancements for malformed PDF files.

 - Cross reference table reading enhancements for malformed PDF files.

 - Encryption documentation.

 - Replace some "assert" statements with error raising.

 - Minor optimizations to FlateDecode algorithm increase speed when using PNG
 predictors.

## Version 1.9, 2006-12-15

 - Fix several serious bugs introduced in version 1.8, caused by a failure to
   run through our PDF test suite before releasing that version.

 - Fix bug in NullObject reading and writing.

## Version 1.8, 2006-12-14

 - Add support for decryption with the standard PDF security handler.  This
   allows for decrypting PDF files given the proper user or owner password.

 - Add support for encryption with the standard PDF security handler.

 - Add new pythondoc documentation.

 - Fix bug in ASCII85 decode that occurs when whitespace exists inside the
   two terminating characters of the stream.

## Version 1.7, 2006-12-10

 - Fix a bug when using a single page object in two PdfFileWriter objects.

 - Adjust PyPDF to be tolerant of whitespace characters that don't belong
   during a stream object.

 - Add documentInfo property to PdfFileReader.

 - Add numPages property to PdfFileReader.

 - Add pages property to PdfFileReader.

 - Add extractText function to PdfFileReader.


## Version 1.6, 2006-06-06

 - Add basic support for comments in PDF files.  This allows us to read some
   ReportLab PDFs that could not be read before.

 - Add "auto-repair" for finding xref table at slightly bad locations.

 - New StreamObject backend, cleaner and more powerful.  Allows the use of
   stream filters more easily, including compressed streams.

 - Add a graphics state push/pop around page merges.  Improves quality of
   page merges when one page's content stream leaves the graphics
   in an abnormal state.

 - Add PageObject.compressContentStreams function, which filters all content
   streams and compresses them.  This will reduce the size of PDF pages,
   especially after they could have been decompressed in a mergePage
   operation.

 - Support inline images in PDF content streams.

 - Add support for using .NET framework compression when zlib is not
   available.  This does not make pyPdf compatible with IronPython, but it
   is a first step.

 - Add support for reading the document information dictionary, and extracting
   title, author, subject, producer and creator tags.

 - Add patch to support NullObject and multiple xref streams, from Bradley
   Lawrence.


## Version 1.5, 2006-01-28

- Fix a bug where merging pages did not work in "no-rename" cases when the
  second page has an array of content streams.

- Remove some debugging output that should not have been present.


## Version 1.4, 2006-01-27

- Add capability to merge pages from multiple PDF files into a single page
  using the PageObject.mergePage function.  See example code (README or web
  site) for more information.

- Add ability to modify a page's MediaBox, CropBox, BleedBox, TrimBox, and
  ArtBox properties through PageObject.  See example code (README or web site)
  for more information.

- Refactor pdf.py into multiple files: generic.py (contains objects like
  NameObject, DictionaryObject), filters.py (contains filter code),
  utils.py (various).  This does not affect importing PdfFileReader
  or PdfFileWriter.

- Add new decoding functions for standard PDF filters ASCIIHexDecode and
  ASCII85Decode.

- Change url and download_url to refer to new pybrary.net web site.


## Version 1.3, 2006-01-23

- Fix new bug introduced in 1.2 where PDF files with \r line endings did not
  work properly anymore.  A new test suite developed with various PDF files
  should prevent regression bugs from now on.

- Fix a bug where inheriting attributes from page nodes did not work.


## Version 1.2, 2006-01-23

- Improved support for files with CRLF-based line endings, fixing a common
  reported problem stating "assertion error: assert line == "%%EOF"".

- Software author/maintainer is now officially a proud married person, which
  is sure to result in better software... somehow.


## Version 1.1, 2006-01-18

- Add capability to rotate pages.

- Improved PDF reading support to properly manage inherited attributes from
  /Type=/Pages nodes.  This means that page groups that are rotated or have
  different media boxes or whatever will now work properly.

- Added PDF 1.5 support.  Namely cross-reference streams and object streams.
  This release can mangle Adobe's PDFReference16.pdf successfully.


## Version 1.0, 2006-01-17

- First distutils-capable true public release.  Supports a wide variety of PDF
  files that I found sitting around on my system.

- Does not support some PDF 1.5 features, such as object streams,
  cross-reference streams.
