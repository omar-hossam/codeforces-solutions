import sys


def get_solvable_questions():
    read, write, count = sys.stdin.readline, sys.stdout.write, str.count
    num_of_lines = int(read())
    
    solvable: int = 0
    TARGET: str = '1'

    for _ in range(num_of_lines):
        if count(read(), TARGET) >= 2:
            solvable += 1

    write(str(solvable) + '\n') 


if __name__ == '__main__':
    get_solvable_questions()
