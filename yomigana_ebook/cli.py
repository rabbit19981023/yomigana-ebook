from typing import List
from argparse import ArgumentParser
from os import path
from time import time

from yomigana_ebook.process_ebook import process_ebook


def main():
    parser = ArgumentParser(
        description="The fastest converter to add yomigana(readings) to Japanese epub eBooks! (Using Mecab and Unidic)"
    )
    parser.add_argument("ebook_paths", type=str, nargs="*")
    args = parser.parse_args()

    if args.ebook_paths:
        process_ebooks(args.ebook_paths)
        exit(0)

    parser.print_help()


def process_ebooks(arg_paths: List[str]):
    for arg_path in arg_paths:
        file_path = path.abspath(arg_path)
        file_dir = path.dirname(file_path)
        file_name = path.basename(file_path)
        output_path = path.join(file_dir, f"with-yomigana_{file_name}")

        with open(file_path, "rb") as f_reader, open(output_path, "wb") as f_writer:
            start_time = time()
            print()
            print(f"[start] parsing the ebook: {file_path}")

            process_ebook(f_reader, f_writer)

            end_time = time() - start_time
            print(f"[done]  here's the parsed ebook: {output_path}")
            print(f"this ebook takes {end_time} secs to process.")
            print()


if __name__ == "__main__":
    main()
