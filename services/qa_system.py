from models import get_model, get_tokenizer

# 获取模型和分词器
model = get_model()
tokenizer = get_tokenizer()


def format_text_for_qa(text: str, question: str) -> str:
    """ 格式化输入文本以适应问答模型 """
    formatted_text = f"question: {text}\n{question}"
    return formatted_text


def answer_question(text: str, question: str) -> str:
    """ 基于文档内容和问题生成答案 """
    formatted_text = format_text_for_qa(text, question)

    # 编码输入文本并生成输出
    inputs = tokenizer(formatted_text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(**inputs, max_length=512)

    # 解码模型输出并返回结果
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer
