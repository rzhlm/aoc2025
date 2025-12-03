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
    pass

if __name__ == "__main__":
    main()
