# this doesnt work
def sentence(words_set, strr):
    result = []
    i = 0
    while len(strr) > 1:
        if strr[:i] in words_set:
            result.append(strr[:i])
            strr = strr[i:]
            i = 0
        else:
            i += 1
    return result


# this one works 0(2^n)
def sentence2(words_set, strr):
    if len(strr) == 0:
        return [], True

    for i in range(len(strr) + 1):
        if strr[:i] in words_set:
            aux, valid = sentence2(words_set, strr[i:])
            if valid: # if suffix is valid
                return [strr[:i]] + aux, True

    # if dont find any word in words_set the sufix is not valid
    return [], False


test1 = "theremin"
words1 = set()
words1.add("the")
words1.add("theremin")
print(sentence2(words1, test1))


test = "thequickbrownfox"
words = set()
words.add("quick")
words.add("brown")
words.add("the")
words.add("fox")
print(sentence2(words, test))

