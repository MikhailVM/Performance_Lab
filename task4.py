def reduction(nums):
    nums.sort()
    mid = len(nums) // 2
    result = 0
    for n in nums:
        result += abs(n - nums[mid])
    return result


file_name = input('Введите имя файла с массивом: ')

data = []
file = open(file_name, 'r')
for line in file:
    line.strip()
    data.append(int(line))

print(reduction(data))
