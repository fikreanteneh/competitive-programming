class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for val in image:
            val.reverse()
            for i, num in enumerate(val):
                val[i] = 1 - num
        return image