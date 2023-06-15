import asyncio

from typing import Annotated
from io import BytesIO

from fastapi import FastAPI, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, StreamingResponse

from yomigana_ebook.process_ebook import process_ebook


app = FastAPI()

app.mount("/assets", StaticFiles(directory="client/dist/assets"), "assets")


@app.get("/")
async def index():
    return FileResponse("client/dist/index.html")


@app.get("/favicon.ico")
async def get_favicon():
    return FileResponse("client/dist/favicon.ico")


@app.post("/api/process-ebook")
async def process_ebook_handler(ebook: Annotated[bytes, File()]):
    return StreamingResponse(process_ebook_streamer(ebook))


async def process_ebook_streamer(ebook: bytes):
    with BytesIO(ebook) as reader, BytesIO() as writer:
        await asyncio.to_thread(process_ebook, reader, writer)
        yield writer.getbuffer().tobytes()
