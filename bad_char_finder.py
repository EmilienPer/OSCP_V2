
immunity_deb_output_file=input("Path to the immunity debugger output:")

def construct_initial_char_list():
    t=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    char_list = []
    for c in t:
        for c2 in t:
            if c!="0" or c2!="0":
                char_list.append("{}{}".format(c,c2))
    return char_list

def show_char(char_list):
    print("".join(['\\x{}'.format(elem) for elem in char_list]).lower())

def get_input():
    if input("Continue [Y/n]") != "n":
        with open(immunity_deb_output_file,"r") as f:
            print(f.readlines())
    return []

def show_bad_char(bad_char_list):
    print("BAD","".join(['\\x{}'.format(elem) for elem in bad_char_list]).lower())





bad_char=["00"]
char_list=construct_initial_char_list()
need_loop=True
while need_loop:
    need_loop=False
    show_char(char_list)
    print("")
    in_char=get_input()
    for i in range(min(len(in_char),len(char_list))):
        if in_char[i]!=char_list[i]:
            new_bad=char_list[i]
            bad_char.append(new_bad)
            char_list.remove(new_bad)
            need_loop=True
show_bad_char(bad_char)