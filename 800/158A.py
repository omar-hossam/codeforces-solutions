import sys


# Original Version:
"""
def main() -> None:
    read, strip = sys.stdin.readline, str.strip
    
    line: list[str] = strip(read()).split(" ")

    n, k = int(line[0]), int(line[1])
    advancers: int = 0    
    
    if k >= 1 and k <= n and n <= 50:
        nums_str: list[str] = strip(read()).split(" ")
        nums: list[int] = list(map(int, nums_str))
        
        k_th_value: int = nums[k - 1]
        
        for i in range(n):
            if nums[i] >= k_th_value and nums[i] > 0:
                advancers += 1
        
    
    sys.stdout.write(str(advancers))
"""    

# Production ready version for ultimate performance and readability:
def main() -> None:
    read = sys.stdin.readline
    
    n, k = map(int, read().split())
    
    scores = list(map(int, read().split()))
    
    threshold = scores[k-1]
    count = 0
    for s in scores:
        if s >= threshold and s > 0:
            count += 1
            
    sys.stdout.write(str(count))


if __name__ == '__main__':
    main()
