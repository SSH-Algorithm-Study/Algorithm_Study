class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        multiple = 1

        output.append(1)  #처음에 1넣어주기 
        for i in range(0, len(nums)-1):
            multiple *= nums[i]
            output.append(multiple)  # 1, 1*2 , 1*2*3 차례로

        multiple = 1  
        for i in range(len(nums) - 2, -1, -1):
            multiple *= nums[i + 1]
            output[i] *= multiple    # 4, 4*3, 4*3*2 뒤부터 차례로

        return output