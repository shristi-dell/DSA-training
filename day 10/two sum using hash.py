class solution:
    def twosum(self,nums:list[int],target:int):
        hash_map={}
        for i in range(len(nums)):
            current_num=nums[i]
            complement=target-current_num
            if complement in hash_map:
                return[hash_map[complement],i]
            hash_map[current_num]=i

obj=solution()
print(obj.twosum([2,7,11,15],9))