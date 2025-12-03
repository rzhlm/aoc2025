import pdb

LOGGING = False
non_valids = []

def is_invalid(num: str) -> bool:
    print(f"entering is_invalid: {num=}") if LOGGING else None
    #breakpoint()
    if len(num) % 2 != 0:
        return False

    #############
    # 0.1.2.3 (len 4)

    half: int = len(num) // 2
    if num[0:half] == num[half:]:
        print(f"Invalid: {num=}") if LOGGING else None
        return True

    return False

def test_range(start: str, end: str):
    out = [i for i in range(
                            int(start),
                            int(end) + 1)
        if is_invalid(str(i))
    ]
    print(out) if LOGGING else None
    return out

def give_vals() -> list[list[str]]:
    output = []
    with open("./day2a-input","r") as f:
        for line in f:
            vals_list = line.strip().split(",")

    for val in vals_list:
        # "a-b"
        start, end = val.split("-")
        output.append([start, end])
    #print("TEST OUTPUT:")
    #print(output)
    return output

def test() -> None:
    #for i in range(11,23):
    assert(test_range("11","22") == [11,22])
    assert(test_range("95", "115") == [99])
    assert(test_range("998","1012") == [1010])

    assert(
        test_range(
                   "11885_11880",
                   "11885_11890"
               ) == [11885_11885]
    )

    assert(
        test_range(
            "222220",
            "222224"
        ) == [222_222]
    )

    assert(
        test_range(
            "1698522",
            "1698528"
        ) == []
    )

    assert(
        test_range(
            "446_443",
            "446_449"
        ) == [446_446]
    )

    assert(
        test_range(
            "3859_3856",
            "3859_3862"
        ) == [3859_3859]
    )

    #non_valids.append(out)
    #print(non_valids)

def main() -> None:
    test()
    vals = give_vals()
    invalid_nums = []
    for start, end in vals:
        invalid_nums.extend(test_range(start, end))
    #print(invalid_nums)
    print(sum(invalid_nums))

if __name__ == "__main__":
    main()
