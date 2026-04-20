import sys


def main() -> None:
    read, strip = sys.stdin.readline, str.strip
    row, col = 0, 0
    
    for i in range(5):
        inp = read()
        if '1' in inp:
            row = i
            col = (strip(inp).index('1')) // 2
            break
    
    for _ in range(4 - row):
        read()
            
    sys.stdout.write(f"{abs(2 - col) + abs(2 - row)}")
            
            
if __name__ == '__main__':
    main()
