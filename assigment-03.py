# n = int(input("Enter a positive integer: "))

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end="")

#     for k in range(i-1, 0, -1):
#         print(k, end="")
#     print()


Pn = int(input("Enter how many prime numbers do you need: "))
count = 0
num = 2 

while count < Pn:
    for i in range(2, int(num**0.5) + 1):
        print(num , i)
        if num % i == 0:
            break
    else:
        # print(num, end=" ")
        count += 1
    num += 1








# count = 0
# num = 2

# while count < Pn:
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=" ")
#         count += 1
#     num += 1