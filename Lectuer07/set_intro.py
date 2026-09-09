setA = {1,2,3,4}
setB = {3,4,5,6}

setA.add(7)
setB.update({6,7})
Uset = setA | setB
print("Union: ", Uset)
print(len(Uset))

setB.update('ABCD')
setA.update([6,7,8,])
print( setB)

print(setA.intersection(setB))
print(setA^setB)

setB.remove('B')
setB.discard(10)
print(setB)
print(setA.clear())

for val in Uset:
    print(val)