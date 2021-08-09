def trap( height) -> int:
    left , right = 0, len(height)-1
    point = left+1
    water = 0

    while left < right:
        if min(height[left],height[right]) <= height[point]:
            for i in range(left, point+1):
                water = water + min(height[left], height[point]) - height[i]

            left = point







