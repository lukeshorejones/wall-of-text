import math

def char_input(text, a, b):
    result = input(text).upper()
    if result != a.upper() and result != b.upper():
        print(f"Please enter {a} or {b}.")
        result = char_input(text, a, b)
    return result

def int_input(text):
    result = input(text)
    if not result.isdigit():
        print("Please enter an integer value.")
        result = int_input(text)
    return int(result)

def print_text(chars, line_length):
    start = int_input("\nEnter starting line to print:\n> ")
    lines = int_input("\nEnter number of lines to print:\n> ")
    print("")

    curr = start - 1
    line = [None] * line_length
    reached_end = False
    for i in range(lines):
        for j in range(line_length):
            line[j] = (curr // len(chars) ** j) % len(chars)
            line[j] = chars[line[j]]

        print(''.join(line))
        curr += 1

        if line == [chars[-1]] * line_length:
            lines = i + 1
            reached_end = True
            break

    if lines > 1:
        s = "s"
        line_range = f"s {start}-{str(start + lines - 1)}"
    else:
        s = ""
        line_range = f" {start}"
    
    print(f"\nSuccessfully printed {lines} line{s} of the wall of text (line{line_range}).")
    if reached_end:
        print("Reached the end of the wall of text.")

def print_num(chars, line_length):
    search = list(input("\nEnter string to search for:\n> "))
    search += [' '] * (line_length - len(search))

    line_no = 1 
    for i in range(line_length):
        line_no += chars.index(search[i]) * len(chars) ** i
    
    print(f"\nYour search is line:\n{line_no}")

def run():
    ch = list(''' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=[];'#\,./!"£$%^&*()_+{}:@~|<>?''')
    l = 140
    
    print(f"\n----------\n\nThe Wall of Text contains every {l}-character line of text that can be made from its set of {len(ch)} characters.\n\nThe line count of the Wall of Text is:\n{95**140}")
    
    o = char_input("\nSelect operation. Enter A or B:\nA) Print the Wall of Text.\nB) Search the Wall of Text.\n> ", "A", "B")
    if o == 'A':
        print_text(ch, l)
    else:
        print_num(ch, l)

    cont = char_input("\nContinue? (y/n):\n> ", "y", "n")
    if cont == "Y":
        run()

run()
