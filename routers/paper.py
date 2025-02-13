from fastapi import APIRouter, UploadFile, File
from services.paper_parser import extract_text_from_pdf
import uuid

router = APIRouter()

@router.post("/upload")
async def upload_paper(file: UploadFile = File(...)):
    paper_id = str(uuid.uuid4())
    file_path = f"./uploaded_papers/{paper_id}.pdf"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    extracted_text = extract_text_from_pdf(file_path)
    return {"paper_id": paper_id, "status": "processed", "extracted_text": extracted_text[:500]}
