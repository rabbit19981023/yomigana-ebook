# yomigana ebook

This project is aimed at making Japanese eBooks more friendly to those who are learning Japanese now by adding readings for every Kanji in the eBooks.

To achieve this, the project utilizes Mecab, a Japanese morphological analyzer, and Unidic, a dictionary developed by NICT, to tokenize words and obtain the corresponding yomigana (reading) of each word. This information is then inserted above or besides the kanji characters in the eBook text, allowing readers to easily read and understand the pronunciation of each word.

## Usage

you can install the package via `pip`:

`$ pip install yomigana-ebook`

then download the `unidic` dictionary:

`$ python -m unidic download`

now you can use it:

`$ yomigana_ebook <your-ebooks>`

or just clone the repo to use it:

```bash
$ git clone https://github.com/rabbit19981023/yomigana-ebook.git
$ pip install .
$ python -m unidic download
$ yomigana_ebook <your-ebooks>
```
