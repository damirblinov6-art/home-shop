from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI(title="Домашний Уют API")

# Получаем абсолютный путь к папке с файлами
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Главная страница
@app.get("/")
async def root():
    return FileResponse(os.path.join(BASE_DIR, "index.html"))

# Админ-панель
@app.get("/admin")
async def admin():
    return FileResponse(os.path.join(BASE_DIR, "admin.html"))

# Дублируем для прямого доступа
@app.get("/admin.html")
async def admin_html():
    return FileResponse(os.path.join(BASE_DIR, "admin.html"))

# Раздача статических файлов (CSS, JS, картинки)
@app.get("/{filename}")
async def static_files(filename: str):
    file_path = os.path.join(BASE_DIR, filename)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return FileResponse(file_path)
    return {"error": "File not found"}

# Health check для Render
@app.get("/health")
async def health():
    return {"status": "ok", "service": "Домашний Уют"}
