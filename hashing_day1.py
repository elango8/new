def hashing_check(arr_in):
    lis = [int(input()) for i in range(arr_in)]
    has = [0]*13
    for i in lis:
        has[i] +=1
    ch = int(input("enter count no to check there frequency:"))
    lis_c = [int(input(f"no's {i}")) for i in range(ch)]
    li = []
    for che in lis_c:
        if 0 <= che < len(has):
            li.append(f"{che} count {has[che]}")
        else:
            li.append(f"{che} not in range")
    
    return li


print(hashing_check(5))