class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        lp = 0
        l = []

        while lp <= len(nums)-3:

            mp = lp + 1
            hp = len(nums) - 1

            while mp < hp:

                total = nums[lp] + nums[mp] + nums[hp]

                if total == 0:

                    if [nums[lp], nums[mp], nums[hp]] not in l:
                        l.append([nums[lp], nums[mp], nums[hp]])

                    mp += 1

                elif total > 0:
                    hp -= 1

                else:
                    mp += 1

            lp += 1

        return l