import sys


def main() -> None:
	word: str = sys.stdin.readline().strip()
	sys.stdout.write(f"{word[0].upper()}{word[1:]}")
	
	
if __name__ == '__main__':
	main()
