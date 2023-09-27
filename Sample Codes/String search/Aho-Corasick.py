
'''a complex multi-pattern string matching algorithm.'''

# to find which indexes
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.failure_link = None
        self.output_link = None
        self.patterns = []


class AhoCorasick:
    def __init__(self):
        self.root = TrieNode()

    def add_pattern(self, pattern):
        node = self.root
        for char in pattern:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.patterns.append(pattern)

    def build_failure_links(self):
        queue = []
        for child in self.root.children.values():
            queue.append(child)
            child.failure_link = self.root

        while queue:
            node = queue.pop(0)
            for char, child in node.children.items():
                queue.append(child)
                failure = node.failure_link
                while failure and char not in failure.children:
                    failure = failure.failure_link
                child.failure_link = failure.children[char] if failure else self.root
                child.output_link = child.failure_link if child.failure_link.is_end_of_word else child.failure_link.output_link

    def search_patterns(self, text):
        node = self.root
        patterns_found = []

        for i, char in enumerate(text):
            while node and char not in node.children:
                node = node.failure_link
            if not node:
                node = self.root
                continue
            node = node.children[char]
            if node.is_end_of_word:
                for pattern in node.patterns:
                    patterns_found.append((i - len(pattern) + 1, i, pattern))

            output_node = node.output_link
            while output_node:
                for pattern in output_node.patterns:
                    patterns_found.append((i - len(pattern) + 1, i, pattern))
                output_node = output_node.output_link

        return patterns_found

# Example usage:
patterns = ["he", "she", "his", "hers"]
text = "ushershe"
aho_corasick = AhoCorasick()

for pattern in patterns:
    aho_corasick.add_pattern(pattern)

aho_corasick.build_failure_links()
results = aho_corasick.search_patterns(text)

for start, end, pattern in results:
    print(f"Pattern '{pattern}' found from index {start} to {end}: {text[start:end+1]}")


# to get each count
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.failure_link = None
        self.output_link = None
        self.patterns = {}
        

class AhoCorasick:
    def __init__(self):
        self.root = TrieNode()

    def add_pattern(self, pattern):
        node = self.root
        for char in pattern:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        if pattern in node.patterns:
            node.patterns[pattern] += 1
        else:
            node.patterns[pattern] = 1

    def build_failure_links(self):
        queue = []
        for child in self.root.children.values():
            queue.append(child)
            child.failure_link = self.root

        while queue:
            node = queue.pop(0)
            for char, child in node.children.items():
                queue.append(child)
                failure = node.failure_link
                while failure and char not in failure.children:
                    failure = failure.failure_link
                child.failure_link = failure.children[char] if failure else self.root
                child.output_link = child.failure_link if child.failure_link.is_end_of_word else child.failure_link.output_link

    def search_patterns(self, text):
        node = self.root
        patterns_found = {}

        for i, char in enumerate(text):
            while node and char not in node.children:
                node = node.failure_link
            if not node:
                node = self.root
                continue
            node = node.children[char]
            if node.is_end_of_word:
                for pattern, count in node.patterns.items():
                    if pattern in patterns_found:
                        patterns_found[pattern] += count
                    else:
                        patterns_found[pattern] = count

            output_node = node.output_link
            while output_node:
                for pattern, count in output_node.patterns.items():
                    if pattern in patterns_found:
                        patterns_found[pattern] += count
                    else:
                        patterns_found[pattern] = count
                output_node = output_node.output_link

        return patterns_found

# Example usage:
patterns = ["he", "she", "his", "hers"]
text = "ushershehe"
aho_corasick = AhoCorasick()

for pattern in patterns:
    aho_corasick.add_pattern(pattern)

aho_corasick.build_failure_links()
results = aho_corasick.search_patterns(text)

for pattern, count in results.items():
    print(f"Pattern '{pattern}' found {count} times.")
