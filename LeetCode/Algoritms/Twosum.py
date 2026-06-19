def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Создаем пустой словарь: в будущем добавляем туда "значение:индекс"
        dict_map = {}
        for i,num in enumerate(nums):
            curr = target - num
            if curr in dict_map: 
                return [i, dict_map.get(curr)]
            else:
                dict_map[nums[i]] = i

if __name__ == '__main__':
    nums = input().strip().strip(']').strip('[').split(',')
    nums = list(map(int,nums))
    target = int(input())
    print(twoSum(nums, target))