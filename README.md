# yomigana ebook

This project is aimed at making Japanese eBooks more friendly to those who are learning Japanese now by adding readings for every Kanji in the eBooks.

To achieve this, the project utilizes Mecab, a Japanese morphological analyzer, and Unidic, a dictionary developed by NICT, to tokenize words and obtain the corresponding yomigana (reading) of each word. This information is then inserted above or besides the kanji characters in the eBook text, allowing readers to easily read and understand the pronunciation of each word.

> This tool is also the fastest converter now. (compared to [Mumumu4/furigana4epub](https://github.com/Mumumu4/furigana4epub) & [itsupera/furiganalyse](https://github.com/itsupera/furiganalyse))

## Usage

1. install the package from `PyPI`:

    ```
    # install the package
    $ pip install yomigana-ebook

    # download the unidic dictionary
    $ python -m unidic download

    # you can convert your japanese ebooks now!
    $ yomigana_ebook [your-ebooks]
    ```

2. build from the source:

    ```
    $ git clone https://github.com/rabbit19981023/yomigana-ebook.git

    # install the project
    $ pip install ./yomigana-ebook

    # download the unidic dictionary
    $ python -m unidic download

    # you can convert your japanese ebooks now!
    $ yomigana_ebook [your-ebooks]
    ```

### For Windows Users

There's a known bug in Windows, see polm/fugashi#42 for more information

To solve it, you must install & use the package in an isolated `virtualenv`:

Here are some examples:

1. install the package from `PyPI`:

    ```
    # create the virtualenv
    $ python -m venv .venv

    # get into the virtualenv
    $ .venv\Scripts\activate

    # install the package
    $ pip install yomigana-ebook

    # download the unidic dictionary
    $ python -m unidic download

    # you can convert your japanese ebooks now!
    $ yomigana_ebook [your-ebooks]
    ```

2. build from source:

    ```
    $ git clone https://github.com/rabbit19981023/yomigana-ebook.git

    $ cd yomigana-ebook

    # create the virtualenv
    $ python -m venv .venv

    # get into the virtualenv
    $ .venv\Scripts\activate

    # install the project
    $ pip install .

    # download the unidic dictionary
    $ python -m unidic download

    # you can convert your japanese ebooks now!
    $ yomigana_ebook [your-ebooks]
    ```

To leave the `virtualenv`, just by a simple command:

```
$ deactivate
```

### Run the web demo via Docker

> NOTE: you NEED to run these commands in the project root, NOT in `web-demo` directory!

1. first we need to build the image:

    ```
    $ docker build -t yomigana-ebook/web-demo -f Dockerfile.web-demo .
    ```

2. then run the container:

    ```
    $ docker run --rm -p 8000:8000 yomigana-ebook/web-demo --host 0.0.0.0
    ```

3. finally just open your browser and navigate to `http://localhost:8000` to use it!

## Credits

This project was inspired by [Mumumu4/furigana4epub](https://github.com/Mumumu4/furigana4epub) & [itsupera/furiganalyse](https://github.com/itsupera/furiganalyse), and has some code from them.
