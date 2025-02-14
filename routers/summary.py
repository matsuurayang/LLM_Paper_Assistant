from fastapi import APIRouter, HTTPException
from services.summarizer import generate_summary
from pydantic import BaseModel

router = APIRouter()

# 请求体格式化
class Paper(BaseModel):
    text: str

@router.post("/summarize")
async def summarize_paper(paper: Paper):
    try:
        # 生成摘要
        summary = generate_summary(paper.text)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
