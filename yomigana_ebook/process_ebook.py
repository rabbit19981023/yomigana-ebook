from warnings import filterwarnings
from typing import IO
from zipfile import ZipFile, ZIP_DEFLATED

from bs4 import BeautifulSoup, NavigableString, Tag, XMLParsedAsHTMLWarning
from yomigana_ebook.yomituki import yomituki_sentence


filterwarnings("ignore", category=XMLParsedAsHTMLWarning, module="bs4")


def process_ebook(reader: IO[bytes], writer: IO[bytes]):
    with (
        ZipFile(reader, "r") as zip_reader,
        ZipFile(writer, "w", ZIP_DEFLATED) as zip_writer,
    ):
        for file in zip_reader.namelist():
            with zip_reader.open(file) as file_reader:
                if file.endswith(("xhtml", "html")):
                    soup = BeautifulSoup(file_reader.read(), "lxml")

                    for child in soup.children:
                        process_tag(child)  # type: ignore

                    zip_writer.writestr(file, soup.encode(formatter=None))  # type: ignore

                else:
                    zip_writer.writestr(file, file_reader.read())


def process_tag(tag: Tag):
    if tag.name == "ruby":
        return

    if type(tag) is NavigableString:
        tag.replace_with("".join(yomituki_sentence(tag)))
        return

    if hasattr(tag, "children"):
        for child in tag.children:
            process_tag(child)  # type: ignore
