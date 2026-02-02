### task 1

testDict = {"one" : [5, 7, 9, 4, 0], "two" : [6, 7, 4, 3, 3], "three" : [9, 9, 6, 5, 5]}
UMax = 0
keyValue = ''

for key, values in testDict.items():
    uniqueCount = len(set(values)) 
    if uniqueCount > UMax:
        UMax = uniqueCount
        keyValue = key
print("Key with maximum unique values:", keyValue)

testDict2 = {"one" : [5, 7, 7, 7, 7], "two" : [6, 7, 7, 7], "three" : [9, 9, 6, 5, 5]}
UMax = 0
keyValue = ''

for key, values in testDict2.items():
    uniqueCount = len(set(values)) 
    if uniqueCount > UMax:
        UMax = uniqueCount
        keyValue = key
print("Key with maximum unique values:", keyValue)

## task 2
test_list = ["DataScience", 3, "is", 8]
key_list = ["name", "id"]

result = []

for i in range(0, len(test_list), len(key_list)):
    values_slice = test_list[i:i+len(key_list)]
    temp_dict = dict(zip(key_list, values_slice))
    result.append(temp_dict)

print(result)

## task 3
tuples_list = [("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]
result = {}

for key, value in tuples_list:
    result[key] = [value]  
print(result)

# task 4
my_dict = {'c': [3], 'b': [12, 10], 'a': [19, 4]}

for key in my_dict:
    my_dict[key].sort()

sorted_dict = dict(sorted(my_dict.items()))
print(sorted_dict)

# task 5
import string
letters = string.ascii_lowercase

count = 0 

my_string = "Hello World"
my_string = my_string.lower()
letter_count = {letter: my_string.count(letter) for letter in string.ascii_lowercase}

print(letter_count)








