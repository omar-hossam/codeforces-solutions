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
