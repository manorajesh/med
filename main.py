import os

tbuf = [] # text buffer

def read(file):
    global tbuf
    text = ""
    if file.startswith("!"):
        file = execute(file[1:])

    try:
        with open(file, "r") as file:
            text = file.readlines()
    except (FileNotFoundError, TypeError):
        try:
            with file as f:
                text = f.readlines()
        except:
            print(f"{file} not found")
            return
    finally:
        for val in text:
            tbuf.append(val)
        print(sum(len(i) for i in text))

def append(line):
    global tbuf
    text = ""

    while not text.endswith("\n.\n"):
        text += input()
        text += "\n"

    text = text[:-3].split("\n")

    for val in text:
        tbuf.insert(line+1, val)

def insert(line):
    global tbuf
    text = ""

    while not text.endswith("\n.\n"):
        text += input()
        text += "\n"

    text = text[:-3].split("\n")

    for val in text[::-1]:
        tbuf.insert(line, val)

def change(line):
    global tbuf
    text = ""

    while not text.endswith("\n.\n"):
        text += input()
        text += "\n"

    text = text[:-3].split("\n")

    tbuf.pop(line)
    for val in text[::-1]:
        tbuf.insert(line, val)

def print_tbuf(line, all=False):
    global tbuf
    if all:
        print("\n".join(tbuf))
    else:
        print(tbuf[line])

def print_tbuf_raw(line, all=False):
    global tbuf
    if all:
        print(tbuf)
    else:
        print(tbuf[line])

def print_tbuf_w_lines():
    global tbuf
    for line, val in enumerate(tbuf):
        print(line, val)

def replace(line, old, new, all=False):
    global tbuf
    if all:
        tbuf = "\n".join(tbuf).replace(old, new).split("\n")
    else:
        tbuf[line] = tbuf[line].replace(old, new)

def execute(command):
    return os.popen(command)

def delete(line):
    global tbuf
    tbuf.pop(line)

def med(file="", prompt=""):
    global tbuf
    cmd_input = ""
    
    if os.path.isfile(file):
        with open(file, "r") as file:
            tbuf = file.readlines()

    line = len(tbuf)-1
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
                line = line - 1 if line > 0 else 0
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
                replace(line, cmd[0].split("/")[1], cmd[0].split("/")[2], True) # what if s/ ///
            elif cmd[0] == "w":
                with open(cmd[1], "w") as file:
                    file.write("\n".join(tbuf))
                print(len(tbuf))
            elif cmd[0] == "W":
                with open(cmd[1], "a") as file:
                    file.write("\n".join(tbuf))
                print(len(tbuf))
            elif cmd[0] == "P":
                prompt = "*"
            elif cmd[0].startswith("!"):
                print(execute(cmd[0][1:]).read().rstrip())
            elif cmd[0] == "wq":
                with open(cmd[1], "w") as file:
                    file.write("\n".join(tbuf))
                print(len(tbuf))
                break
            elif cmd[0].isnumeric():
                line = int(cmd[0]) - 1 if len(tbuf) > (int(cmd[0]) - 1) > -1 else 0
            elif cmd[0] == "n":
                print(line+1, tbuf[line])
            elif cmd[0] == ",n":
                print_tbuf_w_lines()
            elif cmd[0] == "pr":
                print_tbuf_raw(line)
            elif cmd[0] == ",pr":
                print_tbuf_raw(line, True)
            elif cmd[0] == "d":
                undo = list(tbuf) # keep last change
                delete(line)
                line = line - 1 if line > 1 else 1
            elif cmd[0] == "u":
                temp = list(tbuf) # redo feature
                tbuf = list(undo)
                undo = list(temp)
                line = len(tbuf)-1
            else:
                print("?")
        except IndexError:
            print("?")
        except FileNotFoundError:
            print(f"{cmd[1]} not found")

med()