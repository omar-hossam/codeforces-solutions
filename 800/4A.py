def can_divide(weight: int) -> str:
    if not weight % 2: # If weight is even
        # Loop through `range(weight)` to find 2 even numbers that sum to weight
        for i in range(weight): 
            for j in range(weight):
                if not i % 2 and not j % 2 and i + j == weight:
                    return "YES"
        return "NO" 
    return "NO" # If weight is odd

def main() -> None:
    try:
        w: int = int(input())
        result: str = can_divide(w)
        print(result)
    except ValueError:
        print("NO")

        
if __name__ == "__main__":
    main()
