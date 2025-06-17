from model import CelescModel, CPFLModel
from templates import CPFL_TEX, CELESC_TEX
from tex_to_pdf import tex_to_pdf
from fastapi import FastAPI
from fastapi.responses import FileResponse
import base64
import logging
import os

logger = logging.getLogger(__name__)

app = FastAPI(
    name="Gerador de relatório",
    version="1.0.1",
    root_path="/tex2pdf",
    swagger_ui_parameters={"syntaxHighlight": True},
)


@app.post("/build")
async def build(item: CelescModel | CPFLModel):
    item = item.model_dump()
    images = []
    for i in item["images"]:
        if isinstance(i, str):
            try:
                base64.b64decode(i)
                images.append(i)
            except Exception:
                logger.warning("The blob is not a base64 string %s", i)

    template = {
        "celesc": [CELESC_TEX, "/media/celesc.png"],
        "cpfl": [CPFL_TEX, "/media/cpfl.png"]
    }
    tex, enterprise_logo = template.get(item["enterprise_logo"], (None, None))

    item.pop("enterprise_logo")
    pdf_path = "/media/temp.pdf"
    tex_to_pdf(tex=tex, enterprise_logo=enterprise_logo, **item)

    response = FileResponse(
        pdf_path, media_type="application/pdf", filename="documento.pdf"
    )

    from fastapi import BackgroundTasks

    def cleanup():
        os.remove(pdf_path)

    response.background = BackgroundTasks()
    response.background.add_task(cleanup)

    return response
