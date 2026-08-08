def longest_unique_word_sequence(words: list[list[str]]) -> tuple:
    #your code here
    continuous = sum(words, [])
    seen = [] #เก็บค่าของคำที่เจอแล้ว
    component = [] #เก็บค่าของคำที่เจอแล้วในแต่ละ component
    start = 0 #เก็บตำแหน่งเริ่มต้นของลำดับคำที่ไม่มีตัวซ้ำ
    for i in range(len(continuous)): #คือเพื่อวนลูปเช็คค่าของ continuous
        x = continuous[i]
       
        if x not in seen: #คือเช็คว่าค่าของ x นั้นอยู่ใน seen มั้ย ถ้าไม่อยู่ก็ให้เพิ่มค่า x เข้าไปใน seen
            seen.append(x) 
           
        else:
            start += 1
            component.append(seen) #คือเพิ่มค่าของ seen เข้าไปใน component
            
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


