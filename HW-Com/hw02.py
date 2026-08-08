def longest_unique_word_sequence(words: list[list[str]]) -> tuple:
    #your code here
    continuous = sum(words, [])
    meet = [] #เก็บค่าของคำที่เจอแล้ว
    Box = [] #เก็บค่าของคำที่เจอแล้วในแต่ละ component
    start = 0 #เก็บตำแหน่งเริ่มต้นของลำดับคำที่ไม่มีตัวซ้ำ
    for i in range(len(continuous)): #คือเพื่อวนลูปเช็คค่าของ continuous
        x = continuous[i]
       
        if x not in meet: #เช็คว่าค่าของ x นั้นอยู่ใน meet มั้ย ถ้าไม่อยู่ก็ให้เพิ่มค่า x เข้าไปใน meet
            meet.append(x) 
           
        else:  #เช็คว่าค่าของ x นั้นอยู่ใน meet มั้ย ถ้าอยู่ก็ให้เพิ่มค่า start ขึ้น 1 และเพิ่มค่าของ meet เข้าไปใน Box
            start += 1
            Box.append(meet) #คือเพิ่มค่าของ meet เข้าไปใน Box
            
            if x in continuous[start:i-1]:  #เช็คว่าค่าของ x นั้นอยู่ใน continuous[start:i-1] มั้ย ถ้าอยู่ก็ให้เพิ่มค่า start ขึ้น 1 และเพิ่มค่าของ meet เข้าไปใน Box
                start += 1 
                meet = continuous[start:i+1]
                continue
            meet = continuous[start:i+1]
    Box.append(meet)
    final = [x for x in Box if len(x) == max(len(y) for y in Box)]
    return (len(final[0]), final)

words = [["apple", "banana"], ["apple"], ["cherry", "banana"]]
print(longest_unique_word_sequence(words))
# ผลลัพธ์: (3, [['banana', 'apple', 'cherry'], ['apple', 'cherry', 'banana']])

words2 = [["dog", "cat"], ["mouse", "cat"], ["bird", "dog"]]
print(longest_unique_word_sequence(words2))
# ผลลัพธ์: (4, [['mouse', 'cat', 'bird', 'dog']])


