import microbit

letters={}

letters['0'] ="""\
XX
XX
XX
XX
XX\
"""

letters['1'] = """\
 X
XX
 X
 X
 X\
"""

letters['2'] = """\
XX
 X
XX
X 
XX\
"""

letters['3'] = """\
XX
 X
X 
 X
XX\
"""

letters['4'] = """\
X 
X 
XX
 X
 X\
"""

letters['5'] = """\
XX
X 
XX
 X
XX\
"""

letters['6'] = """\
XX
X 
XX
XX
XX\
"""

letters['7'] = """\
XX
 X
 X
 X
 X\
"""

letters['8'] = """\
XX
XX
  
XX
XX\
"""

letters['9'] = """\
XX
XX
XX
 X
 X
"""

def show_gk_number(number):
    number=str(number)
    if len(number) == 2:
        show_gk_letter(number[0], 0)
        show_gk_letter(number[1], 3)
    else:
        show_gk_letter(number[0], 3)

def show_gk_letter(letter, col):
    for y,row in enumerate(letters[str(letter)].split("\n")):
        for x,c in enumerate(row):
            if c == 'X':
                brightness = 9
            else:
                brightness = 0

            microbit.display.set_pixel(x+col,y,brightness)

for i in range(0, 35):
    # show_letter(i,0)
    # show_letter(i+1,3)

    show_gk_number(i)

    microbit.sleep(1000)
    microbit.display.clear()
