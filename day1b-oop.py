
class Knob():
    def __init__(self):
        self.position = 50
        self.zero_count = 0

    def rotate(self, instruction: str):
        if instruction[0] not in ("L","R"):
            raise Exception("rotate instruction not valid")

        adding: bool = True if instruction[0] == "R" else False

        try:
            clicks = int(instruction[1:])
        except:
            raise ValueError("rotate instruction not valid")
        
        if clicks == 0:
            pass
        else:
            for _ in range(clicks):
                if adding:
                    self.position += 1
                else:
                    self.position -= 1

                if self.position == 100:
                    self.position = 0
                    
                if self.position = -1:
                    self.position = 99

                if self.position == 0:
                    self.zero_count += 1


def test():
    test_knob = Knob()
    
    test_knob.rotate("L68")
    assert(test_knob.position == 82)
    assert(test_knob.zero_count == 1)

def main():
    test()
    pass()


if __name__ == "__main__":
    main()
