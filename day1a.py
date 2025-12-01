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

def rest_position(instruction: str) -> int:
    pass

def is_zero(position) -> int:
    return position == 0


def test():
    test_data = (
        "L68", "L30", "R48","L5","R60","L55","L1","L99","R14","L82"
    )
    assert()


def main():
    test()

if __name__ == "__main__":
    main()
