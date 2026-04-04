def trap(height):
    l = 0
    r = len(height) - 1
    total = 0
    l_max = height[l]
    r_max = height[r]
    
    while l < r:
        if height[l] < height[r]:
            l_max = max(l_max, height[l])
            total += l_max - height[l]
            l += 1
        else:
            r_max = max(r_max, height[r])
            total += r_max - height[r]
            r -= 1  
    return total

print(trap([0,1,0,2,1,3,0,1,3,2,1,2,1]))