def search_range(nums, target):
    
    return [find_first(nums, target), find_last(nums, target)]


def find_first(nums, target):
    left, right = 0, len(nums) - 1
    ans = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            ans = mid
            right = mid - 1   # move left
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return ans


def find_last(nums, target):
    left, right = 0, len(nums) - 1
    ans = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            ans = mid
            left = mid + 1    # move right
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return ans


# Example usage
if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(search_range(nums, target))  # Output: [3, 4]