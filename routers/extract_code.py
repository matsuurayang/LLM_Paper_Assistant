from fastapi import APIRouter, HTTPException
from services.code_extractor import extract_code
from pydantic import BaseModel

router = APIRouter()

# 请求体格式化
class Paper(BaseModel):
    text: str

@router.post("/extract_code")
async def extract_code_from_paper(paper: Paper):
    try:
        # 提取代码
        extracted_code = extract_code(paper.text)
        if not extracted_code:
            raise HTTPException(status_code=404, detail="No code found in the document")
        return {"extracted_code": extracted_code}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
