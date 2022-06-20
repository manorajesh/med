import os
import readchar

tbuf = [] # text buffer

def find_index(line):
    global tbuf

    line = 0 if line < 0 else line
    return [i for i, v in enumerate(tbuf) if v == '\n'][line]

def read(file):
    global tbuf
    if os.path.isfile(file):
        tbuf.append(file.read())
    else:
        print(f"{file} is not a file.")

def append(line):
    global tbuf
    text = ""

    while not text.endswith("\n.\n"):
        text += readchar.readkey()

    tbuf.insert(find_index(line), text[:-2])

def insert(line):
    global tbuf
    text = ""

    while not text.endswith("\n.\n"):
        text += readchar.readkey()

    tbuf.insert(find_index(line-1), text)

def change(line):
    global tbuf
    text = ""

    while not text.endswith("\n.\n"):
        text += readchar.readkey()

    tbuf[find_index[line]:find_index[line+1]] = text[:-2]

def print_tbuf(line, all=False):
    global tbuf
    if all:
        print(tbuf)
    else:
        print(tbuf[find_index(line):find_index(line+1)])

def replace(line, old, new, all=False):
    global tbuf
    if all:
        tbuf[find_index(line):find_index(line+1)] = tbuf[find_index(line):find_index(line+1)].replace(old, new)
    else:
        tbuf[find_index(line)] = tbuf[find_index(line)].replace(old, new)

def med(file="", prompt=""):
    global tbuf
    cmd_input = ""
    
    if os.path.isfile(file):
        tbuf = file.read()

    while cmd_input != "q":
        cmd_input = input(prompt)
        cmd, arg1, arg2 = cmd_input.split()

        line = tbuf.count("\n")

        if cmd == "r":
            read(file)
        elif cmd == "a":
            append(int(line))
        elif cmd == "i":
            insert(int(line))
        elif cmd == "c":
            change(int(line))
        elif cmd == "p":
            print_tbuf(int(line))
        elif cmd == ",p":
            print_tbuf(int(line), True)
        elif cmd == "s":
            replace(int(line), arg1.strip("/"), arg2.strip("/"))
        elif cmd == ",s":
            replace(int(line), arg1.strip("/"), arg2.strip("/"), True)
        elif cmd == "w":
            with open(arg1, "w") as file:
                file.write(tbuf)
            file.close()
            print(len(tbuf))
        elif cmd == "P":
            prompt = "*"
        else:
            print("?")


## testing
med()