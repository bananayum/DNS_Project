import sys
def match_chars(char):
    if char == "(":
        return ")"
    elif char == "[":
        return "]"
    else:
        return "}"

def handle(strings):
    struct_info = []
    # 存储数字位置，数字数值，符号
    for i in range(0,len(strings)):
        if strings[i].isdigit():
            struct_info.append([i,int(strings[i]),strings[i+1]])
    new_strings = ""
    # 从最内层的括号开始去除
    for struct in struct_info[::-1]:
        # 确定括号内的内容的起始和结束位置
        start = struct[0] + 2
        end = start + strings[start:].index(match_chars(struct[2]))
        new_strings = ""
        new_strings = new_strings + strings[:struct[0]]
        for k in range(0,struct[1]):
            new_strings = new_strings + strings[start:end]

        new_strings = new_strings + strings[end+1:]
        # 为了循环删去括号，把新值覆盖到旧值
        strings = new_strings

    return new_strings


line = sys.stdin.readline().strip()
result = handle(line)
print(result[::-1])
