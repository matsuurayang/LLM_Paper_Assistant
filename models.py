from transformers import pipeline

# 加载 T5-Small 作为摘要生成模型
def load_summarization_model():
    model_name = "t5-small"
    summarizer = pipeline("summarization", model=model_name)
    return summarizer

# 加载问答模型
def load_qa_model():
    model_name = "deepset/roberta-base-squad2"
    qa_pipeline = pipeline("question-answering", model=model_name)
    return qa_pipeline

summarizer = load_summarization_model()
qa_pipeline = load_qa_model()
