from fastapi import FastAPI, Response
import subprocess
from contextlib import asynccontextmanager
from pathlib import Path


@asynccontextmanager
async def lifespan(app: FastAPI):
    process = subprocess.Popen(["python3", "./src/watch.py"])
    yield
    process.terminate()

app = FastAPI(lifespan=lifespan)

# 定义一个路由来查看图表


@app.get("/view-chart")
async def view_chart():
    process = subprocess.Popen(["python3", "./src/plt.py"])
    process.wait()

    IMAGE_PATH = Path("static/result.png")
    if not IMAGE_PATH.is_file():
        return Response(content="Image not found", media_type="text/plain")
    with open(IMAGE_PATH, "rb") as img_file:
        img_data = img_file.read()
    return Response(content=img_data, media_type="image/png")
