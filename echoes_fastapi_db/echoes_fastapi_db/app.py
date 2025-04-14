from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from .db import SessionLocal, Upload
import shutil
import os

app = FastAPI()

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...), label: str = Form(...)):
    file_path = f"images/uploads/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    db = SessionLocal()
    upload = Upload(filename=file.filename, label=label)
    db.add(upload)
    db.commit()
    db.close()

    return JSONResponse(content={"message": "Image uploaded successfully", "filename": file.filename, "label": label})