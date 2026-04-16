import sys


# My Original Version!
def main() -> None:
	"""
	  NOTES
	  - letters' case does not matter
	  - It is guaranteed that the strings are of the same length
	"""
	
	read, write = sys.stdin.readline, sys.stdout.write
	w1: str
	w2: str
		
	w1, w2 = [read().strip().lower() for _ in range(2)]
	
	_len = len(w1)
	
	if w1 == w2:
		write("0")
		return None
	
	for i in range(_len):
		if w1[i] > w2[i]:
			write("1")
			return None
	
	write("-1")


# More Pythonic!
def pythonic() -> None:
	read, write = sys.stdin.readline, sys.stdout.write 
	w1, w2 = [read().strip().lower() for _ in range(2)]
	if w1 == w2:
		write("0")
	elif w1 < w2:
		write("-1")
	else:
		write("1")


if __name__ == '__main__':
	pythonic()
