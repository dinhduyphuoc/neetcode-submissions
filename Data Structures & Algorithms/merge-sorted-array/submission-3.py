class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = len(nums1) - 1 - n
        i = len(nums1) - 1
        j = len(nums2) - 1

        while k >= 0:
            print("Before: ", nums1)
            print(i, j, k)
            if j < 0:
                return
            if nums1[k] > nums2[j]:
                nums1[k], nums1[i] = nums1[i], nums1[k]
                k -= 1
                i -= 1
            else:
                nums1[i] = nums2[j]
                i -= 1
                j -= 1
            print("After: ", nums1)
            print(i, j, k)
        
        while j >= 0:
            nums1[i] = nums2[j]
            i -= 1
            j -= 1
            
        

