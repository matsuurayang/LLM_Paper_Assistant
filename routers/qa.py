from fastapi import APIRouter, HTTPException
from services.qa_system import answer_question
from pydantic import BaseModel

router = APIRouter()

# 请求体格式化
class QuestionRequest(BaseModel):
    text: str
    question: str

@router.post("/answer")
async def answer_question_from_paper(request: QuestionRequest):
    try:
        # 生成答案
        answer = answer_question(request.text, request.question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
