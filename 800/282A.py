import sys
    

def bitpp() -> None:
    read, write, strip,  = sys.stdin.readline, sys.stdout.write, str.strip

    x_value: int = 0
    num_of_lines: int = int(read())
    
    # My original mathmatical clever version:
    """
    find = str.find 
    
    for _ in range(num_of_lines):
        line = strip(read())
        X = find(line, "X")
        
        if X >= 0:
            # if X is zero get the next operator if '+' then '+1' if '-' then '-1' to x_value, if it's not in index 0 then get the operator before it and do the same 
            
            x_value += int(f"{line[X + 1]}1") if X == 0 else int(f"{line[X - 1]}1")
    """
    
    # Performance and production ready version:
    for _ in range(num_of_lines):
        line = strip(read())
        
        if '++' in line:
            x_value += 1
        elif '--' in line:
            x_value -= 1
        
    sys.stdout.write(str(x_value))
    
    
if __name__ == '__main__':
    bitpp()
