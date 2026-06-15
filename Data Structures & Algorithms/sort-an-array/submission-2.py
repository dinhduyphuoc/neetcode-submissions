class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(a, low, high):
            pivot = a[low + (high - low) // 2]

            i = low - 1
            j = high + 1

            while True:
                i += 1
                while a[i] < pivot:
                    i += 1
                j -= 1
                while a[j] > pivot:
                    j -= 1
                if i >= j:
                    return j
                
                a[i], a[j] = a[j], a[i]
        
        def quicksort(a, low, high=None):
            if high is None:
                high = len(a) - 1
            
            if low < high:
                p = partition(a, low, high)
                quicksort(a, low, p)
                quicksort(a, p + 1, high)
            
        quicksort(nums, 0)

        return nums