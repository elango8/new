from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def merge(nums, low, mid, high):
            temp = []
            left = low
            right = mid + 1

            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1

            while left <= mid:
                temp.append(nums[left])
                left += 1

            while right <= high:
                temp.append(nums[right])
                right += 1

            for i in range(len(temp)):
                nums[low + i] = temp[i]

        def merge_sort(nums, low, high):
            if low < high:
                mid = (low + high) // 2
                merge_sort(nums, low, mid)
                merge_sort(nums, mid + 1, high)
                merge(nums, low, mid, high)

        merge_sort(nums, 0, len(nums) - 1)

        return nums[-k]

nums = [8, 3, 5, 2]
sol = Solution()
print(sol.findKthLargest(nums, 2))
