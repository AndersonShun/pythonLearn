





class Solution(object):
    def twosum(self, nums, target):
        '''
        '''
        lookup = {}
        for i,num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i

        return []

if __name__ == '__main__':
    sol = Solution()
    ans = sol.twosum([2,1,4,5,6],3) 
    print(ans)