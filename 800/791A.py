import sys


def main():
	limak, bob = map(int, sys.stdin.readline().strip().split())

	if limak == bob:
		sys.stdout.write('1')
		return 0
	
	years = 0
	
	while limak <= bob:
		if limak == bob:
			years += 1
			break
		limak *= 3
		bob *= 2
		years += 1

	sys.stdout.write(str(years))


if __name__ == '__main__':
	main()
