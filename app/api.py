import io
import os
import base64
from fastapi import FastAPI
from fastapi.responses import FileResponse
from template import HTML
from model import Model
from PIL import Image
from fpdf import FPDF
from playwright.async_api import async_playwright


app = FastAPI(name="Gerador de relatório", version="1.0.0",
              root_path="/html2pdf", swagger_ui_parameters={"syntaxHighlight": True})


async def html_pdf(html_string, pdf_path, img_path):
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=['--no-sandbox'])
        page = await browser.new_page(
            viewport={"width": 794, "height": 1123},
            device_scale_factor=5
        )
        await page.set_content(html_string)
        page.wait_for_load_state('networkidle')
        await page.evaluate("document.fonts.ready")
        screenshot_bytes = await page.screenshot(full_page=True)
        await browser.close()

    image = Image.open(io.BytesIO(screenshot_bytes))
    image_rgb = image.convert('RGB')
    image_rgb.save(img_path)

    pdf = FPDF(unit="pt", format=[image.width, image.height])
    pdf.add_page()
    pdf.image(img_path, 0, 0, image.width, image.height)
    pdf.output(pdf_path)

    os.remove(img_path)

    return


@app.post("/build")
async def build(item: Model):
    item = item.model_dump()
    for i in item["images"]:
        if isinstance(i, str):
            try:
                base64.b64decode(i)
            except Exception:
                raise Exception("The blob is not a base64 string")
    
    item["enterprise_logo"] = f'<img src="data:image/png;base64, {item["enterprise_logo"]}" width="84" height="34"/>'
    item["images"] = '\n'.join([f'<img src="data:image/png;base64, {i}" />' for i in item["images"]])
    html = HTML.format(**item)
    pdf_path = "/media/temp.pdf"
    img_path = "/media/temp_image.jpg"
    await html_pdf(html, pdf_path, img_path)

    response = FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename="documento.pdf"
    )

    from fastapi import BackgroundTasks

    def cleanup():
        os.remove(pdf_path)
    response.background = BackgroundTasks()
    response.background.add_task(cleanup)

    return response
