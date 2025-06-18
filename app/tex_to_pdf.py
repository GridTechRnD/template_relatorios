import os
import base64
import shutil
import tempfile
import subprocess


def tex_to_pdf(tex: str, enterprise_logo: str, **kwargs) -> None:
    if not shutil.which("xelatex"):
        raise ModuleNotFoundError(
            'Module "xelatex" not found in OS! Please install texlive-xetex and try again.'
        )

    temp_images: list[str] = []
    with tempfile.TemporaryDirectory() as tmpdir:
        for i, image in enumerate(kwargs["images"]):
            temp_image = os.path.join(tmpdir, f"temp_image{i+1}.png")
            temp_images.append(temp_image)
            with open(temp_image, "wb") as file:
                file.write(base64.b64decode(image))

        tex_path = os.path.join(tmpdir, "temp.tex")
        tex = tex.format(
            **kwargs,
            **{f"temp_image{i+1}": image for i, image in enumerate(temp_images)},
            enterprise_logo=enterprise_logo,
            hexing_logo="/media/hexing.png",
        )

        with open(tex_path, "w", encoding="utf-8") as f:
            f.write(tex)
        try:
            subprocess.run(
                ["xelatex", "-interaction=nonstopmode", tex_path], cwd=tmpdir
            )
            pdf_path = os.path.join(tmpdir, "temp.pdf")
            if os.path.exists(pdf_path):
                shutil.move(pdf_path, "/media/temp.pdf")

        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Erro ao compilar o LaTeX: {e}") from e
