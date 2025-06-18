import base64
import logging
import os

from fastapi import BackgroundTasks, FastAPI, Path
from fastapi.responses import FileResponse
from model import CelescModel, CpflHXAPModel, CpflRelayModel
from templates import CELESC_TEX, CPFL_HXAP_TEX, CPFL_RELAY_TEX
from tex_to_pdf import tex_to_pdf

logger = logging.getLogger(__name__)

app = FastAPI(
    name="Gerador de relatório",
    version="1.0.1",
    root_path="/tex2pdf",
    swagger_ui_parameters={"syntaxHighlight": True},
)

templates = {
    "celesc": [CELESC_TEX, "/media/celesc.png"],
    "cpfl_hxap": [CPFL_HXAP_TEX, "/media/cpfl.png"],
    "cpfl_relay": [CPFL_RELAY_TEX, "/media/cpfl.png"],
}


@app.post("/build/{template}")
async def build(
    template: str = Path(..., description="Nome do template"),
    item: CelescModel | CpflHXAPModel | CpflRelayModel = None,
):
    item = item.model_dump()
    images = []
    for i in item["images"]:
        if isinstance(i, str):
            try:
                base64.b64decode(i)
                images.append(i)
            except Exception:
                logger.warning("The blob is not a base64 string %s", i)

    if template not in templates:
        return {"error": "Template not found"}

    tex, enterprise_logo = templates.get(template, (None, None))

    pdf_path = "/media/temp.pdf"
    tex_to_pdf(tex=tex, enterprise_logo=enterprise_logo, **item)

    response = FileResponse(
        pdf_path, media_type="application/pdf", filename="documento.pdf"
    )

    def cleanup():
        os.remove(pdf_path)

    response.background = BackgroundTasks()
    response.background.add_task(cleanup)

    return response
