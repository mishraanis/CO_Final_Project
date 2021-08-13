#!/usr/bin/env python3

def assemble(command: str, line_num: int) -> str:
    """
    :param line_num:
    :param command: add R0 R1 R2
    :return: 0000000000001010
    """

    reg = {"R0": "000", "R1": "001", "R2": "010", "R3": "011", "R4": "100",
           "R5": "101", "R6": "110"}

    if command.split()[0] == "mul" and len(command.split()) == 4:
        if ((reg.get(command.split()[1]) is not None) and
                (reg.get(command.split()[2]) is not None) and
                (reg.get(command.split()[3]) is not None)):
            ans = "00110" + reg.get(command.split()[1]) + reg.get(
                command.split()[2]) + reg.get(command.split()[3])
            return ans
        else:
            for i in command.split():
                if i == "FLAGS":
                    print("Line " + line_num + ": ERR: Illegal use of FLAGS")
                    return ""
            print("Line " + line_num + ": ERR: Wrong register")
            return ""

    elif command.split()[0] == "div" and len(command.split()) == 3:
        if ((reg.get(command.split()[1]) is not None) and
                (reg.get(command.split()[2]) is not None)):
            ans = "00111" + reg.get(command.split()[1]) + reg.get(
                command.split()[2])
            return ans
        else:
            for i in command.split():
                if i == "FLAGS":
                    print("Line " + line_num + ": ERR: Illegal use of FLAGS")
                    return ""
            print("Line " + line_num + ": ERR: Wrong register")
            return ""

    elif command.split()[0] == "rs" and len(command.split()) == 3:
        if reg.get(command.split()[1]) is not None:
            ans = "01000" + reg.get(command.split()[1]) + \
                  bin(int(command.split()[2][1:]))[2:]
            return ans
        else:
            for i in command.split():
                if i == "FLAGS":
                    print("Line " + line_num + ": ERR: Illegal use of FLAGS")
                    return ""
            print("Line " + line_num + ": ERR: Wrong register")
            return ""

    elif command.split()[0] == "ls" and len(command.split()) == 3:
        if reg.get(command.split()[1]) is not None:
            ans = "01000" + reg.get(command.split()[1]) + \
                  bin(int(command.split()[2][1:]))[2:]
            return ans
        else:
            for i in command.split():
                if i == "FLAGS":
                    print("Line " + line_num + ": ERR: Illegal use of FLAGS")
                    return ""
            print("Line " + line_num + ": ERR: Wrong register")
            return ""

    elif command.split()[0] == "xor" and len(command.split()) == 4:
        if (reg.get(command.split()[1]) is not None) and \
            (reg.get(command.split()[2]) is not None) and \
                (reg.get(command.split()[3]) is not None):
            ans = "01010" + reg.get(command.split()[1]) + \
                  reg.get(command.split()[2]) + reg.get(command.split()[3])
            return ans
        else:
            for i in command.split():
                if i == "FLAGS":
                    print("Line " + line_num + ": ERR: Illegal use of FLAGS")
                    return ""
            print("Line " + line_num + ": ERR: Wrong register")
            return ""

    elif command.split()[0] == "or" and len(command.split()) == 4:
        if (reg.get(command.split()[1]) is not None) and \
            (reg.get(command.split()[2]) is not None) and \
                (reg.get(command.split()[3]) is not None):
            ans = "01010" + reg.get(command.split()[1]) + \
                  reg.get(command.split()[2]) + reg.get(command.split()[3])
            return ans
        else:
            for i in command.split():
                if i == "FLAGS":
                    print("Line " + line_num + ": ERR: Illegal use of FLAGS")
                    return ""
            print("Line " + line_num + ": ERR: Wrong register")
            return ""

    return ""
