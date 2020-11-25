#task1
dict1={1:'one', 2:'two', 3:'three',4:'four',5:'five'}
dict2={6:'six', 7:'seven', 8:'eight', 9:'nine'}
dict1.update(dict2)
print(dict1)
#output: {1: 'one', 2: 'two', 3: 'three', 4:'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

#task2
del dict1[3]
print(dict1)
#output {1: 'one', 2: 'two', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

#task3
keys = [10,20,30]
values =['ten', 'twenty', 'thirty']
print(dict(zip(keys, values)))
#output {10: 'ten', 20: 'twenty', 30: 'thirty'}

#task4
Phones= {'Vivo','Redmi','Apple','Samsung'}
print(len(Phones))
#output 4

#task5
FavPhones= {'Apple','Samsung','Realme','Oneplus'}
Phones.difference_update(FavPhones)
print(Phones)
#output {'Vivo', 'Redmi'}
