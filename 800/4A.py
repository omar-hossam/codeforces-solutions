# Version 1: Brute force (my first solution)
def can_divide_brute(weight: int) -> str:
    if not weight % 2: # if weight is even
        # Loop through `range(weight)` to find 2 even numbers that sum to weight
        for i in range(weight): 
            for j in range(weight):
                if not i % 2 and not j % 2 and i + j == weight:
                    return "YES"
        return "NO" 
    return "NO" # if weight is odd


# Version 2: Mathematical 0(1) (after learning)
def can_divide(weight: int) -> str:
    return "YES" if weight > 2 and weight % 2 == 0 else "NO" 


def main() -> None:
    try:
        w: int = int(input())
        result: str = can_divide(w)
        print(result)
    except ValueError:
        print("NO")

        
if __name__ == "__main__":
    main()
