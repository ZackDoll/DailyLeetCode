class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        nums_seen = dict()
        result = [0] * len(arr)
        for i in range(len(arr)):
            if arr[i] not in nums_seen:
                nums_seen[arr[i]] = [i,]
            else:
                nums_seen.get(arr[i]).append(i)

        #O(n^2)
        #prefix sum maybe??
        #i hate leetcode
        for val, indexes in nums_seen.items():
            if len(indexes) == 1:
                continue
            
            prefix_sum = 0
            for i in range(len(indexes)):
                prefix_sum += indexes[i]
            
            curr_sum = 0
            for i in range(len(indexes)):
                curr_index = indexes[i]

                left_sum = i * curr_index - curr_sum
                right_sum = (prefix_sum - curr_sum - curr_index) - (len(indexes) -i-1) * curr_index

                result[curr_index] = left_sum + right_sum
                curr_sum += curr_index

        return result
