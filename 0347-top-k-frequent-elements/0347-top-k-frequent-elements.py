class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count= Counter(nums)
        compare = list(count.values())
        answer = []
        check = len(compare) - k
        def quick(left, right):
            if left >= right:
                return 
            pivot = compare[left]
            write = left + 1
            for read in range(left + 1, right + 1):
                if compare[read] <= pivot:
                    compare[read], compare[write] = compare[write], compare[read]
                    write += 1
            compare[write-1], compare[left] = compare[left], compare[write -1]
            if write - 1 == check:
                return compare[write -1]
            elif write - 1 < check:
                return quick(write, right)
            else:
                return quick(left, write - 2)
        quick(0, len(compare) - 1)
        compare = set(compare[check:len(compare)])
        for i, j in count.items():
            if j in compare:
                answer.append(i)
        return answer
