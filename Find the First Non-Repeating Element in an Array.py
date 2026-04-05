def first_non_repeating(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    # also use defaultdict for stores the key and value
    for num in arr:
        if freq[num] == 1:
            return num
    return -1


print(first_non_repeating([4, 5, 1, 2, 0, 4]))  
