# Web Demo

This is a web demo for the `yomigana-ebook` package.

## Usage

To use it, you can follow the steps below:

1. install the dependencies and download the `unidic` dictionary:

```bash
$ pip install .
$ python -m unidic download
```

2. build the client:

```bash
$ cd client
$ npm install
$ npm run build
```

3. go back to `web-demo` directory (the `web-demo` project root) and run the web service:

```bash
$ cd ..
$ uvicorn web_demo.main:app
```

4. finally, just open your browser and navigate to `http://localhost:8000` to use it!

### Run the web demo via Docker

please see [Project README](../README.md#run-the-web-demo-via-docker)
