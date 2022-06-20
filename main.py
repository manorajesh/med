import os, io

tbuf = [] # text buffer

def find_index(line):
    global tbuf
    if tbuf == []:
        return 0

    line = 0 if line < 0 else line

    total = [i for i, v in enumerate(tbuf) if v == '\n']
    total.insert(0, 0)
    total.append(len(tbuf)-1)
    return total[line%len(total)]

def read(file):
    global tbuf
    text = ""
    if file.startswith("!"):
        file = execute(file[1:])

    try:
        with open(file, "r") as file:
            text = file.read()
    except (FileNotFoundError, TypeError):
        try:
            with file as f:
                text = f.read()
        except:
            print(f"{file} not found")
            return
    finally:
        tbuf[len(tbuf):] = text
        print(len(text))

def append(line):
    global tbuf
    text = ""

    while not text.endswith("\n.\n"):
        text += input()
        text += "\n"

    tbuf[find_index(line):find_index(line+1)] = text[:-3]

def insert(line):
    global tbuf
    text = ""

    while not text.endswith("\n.\n"):
        text += input()
        text += "\n"

    tbuf[find_index(line-2):find_index(line-1)] = text[:-2]

def change(line):
    global tbuf
    text = ""

    while not text.endswith("\n.\n"):
        text += input()
        text += "\n"

    tbuf[find_index(line-1):find_index(line)] = text[:-3]

def print_tbuf(line, all=False):
    global tbuf
    if all:
        print("".join(tbuf))
    else:
        print("".join(tbuf[find_index(line-1):find_index(line)]))

def print_tbuf_raw(line, all=False):
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

def execute(command):
    return os.popen(command)

def med(file="", prompt=""):
    global tbuf
    cmd_input = ""
    
    if os.path.isfile(file):
        tbuf = file.read()

    line = tbuf.count("\n")
    while cmd_input != "q":
        try:
            cmd_input = input(prompt)
            cmd = cmd_input.split()

            if cmd[0] == "r":
                read(cmd[1])
                line = tbuf.count("\n")
            elif cmd[0] == "a":
                append(line)
                line += 1
            elif cmd[0] == "i":
                insert(line)
                line -= 1
            elif cmd[0] == "c":
                change(line)
            elif cmd[0] == "p":
                print_tbuf(line)
            elif cmd[0] == ",p":
                print_tbuf(line, True)
            elif cmd[0] == "s":
                replace(line, cmd[1].strip("/"), cmd[2].strip("/"))
            elif cmd[0] == ",s":
                replace(line, cmd[1].strip("/"), cmd[2].strip("/"), True)
            elif cmd[0] == "w":
                with open(cmd[1], "w") as file:
                    file.write(tbuf)
                print(len(tbuf))
            elif cmd[0] == "P":
                prompt = "*"
            elif cmd[0].startswith("!"):
                print(execute(cmd[0][1:]).read().rstrip())
            elif cmd[0] == "wq":
                with open(cmd[1], "w") as file:
                    file.write(tbuf)
                print(len(tbuf))
                break
            elif cmd[0].isnumeric():
                line = int(cmd[0])
            elif cmd[0] == "n":
                print(line, end=" ")
                print_tbuf(line)
            elif cmd[0] == "pr":
                print_tbuf_raw(line)
            elif cmd[0] == ",pr":
                print_tbuf_raw(line, True)
            else:
                print("?")
        except IndexError:
            print("? +")


## testing
try:
    med()
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise