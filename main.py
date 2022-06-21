import os

tbuf = [] # text buffer

def find_index(line):
    global tbuf
    if tbuf == []:
        return 0

    line = 0 if line < 0 else line

    total = [i for i, v in enumerate(tbuf) if v == '\n']
    total.insert(0, 0)
    total.append(len(tbuf)-1)
    return total[line]

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

    tbuf = list("".join(tbuf[:find_index(line)+1]) + text[:-3] + "".join(tbuf[find_index(line):]))

def insert(line):
    global tbuf
    text = ""

    while not text.endswith("\n.\n"):
        text += input()
        text += "\n"

    if line == 1:
        for i, v in enumerate(text[:-2]):
            tbuf.insert(find_index(line-1)+i, v)
    else:
        for i, v in enumerate(text[:-2]):
            tbuf.insert(find_index(line-1)+i+1, v)

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
        print("".join(tbuf[find_index(line-1):find_index(line)+1]).replace("\n", "", 2)) # fix

def print_tbuf_raw(line, all=False):
    global tbuf
    if all:
        print(tbuf)
    else:
        print(tbuf[find_index(line):find_index(line+1)])

def replace(line, old, new, all=False):
    global tbuf
    if all:
        tbuf[:] = "".join(tbuf[:len(tbuf)]).replace(old, new)
    else:
        tbuf[find_index(line-1):find_index(line)] = "".join(tbuf[find_index(line-1):find_index(line)]).replace(old, new)

def execute(command):
    return os.popen(command)

def delete(line):
    global tbuf
    for i in range(find_index(line-1), find_index(line)+1):
        del tbuf[i]

def med(file="", prompt=""):
    global tbuf
    cmd_input = ""
    
    if os.path.isfile(file):
        with open(file, "r") as file:
            tbuf = file.read()

    line = tbuf.count("\n")
    undo = [] # undo buffer
    while cmd_input != "q":
        try:
            cmd_input = input(prompt)
            cmd = cmd_input.split()
            
            if cmd[0] == "r":
                undo = list(tbuf) # keep last change
                read(cmd[1])
                line = tbuf.count("\n")
            elif cmd[0] == "a":
                undo = list(tbuf) # keep last change
                append(line)
                line += 1
            elif cmd[0] == "i":
                undo = list(tbuf) # keep last change
                insert(line)
                line = line - 1 if line > 1 else 1
            elif cmd[0] == "c":
                undo = list(tbuf) # keep last change
                change(line)
            elif cmd[0] == "p":
                print_tbuf(line)
            elif cmd[0] == ",p":
                print_tbuf(line, True)
            elif cmd[0].startswith("s"):
                undo = list(tbuf) # keep last change
                replace(line, cmd[0].split("/")[1], cmd[0].split("/")[2])
            elif cmd[0].startswith(",s"):
                undo = list(tbuf) # keep last change
                replace(line, cmd[0].split("/")[1], cmd[0].split("/")[2], True)
            elif cmd[0] == "w":
                with open(cmd[1], "w") as file:
                    file.write("".join(tbuf))
                print(len(tbuf))
            elif cmd[0] == "W":
                with open(cmd[1], "a") as file:
                    file.write("".join(tbuf))
                print(len(tbuf))
            elif cmd[0] == "P":
                prompt = "*"
            elif cmd[0].startswith("!"):
                print(execute(cmd[0][1:]).read().rstrip())
            elif cmd[0] == "wq":
                with open(cmd[1], "w") as file:
                    file.write("".join(tbuf))
                print(len(tbuf))
                break
            elif cmd[0].isnumeric():
                line = int(cmd[0]) if 0 < int(cmd[0]) < tbuf.count("\n")+2 else 1
            elif cmd[0] == "n":
                print(line, end=" ")
                print_tbuf(line)
            elif cmd[0] == "pr":
                print_tbuf_raw(line)
            elif cmd[0] == ",pr":
                print_tbuf_raw(line, True)
            elif cmd[0] == "d":
                undo = list(tbuf) # keep last change
                delete(line)
                line = line - 1 if line > 1 else 1
            elif cmd[0] == "u":
                tbuf = undo
                line = tbuf.count("\n")
            else:
                print("?")
        except IndexError:
            print("? +")
        except FileNotFoundError:
            print(f"{cmd[1]} not found")

med()