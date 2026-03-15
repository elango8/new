# n=5
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     for k in range(2*i):
#         print(" ",end=" ")
#     for l in range(n-i):
#         print("*",end=" ")
#     print()
# for p in range(n):
#     for e in range(p+1):
#         print("*",end=" ")
#     for g in range((n*2)-(p*2)-2):
#         print(" ",end=" ")
#     for x in range(p+1):
#         print("*",end=" ")
#     print()

# n=5
# for p in range(n):
#     for e in range(p+1):
#         print("*",end=" ")
#     for g in range((n*2)-(p*2)-2):
#         print(" ",end=" ")
#     for x in range(p+1):
#         print("*",end=" ")
#     print()

# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     for k in range(2*i):
#         print(" ",end=" ")
#     for l in range(n-i):
#         print("*",end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or i == n-1 or j == n-1:
#             print(4,end="")
#         else:print(5,end="")
#     print()
# print()

def print_square(n):
    border = 4
    inside = 4
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0 or i == n-1 or j == n-1:
                print(border, end="")
            else:
                print(inside, end="")
        inside -= 1
        print()
print_square(7)


