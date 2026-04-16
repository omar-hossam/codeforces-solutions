import sys


def main() -> None:
	read = sys.stdin.readline
	w1: str
	w2: str
	
	w1, w2 = [read().strip() for _ in range (2)]
	sys.stdout.write("YES" if w1 == w2[::-1] else "NO")


if __name__ == '__main__':
	main()
