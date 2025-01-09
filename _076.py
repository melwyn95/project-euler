def solve(nums, soFar, target, cache):
    if (tuple(nums), soFar) in cache:
        return cache[(tuple(nums), soFar)]
    if soFar == target:
        if (tuple(nums), soFar) not in cache:
            cache[(tuple(nums), soFar)] = 1
        return 1
    else:
        ways = 0
        for i in range(len(nums)):
            if soFar + nums[i] <= target:
                ways += solve(nums[i:], soFar + nums[i], target, cache)
        if (tuple(nums), soFar) not in cache:
            cache[(tuple(nums), soFar)] = ways
        return ways

def ways(n):
    cache = {}
    return solve([m for m in range(n-1, 0, -1)], 0, n, cache)

print(ways(100))
