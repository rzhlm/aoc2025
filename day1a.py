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

def rest_position(start: int = 50, instruction: str = "L0") -> int:
    """
       input: start position (def: 50) & line instruction (def: do nothing)
       output: resting position 
    """
    print(f"rest_pos() called with: {start=}; {instruction=}")
    if instruction[0] == "L":
        num_clicks = int(instruction[1:])
        end = start - num_clicks
        if end < 0:
            while end < 0:
                end += 100
    elif instruction[0] == "R":
        num_clicks = int(instruction[1:])
        end = start + num_clicks
        if end > 99:
            while end > 99:
                end -= 100
    else:
        raise Exception("rest_position: instruction: input not valid")
    print(f"{start=}; {num_clicks=}; {end=}")
    return end

def is_zero(position) -> int:
    return position == 0


def give_zeroes(data: tuple[str]) -> int:
    counter: int = 0
    start: int = 50
    for datum in data:
        result = rest_position(start=start, instruction=datum)
        if result == 0:
            counter += 1
        start = result
    return counter


def test():
    test_data = (
        "L68", "L30", "R48","L5","R60","L55","L1","L99","R14","L82"
    )
    assert(rest_position(50, test_data[0]) == 82)
    assert(rest_position(82, test_data[1]) == 52)
    assert(rest_position(52, test_data[2]) == 0)

    assert(give_zeroes(test_data[:3]) == 1)


def main():
    test()
    with open("./day1a-data.txt","r") as f:
        lines = [line.strip() for line in f]
    password = give_zeroes(lines)
    print(f"{password=}")
    

if __name__ == "__main__":
    main()
