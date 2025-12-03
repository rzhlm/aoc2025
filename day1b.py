# password in safe
# dial with arrow. circle
# digits 0 to 99
# data:
# rotations, 1 per line
# (direction) num_clicks
# start: at 50
#
# password:
# number of times the dial has pointed at 0, after each rotation
# 

LOGGING = True

def rest_position(start: int = 50, instruction: str = "L0") -> int:
    """
       input: start position (def: 50) & line instruction (def: do nothing)
       output: resting position 
    """
    count = 0
    print("*"*20) if LOGGING else None
    print(f"rest_pos() called with: {start=}; {instruction=}") if LOGGING else None
    if instruction[0] == "L":
        num_clicks = int(instruction[1:])
        end = start - num_clicks
        if end < 0:
            while end < 0:
                end += 100
                count += 1
        elif end == 0:
            count += 1
            
    elif instruction[0] == "R":
        num_clicks = int(instruction[1:])
        end = start + num_clicks
        if end > 99:
            while end > 99:
                end -= 100
                count += 1
    else:
        raise Exception("rest_position: instruction: input not valid")
    print(f"{start=}; {num_clicks=}; {end=} ; {count=}") if LOGGING else None
    
    return (end, count)

def is_zero(position) -> int:
    return position == 0


def give_zeroes(data: tuple[str]) -> int:
    print(f"\tgive_zeroes called with: {data=}") if LOGGING else None
    counter: int = 0
    start: int = 50
    
    for datum in data:
        print(f"\t\tgive zeroes for datum loop: {datum=}") if LOGGING else None
        result, zeroes = rest_position(start=start, instruction=datum)
        print(f"\t\t thus: {result=}; {zeroes=}; {counter=}") if LOGGING else None
        #if result == 0:
        #    counter += 1
        counter += zeroes
        #if result == 0:
        #   counter += 1
        start = result
        print(f"\t\tafterwards: {counter=}; {result=}") if LOGGING else None
    print(f"\t end of give_zeroes: {counter=}") if LOGGING else None
    print("-"*80) if LOGGING else None
    return counter


def test():
    test_data = (
        "L68", "L30", "R48","L5","R60","L55","L1","L99","R14","L82"
    )
    assert(rest_position(50, test_data[0]) == (82,1)) # 50-68 
    assert(rest_position(82, test_data[1]) == (52,0)) # 82-30
    assert(rest_position(52, test_data[2]) == (0,1)) # 52+48

    assert(give_zeroes(["R1000"]) == 10)

    print(give_zeroes(test_data))
    assert(give_zeroes(test_data) == 6)
    

    assert(give_zeroes(["R49"]) == 0)
    print(give_zeroes(["R49","R0"]))
    assert(give_zeroes(["R49","R1"]) == 1)
    assert(give_zeroes(["R49","R1","R0","R0"]) == 1)
    assert(give_zeroes(["R49","R1","R0","L1"]) == 2)

    #assert(give_zeroes(["R49","L99","R1","L1","R1","L1"]) == 3) # 50->99->0->1->0->1
    print(give_zeroes(["R49","L99","R1","L1","R1","L1"]))


def main():
    test()
    
    with open("./day1a-data.txt","r") as f:
        lines = [line.strip() for line in f]
    #password = give_zeroes(lines)
    #print(f"{password=}")
    

if __name__ == "__main__":
    main()
