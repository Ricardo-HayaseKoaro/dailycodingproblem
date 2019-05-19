
def encode(s):
    curr_char = s[0]
    count = 0
    coded = []
    for c in s:
        if curr_char == c:
            count += 1
        else:
            coded.append(str(count))
            coded.append(curr_char)
            curr_char = c
            count = 1  # start at 1 because its count the first appearance of the char
    coded.append(str(count))
    coded.append(curr_char)
    return ''.join(coded)


def decode(s):
    count = 0
    result = ''
    for char in s:
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            # char is alphabetic
            result += char * count
            count = 0
    return result


test = "AAAABBBCCDAA"
code = encode(test)
print(code)
decode_test = decode(code)
print(decode_test)
print(test)