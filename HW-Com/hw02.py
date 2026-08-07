def longest_unique_word_sequence(words: list[list[str]]) -> tuple:
    #your code here
    continuous = sum(words, [])
    seen = []
    component = []
    start = 0
    for i in range(len(continuous)):
        print(f"i: {i}, start: {start}, seen: {seen}, component: {component}")
        x = continuous[i]
        # print(f"i:{i}, x:{x}")
        if x not in seen:
            seen.append(x)
            # print(f"seen: {seen}")
        else:
            # print(f"Else_Condition")
            start += 1
            component.append(seen)
            # print(f'component: {component}')
            if x in continuous[start:i-1]:
                start += 1
                seen = continuous[start:i+1]
                continue
            seen = continuous[start:i+1]
    component.append(seen)
    final = [x for x in component if len(x) == max(len(y) for y in component)]
    return (len(final[0]), final)

words = [["apple", "banana"], ["apple"], ["cherry", "banana"]]
print(longest_unique_word_sequence(words))
# ผลลัพธ์: (3, [['banana', 'apple', 'cherry'], ['apple', 'cherry', 'banana']])

words2 = [["dog", "cat"], ["mouse", "cat"], ["bird", "dog"]]
print(longest_unique_word_sequence(words2))
# ผลลัพธ์: (4, [['mouse', 'cat', 'bird', 'dog']])


