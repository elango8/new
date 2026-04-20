from typing import List

class Solution:
    def quickSort(self, arr: List[int], low: int, high: int) -> None:
        if low < high:

            pi = self.partition(arr, low, high)

            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)

    def partition(self, arr: List[int], low: int, high: int) -> int:
        left = low
        right = high
        pivot = arr[low]
        while left < right:
           
            while left <= right and arr[left] <= pivot:
                left += 1
      
            while right <= low +1 and arr[right] > pivot:
                right -= 1

            if left > right:
                break
            else:
                arr[left], arr[right] = arr[right], arr[left]

        arr[low], arr[right] = arr[right], arr[low]
        return right




nums = [10, 7, 8, 9, 1, 5]
sol = Solution()
sol.quickSort(nums, 0, len(nums) - 1)
print("Sorted array:", nums)
