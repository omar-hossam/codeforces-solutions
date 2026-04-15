import sys

nums = sys.stdin.readline().strip().split('+')

nums.sort()

sys.stdout.write('+'.join(nums))
