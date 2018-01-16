min = 100; max = 0
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
for i in numbers:
     if min > i:
         min = i
     if max < i:
        max = i
print("the minimum of the sequence is", min)
print("the maximum of the sequence is", max)
