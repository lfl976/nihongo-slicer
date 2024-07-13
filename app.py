import MeCab

def tokenize_japanese(text):
    mecab = MeCab.Tagger("-Owakati")
    mecab.parse("")  # 清除内部状态
    node = mecab.parseToNode(text)
    tokens = []
    print(node)
    while node:
        if node.surface != "":
            # 获取词元的表面形式（即原始文本）
            token = node.surface
            # 获取词元的词性信息
            print(node.feature)
            pos = node.feature.split(",")[0]
            # 获取假名信息
            reading = node.feature.split(",")[8]
            tokens.append((token, pos, reading))
        node = node.next
    return tokens

# 示例文本
text = "明日は晴れるかもしれない。"

# 分词
tokens = tokenize_japanese(text)
for token in tokens:
    print(token)
