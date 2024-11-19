def twosum(nums:list[int], target:int) -> list[int]:
    retorno = {}
    for num in range(len(nums)):
        for i in range(len(nums)):
            if i == num:
                pass
            elif nums[i] + nums[num] == target:
                retorno[num] = nums[num]
                retorno[i] = nums[i]
                return retorno
        
print(twosum([1,2,1,2],4))