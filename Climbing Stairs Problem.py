def climb_stairs(n: int) -> int:

    if n == 0:
        return 1
    if n < 0:
        return 0
    
    return climb_stairs(n-1) + climb_stairs(n-2)

print(climb_stairs(5)) 