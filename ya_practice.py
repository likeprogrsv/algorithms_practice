import sys
'''
j = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()

result = 0
for ch in s:
    if ch in j:
        result += 1
        
        
        
        i = format(112, 'b')

print(i)
'''
'''
5
1
0
1
0
1
'''

'''
lines = []
while True:
    line = input()
    if line:
        lines.append(int(line))
    else:
        break
        
'''
lines = []
with open('input.txt') as f:
    [lines.append(int(line.strip())) for line in f.readlines()]

def max_len(lines):
    if len(lines) == 0 or len(lines) > 10000: return None
    bin = [format(i, 'b') for i in lines]
    bin = [int(i) for i in bin]
    results = []
    for num in range(len(bin)):
        nums = [int(i) for i in str(bin[num])]
        results[num] = results.append(0)
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                results[num] = count
                count = 0
            if len(nums) == 1 or i == len(nums) - 1:
                results[num] = count
    return max(results)
print(max_len(lines))
