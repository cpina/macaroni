import microbit

digits={}

digits['0'] ="""\
XX
XX
XX
XX
XX\
"""

digits['1'] = """\
 X
XX
 X
 X
 X\
"""

digits['2'] = """\
XX
 X
XX
X 
XX\
"""

digits['3'] = """\
XX
 X
X 
 X
XX\
"""

digits['4'] = """\
X 
X 
XX
 X
 X\
"""

digits['5'] = """\
XX
X 
XX
 X
XX\
"""

digits['6'] = """\
XX
X 
XX
XX
XX\
"""

digits['7'] = """\
XX
 X
 X
 X
 X\
"""

digits['8'] = """\
XX
XX
  
XX
XX\
"""

digits['9'] = """\
XX
XX
XX
 X
 X
"""

def show_gk_number(number):
    number=str(number)
    if len(number) == 2:
        show_gk_digit(number[0], 0)
        show_gk_digit(number[1], 3)
    else:
        show_gk_digit(number[0], 3)

def show_gk_digit(digit, col):
    for y,row in enumerate(digits[str(digit)].split("\n")):
        for x,c in enumerate(row):
            if c == 'X':
                brightness = 9
            else:
                brightness = 0

            microbit.display.set_pixel(x+col,y,brightness)

for i in range(0, 35):
    show_gk_number(i)

    microbit.sleep(1000)
    microbit.display.clear()
