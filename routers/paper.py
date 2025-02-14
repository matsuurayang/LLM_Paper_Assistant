from fastapi import APIRouter, File, UploadFile, HTTPException
from io import StringIO
from pydantic import BaseModel
import textract

router = APIRouter()


# 用于接收上传的文件和解析内容
class Paper(BaseModel):
    text: str


# 上传文件并提取文本
@router.post("/upload")
async def upload_paper(file: UploadFile = File(...)):
    try:
        contents = await file.read()

        # 使用 textract 提取文本
        text = textract.process(docx=contents).decode("utf-8")

        return {"text": text}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing the file: {str(e)}")
