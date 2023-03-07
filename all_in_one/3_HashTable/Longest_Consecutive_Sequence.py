def longestConsecutive(nums):
    save = {}
    for num in nums:
        save[num] = True

    max_length = 0

    for num in nums:
        length = 0
        if (num - 1) not in save:
            while (num + 1) in save:
                length += 1
        max_length = max(max_length, length)

    return max_length


print(longestConsecutive([100, 4, 200, 1, 3, 2]))
