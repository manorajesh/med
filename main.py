from os import path, popen

tbuf = [] # text buffer

def read(file):
    global tbuf
    text = ""
    if file.startswith("!"):
        file = execute(file[1:])

    try:
        with open(file, "r") as f:
            text = f.read().splitlines()
    except (FileNotFoundError, TypeError):
        try:
            with file as f:
                text = f.read().splitlines()
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

    for val in text[:-3].split("\n")[::-1]:
        tbuf.insert(line+1, val)

def insert(line):
    global tbuf
    text = ""

    while not text.endswith("\n.\n"):
        text += input()
        text += "\n"

    for val in text[:-3].split("\n")[::-1]:
        tbuf.insert(line, val)

def change(line):
    global tbuf
    text = ""

    while not text.endswith("\n.\n"):
        text += input()
        text += "\n"

    tbuf.pop(line)
    for val in text[:-3].split("\n")[::-1]:
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
        print(f"{line+1}\t{val}")

def replace(line, words, all=False):
    global tbuf
    old, new = words

    if all:
        tbuf = "\n".join(tbuf).replace(old, new).split("\n")
    else:
        tbuf[line] = tbuf[line].replace(old, new)

def execute(command):
    return popen(command)

def delete(line):
    global tbuf
    tbuf.pop(line)

def isValidLine(list, index, default):
    global tbuf
    try:
        if len(tbuf) >= int(list[index]) > 0:
            return int(list[index])-1
        else:
            return default
    except (IndexError, ValueError):
        return default

def splitReplace(string):
    text = string[0].lstrip(',s')
    words = [""]
    c = 0

    if text.startswith("/") and text.endswith("/"):
        for letter in text[1:-1]:
            if letter == "/" and c < 1:
                words.append("")
                c += 1
            else:
                words[c] += letter
    return words

def split(string, maxAllowed):
    try:
        if string.index(" ") > maxAllowed:
            return [string]
        else:
            return string.split()    
    except ValueError:
        return string.split()

def med(file="", prompt=""):
    global tbuf
    
    if path.isfile(file):
        with open(file, "r") as f:
            tbuf = f.read().splitlines()
            print(path.getsize(file))

    line = len(tbuf)-1
    undo = [] # undo buffer
    help = "?"
    while (cmd_input := input(prompt)) != "q":
        try:
            cmd = split(cmd_input, 1)
            
            if cmd[0] == "r":
                undo = list(tbuf) # keep last change
                read(cmd[1])
                line = len(tbuf)-1
            elif cmd[0] == "a":
                undo = list(tbuf) # keep last change
                append(isValidLine(cmd, 1, line))
                line += 1
            elif cmd[0] == "i":
                undo = list(tbuf) # keep last change
                insert(isValidLine(cmd, 1, line))
                line = line - 1 if line > 0 else 0
            elif cmd[0] == "c":
                undo = list(tbuf) # keep last change
                change(isValidLine(cmd, 1, line))
            elif cmd[0] == "p":
                print_tbuf(isValidLine(cmd, 1, line))
            elif cmd[0] == ",p":
                print_tbuf(line, True)
            elif cmd[0].startswith("s"):
                undo = list(tbuf) # keep last change
                replace(line, splitReplace(cmd))
            elif cmd[0].startswith(",s"):
                undo = list(tbuf) # keep last change
                replace(line, splitReplace(cmd), True)
            elif cmd[0] == "w":
                with open(cmd[1], "w") as file:
                    file.write("\n".join(tbuf))
                print(len(tbuf))
            elif cmd[0] == "W":
                with open(cmd[1], "a") as file:
                    file.write("\n".join(tbuf))
                print(len(tbuf))
            elif cmd[0] == "P":
                prompt = "*" if len(cmd) < 2 else cmd[1]
            elif cmd[0].startswith("!"):
                print(execute(cmd[0][1:]).read().rstrip())
            elif cmd[0] == "wq":
                with open(cmd[1], "w") as file:
                    file.write("\n".join(tbuf))
                print(len(tbuf))
                break
            elif cmd[0].isnumeric():
                line = int(cmd[0]) - 1 if len(tbuf) > (int(cmd[0]) - 1) > -1 else 0
                print(tbuf[line])
            elif cmd[0] == "n":
                print(f"{isValidLine(cmd, 1, line)+1}\t{tbuf[isValidLine(cmd, 1, line)]}")
            elif cmd[0] == ",n":
                print_tbuf_w_lines()
            elif cmd[0] == "pr":
                print_tbuf_raw(line)
            elif cmd[0] == ",pr":
                print_tbuf_raw(line, True)
            elif cmd[0] == "d":
                undo = list(tbuf) # keep last change
                delete(isValidLine(cmd, 1, line))
                line = line - 1 if line > 1 else 1
            elif cmd[0] == "u":
                temp = list(tbuf) # redo feature
                tbuf = list(undo)
                undo = list(temp)
                del temp
                line = len(tbuf)-1
            elif cmd[0] == "h":
                print(help)
            elif cmd[0] == "y":
                copy = tbuf[isValidLine(cmd, 1, line)]
            elif cmd[0] == "x":
                undo = list(tbuf) # keep last change
                copy = tbuf[isValidLine(cmd, 1, line)]
                delete(isValidLine(cmd, 1, line))
                line = line - 1 if line > 1 else 1
            elif cmd[0] == "m":
                tbuf.insert(isValidLine(cmd, 1, line), copy)
            else:
                print("?")
                help = 'invalid command'
        except IndexError:
            print("?")
            help = 'invalid address'
        except TypeError:
            print("?")
            help = f'unexpected address for {cmd[0]}'
        except FileNotFoundError:
            print("?")
            help = f'"{cmd[1]}" not found'
        except ValueError:
            print("?")
            help = "not enough arguments for replace"
        except UnboundLocalError:
            print("?")
            help = "copy buffer is empty"

if __name__ == "__main__":
    med()