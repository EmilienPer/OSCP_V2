import re

immunity_deb_output_file = input("Path to the immunity debugger output:")
start_bad=input("Already know bad char:(ex:\\x00\\xff)")


def get_start_bad():
    return start_bad.upper().split("\\X")

def construct_initial_char_list():
    t = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    char_list = []
    for c in t:
        for c2 in t:
            if c != "0" or c2 != "0":
                char_list.append("{}{}".format(c, c2))
    return char_list


def show_char(char_list):
    print("".join(['\\x{}'.format(elem) for elem in char_list]).lower())


def get_input():
    regex = '(\S*)' \
            '\s\s' \
            '([0-9f-zA-F]{2}|(\s{2}}))' \
            '\s' \
            '([0-9f-zA-F]{2}|(\s{2}))' \
            '\s' \
            '([0-9f-zA-F]{2}|(\s{2}))' \
            '\s' \
            '([0-9f-zA-F]{2}|(\s{2}))' \
            '\s' \
            '([0-9f-zA-F]{2}|(\s{2}))' \
            '\s' \
            '([0-9f-zA-F]{2}|(\s{2}))' \
            '\s' \
            '([0-9f-zA-F]{2}|(\s{2}))' \
            '\s' \
            '([0-9f-zA-F]{2}|(\s{2}))'
    out = []
    if input("Continue [Y/n]") != "n":
        with open(immunity_deb_output_file, "rb") as f:
            for line in f.readlines():
                try:
                    l = re.findall(regex, line.decode('utf-8'))[0]
                    for e in [1, 3, 5, 7, 9, 11, 13, 15]:
                        if len(l[e]) != 0:
                            out.append(l[e])
                except:
                    pass

            return out
    return []


def show_bad_char(bad_char_list):
    print("BAD", "".join(['\\x{}'.format(elem) for elem in bad_char_list]).lower())


bad_char = ["00"]
char_list = construct_initial_char_list()
for elem in get_start_bad():
    try:
        if elem != "":
            bad_char.append(elem)
            char_list.remove(elem)
    except:
        pass
need_loop = True
while need_loop:
    need_loop = False
    show_char(char_list)
    print("")
    in_char = get_input()
    for i in range(min(len(in_char), len(char_list))):
        if in_char[i].upper() != char_list[i].upper():
            new_bad = char_list[i]
            bad_char.append(new_bad)
            char_list.remove(new_bad)
            need_loop = True
            print(" >>>>>>>       Find a bag char: {}".format(new_bad))
            break
show_bad_char(bad_char)
