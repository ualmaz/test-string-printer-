import re

pattern = r'\d+'
sentence = "12 ай, 12 жыл 12 үй 12 киши"
res = re.findall(pattern, sentence)
print(res)
