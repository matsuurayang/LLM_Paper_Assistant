# routers/paper.py

from fastapi import APIRouter, File, UploadFile, HTTPException
from io import BytesIO
from services.paper_parser import parse_pdf  # 引入自定义的解析函数

router = APIRouter()

# 用于接收上传的文件和解析内容
class Paper(BaseModel):
    text: str

# 上传并提取 PDF 文本
@router.post("/upload")
async def upload_paper(file: UploadFile = File(...)):
    try:
        # 读取上传的文件
        contents = await file.read()

        # 使用 paper_parser 提取文本
        text = parse_pdf(contents)

        return {"text": text}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing the file: {str(e)}")
