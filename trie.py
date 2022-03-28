class Trie:
    def __init__(self):
        self.root = {}

    def add(self, word):
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node['_end_'] = True

    def find(self, word):
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return '_end_' in node

    def find_prefix(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True

    def _get_words(self, node):
        words = []
        if '_end_' in node:
            words.append('')
        
        for c in node:
            if c != '_end_':
                for word in self._get_words(node[c]):
                    words.append(c + word)
        return words

    def auto_complete(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node:
                return []
            node = node[c]
        return self._get_words(node)

trie = Trie()
trie.add('apple')
trie.add('apples')
trie.add('app')
trie.add('map')
trie.add('thadeu')
trie.add('amazon')
trie.add('amzing')

print(trie.find('apple'))
print(trie.find('apples'))
print(trie.find('app'))
print(trie.auto_complete('appl'))
print(trie.auto_complete('a'))
from collections import Counter
l = ['rose','tulips','sunflowers','tulips','rose']
my_count = Counter(l)
print(my_count)