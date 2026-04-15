arr = [12,11,13,5,6,7]
def rec(arr):
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    rec(left_half)
    rec(right_half)