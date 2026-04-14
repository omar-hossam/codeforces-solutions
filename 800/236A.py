import sys


# Original Version
"""
def main() -> None:
    letters = list(sys.stdin.readline().strip())
    count = len(set(letters))
    sys.stdout.write("CHAT WITH HER!" if count % 2 == 0 else "IGNORE HIM!")
"""

# More PRO & Performance Version!
def main() -> None:
    count = len(set(sys.stdin.readline().strip()))
    # use '&' operator to check if the last bit is 0 'EVEN' else it's 'ODD'
    sys.stdout.write("CHAT WITH HER!" if count & 1 == 0 else "IGNORE HIM!")
    
    
if __name__ == '__main__':
    main()
