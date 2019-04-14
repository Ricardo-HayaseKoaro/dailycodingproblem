END = '__ENDS_HERE'


class Trie(object):

    def __init__(self):
        self.trie = {}

    def insert(self, text):
        aux = self.trie
        for char in text:
            if char not in aux:
                aux[char] = {}
            aux = aux[char]
        aux[END] = True

    # search for nodes with same prefix(str)
    def search(self, str):
        aux = self.trie
        for char in str:
            if char in aux:
                aux = aux[char]
            else:
                return []
        return self.word(aux)

    # aux comes with all words that have the prefix, now we need to save the worlds in array
    def word(self, aux):
        result = []
        for c, v in aux.items():
            if c == END:  # separate words
                subresult = ['']
            else:
                subresult = [c + s for s in self.word(v)]
            result.extend(subresult)
        return result


# first version without using trie
def auto_complete(str, array):
    k = len(str)
    result = []
    for word in array:
        if(word[:k] == str):
            result.append(word)
    print(result)


str = 'de'
array = ['dog', 'deer', 'deal']
# auto_complete(str, array)

trie = Trie()
for word in array:
    trie.insert(word)


def autocomplete(s):
    suffixes = trie.search(s)
    return [s + w for w in suffixes]


print(autocomplete(str))