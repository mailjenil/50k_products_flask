"""
This class is responsible for all data structures related to Trie
"""
import enum


class CoreNode:
    def __init__(self):
        self.child_nodes = {}
        self.last_node = False


class ProductTrie:
    def __init__(self):
        self.root = CoreNode()
        self.entities = []

    def form_product_trie(self, keys):
        for key in keys:
            self.insert(key)

    def insert(self, entities):
        current_node = self.root

        for entity in list(entities):
            if not current_node.child_nodes.get(entity):
                current_node.child_nodes[entity] = CoreNode()
            current_node = current_node.child_nodes[entity]
        current_node.last_node = True

    def search(self, entities):
        current_node = self.root
        found = True

        for entitiy in list(entities):
            if not current_node.child_nodes.get(entitiy):
                found = False
                break
            current_node = current_node.child_nodes[entitiy]
        return current_node and current_node.last_node and found

    def suggestions_rec(self, current_node, word):
        if current_node.last_node:
            self.entities.append(word)

        for entity, number in current_node.child_nodes.items():
            self.suggestions_rec(number, word + entity)

    def get_auto_completions(self, key):
        last_node = self.root
        not_found = False
        temp_word = ''

        for a in list(key):
            if not last_node.child_nodes.get(a):
                not_found = True
                break

            temp_word += a
            last_node = last_node.child_nodes[a]

        if not_found:
            return TrieStatus.not_found
        elif last_node.last_node and not last_node.child_nodes:
            return TrieStatus.others_not_found

        self.suggestions_rec(last_node, temp_word)
        return self.entities


class TrieStatus(enum.Enum):
    not_found = 2
    others_not_found = 3
