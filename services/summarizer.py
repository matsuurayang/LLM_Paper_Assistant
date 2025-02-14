from models import get_model, get_tokenizer

# 获取模型和分词器
model = get_model()
tokenizer = get_tokenizer()


def format_text_for_summary(text: str) -> str:
    """ 格式化文本，使其适合摘要生成 """
    formatted_text = f"summarize: {text}"
    return formatted_text


def generate_summary(text: str) -> str:
    """ 基于论文内容生成摘要 """
    formatted_text = format_text_for_summary(text)

    # 编码输入文本并生成输出
    inputs = tokenizer(formatted_text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(**inputs, max_length=512)

    # 解码模型输出并返回结果
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return summary
