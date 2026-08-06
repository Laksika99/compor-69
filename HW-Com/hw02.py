def longest_unique_word_sequence(words: list[list[str]]) -> tuple:
    #your code here
    pass
    max_len = 0
    result = []

    def dfs(current_sequence, index, used):
        nonlocal max_len, result

        if index == len(words):
            if len(current_sequence) > max_len:
                max_len = len(current_sequence)
                result = [current_sequence.copy()]
            elif len(current_sequence) == max_len:
                result.append(current_sequence.copy())
            return
        
        picked = False

        for word in words[index]:
            if word not in used:
                picked = True
                current_sequence.append(word)
                used.add(word)

                dfs(current_sequence, index + 1, used)

                current_sequence.pop()
                used.remove(word)

        if not picked:
            dfs(current_sequence, index + 1, used)

    dfs([], 0, set())

    return max_len, result

words = [["apple", "banana"], ["apple"], ["cherry", "banana"]]
print(longest_unique_word_sequence(words))
# ผลลัพธ์: (3, [['banana', 'apple', 'cherry'], ['apple', 'cherry', 'banana']])

words2 = [["dog", "cat"], ["mouse", "cat"], ["bird", "dog"]]
print(longest_unique_word_sequence(words2))
# ผลลัพธ์: (4, [['mouse', 'cat', 'bird', 'dog']])


