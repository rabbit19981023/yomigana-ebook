import "./style.css";

const loader = <HTMLDivElement>document.querySelector(".loader");
const dropContainer = <HTMLLabelElement>document.querySelector(".drop-container");
const fileInput = <HTMLInputElement>document.querySelector(".input-file");
const submitBtn = <HTMLButtonElement>document.querySelector(".btn-submit");

submitBtn.addEventListener("click", async _event => {
    const files = fileInput.files;

    enableLoader();

    for (const file of files!) {
        const formData = new FormData();
        formData.append("ebook", file);

        const response = await fetch("/api/process-ebook", { method: "POST", body: formData });
        const blobUrl = URL.createObjectURL(await response.blob());

        const link = document.createElement("a");
        link.href = blobUrl;
        link.download = `with-yomigana_${file.name}`;
        link.click();

        link.remove();
    }

    disableLoader();
});

dropContainer.addEventListener("drop", event => {
    event.preventDefault();
    dropContainer.style.backgroundColor = "transparent";
    fileInput.files = event.dataTransfer!.files;
});

dropContainer.addEventListener("dragover", event => {
    event.preventDefault();
    dropContainer.style.backgroundColor = "#fff";
});

dropContainer.addEventListener("dragleave", _event => {
    dropContainer.style.backgroundColor = "transparent";
});

function enableLoader() {
    loader.classList.toggle("enable");
}

function disableLoader() {
    loader.classList.toggle("enable");
}
