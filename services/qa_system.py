from models import qa_pipeline

def answer_question(context: str, question: str) -> str:
    """根据上下文回答问题"""
    answer = qa_pipeline(question=question, context=context)
    return answer['answer']
