import sys


def main() -> None:
    M, N = map(int, sys.stdin.readline().split())
    sys.stdout.write(str((M * N) // 2))
    
    
if __name__ == '__main__':
    main()
