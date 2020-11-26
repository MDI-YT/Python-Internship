#task1
list1=[1,2,3,4,5]
list1.append(6)
print(list1)
#output [1, 2, 3, 4, 5, 6]

list1.remove(3)
print(list1)
#output [1, 2, 4, 5, 6]

a=max(list1)
b=min(list1)
print(a,b)
#output 6 1

#task2 
tuples=("one", "two", "three", "four", "five")
print(tuples[::-1])
#output ('five', 'four', 'three', 'two', 'one')

#task3
tuples=list(tuples)
print(tuples)
#output ['one', 'two', 'three', 'four', 'five']