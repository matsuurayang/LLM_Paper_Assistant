from models import get_model, get_tokenizer

# 获取模型和分词器
model = get_model()
tokenizer = get_tokenizer()


def format_text_for_code_extraction(text: str) -> str:
    """ 格式化输入文本，提取文本中的代码片段 """
    # 提取代码块的正则表达式，可以根据实际情况调整
    code_blocks = []
    lines = text.split('\n')

    in_code_block = False
    code_block = []

    for line in lines:
        # 假设代码块以 4 个空格开头
        if line.startswith('    '):  # 检测缩进
            if not in_code_block:
                in_code_block = True
            code_block.append(line.strip())
        else:
            if in_code_block:
                code_blocks.append('\n'.join(code_block))
                in_code_block = False
                code_block = []

    # 如果最后一个块是代码，也要加上
    if in_code_block:
        code_blocks.append('\n'.join(code_block))

    # 格式化为 T5 输入要求
    return "extract code: " + '\n'.join(code_blocks)


def extract_code(text: str) -> str:
    """ 提取文档中的代码 """
    formatted_text = format_text_for_code_extraction(text)

    # 编码输入文本并生成输出
    inputs = tokenizer(formatted_text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(**inputs, max_length=512)

    # 解码模型输出并返回结果
    code = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return code
