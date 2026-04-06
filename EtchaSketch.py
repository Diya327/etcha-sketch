from tkinter import*
import random

#---variables for screen---
canvas_height = int(input("How tall do you want your screen? (up to 850) "))
canvas_width = int(input("How wide do you want your screen? (up to 2000) "))
canvas_colour = 'black'

p1_x = canvas_width/4
p1_y = canvas_height/4
p2_x = (canvas_width/4)*3
p2_y = canvas_height/4
p3_x = canvas_width/4
p3_y = (canvas_height/4)*3
p4_x = (canvas_width/4)*3
p4_y = (canvas_height/4)*3

colours = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "pink"]
current_colour = "red"
i = 0# Initial color

# Function to change line color every 2 seconds
def change_colour():
    global i
    global current_colour
    current_colour = colours[i]
    if i == 6:
        i = 0
    else:
        i = i + 1
    canvas.after(1000, change_colour)

line_width = 5
line_length = 5

# controls moving up
def move_N(self):
    global p1_y
    canvas.create_line(p1_x, p1_y, p1_x, (p1_y-line_length), width = line_width, fill=current_colour)
    p1_y = p1_y-line_length
    global p2_y
    canvas.create_line(p2_x, p2_y, p2_x, (p2_y-line_length), width = line_width, fill=current_colour)
    p2_y = p2_y-line_length
    global p3_y
    canvas.create_line(p3_x, (p3_y+line_length), p3_x, p3_y, width = line_width, fill=current_colour)
    p3_y = p3_y+line_length
    global p4_y
    canvas.create_line(p4_x, (p4_y+line_length), p4_x, p4_y, width = line_width, fill=current_colour)
    p4_y = p4_y+line_length

# controls moving down
def move_S(self):
    global p1_y
    canvas.create_line(p1_x, (p1_y+line_length), p1_x, p1_y, width = line_width, fill=current_colour)
    p1_y = p1_y+line_length
    global p2_y
    canvas.create_line(p2_x, (p2_y+line_length), p2_x, p2_y, width = line_width, fill=current_colour)
    p2_y = p2_y+line_length
    global p3_y
    canvas.create_line(p3_x, p3_y, p3_x, (p3_y-line_length), width = line_width, fill=current_colour)
    p3_y = p3_y-line_length
    global p4_y
    canvas.create_line(p4_x, p4_y, p4_x, (p4_y-line_length), width = line_width, fill=current_colour)
    p4_y = p4_y-line_length

# controls moving right
def move_E(self):
    global p1_x
    canvas.create_line((p1_x+line_length), p1_y, p1_x, p1_y, width = line_width, fill=current_colour)
    p1_x = p1_x+line_length
    global p2_x
    canvas.create_line(p2_x, p2_y, (p2_x-line_length), p2_y, width = line_width, fill=current_colour)
    p2_x = p2_x-line_length
    global p3_x
    canvas.create_line((p3_x+line_length), p3_y, p3_x, p3_y, width = line_width, fill=current_colour)
    p3_x = p3_x+line_length
    global p4_x
    canvas.create_line(p4_x, p4_y, (p4_x-line_length), p4_y, width = line_width, fill=current_colour)
    p4_x = p4_x-line_length
    
# controls moving left
def move_W(self):
    global p1_x
    canvas.create_line(p1_x, p1_y, (p1_x-line_length), p1_y, width = line_width, fill=current_colour)
    p1_x = p1_x-line_length
    global p2_x
    canvas.create_line((p2_x+line_length), p2_y, p2_x, p2_y, width = line_width, fill=current_colour)
    p2_x = p2_x+line_length
    global p3_x
    canvas.create_line(p3_x, p3_y, (p3_x-line_length), p3_y, width = line_width, fill=current_colour)
    p3_x = p3_x-line_length
    global p4_x
    canvas.create_line((p4_x+line_length), p4_y, p4_x, p4_y, width = line_width, fill=current_colour)
    p4_x = p4_x+line_length

#delete everything
def erase(self):
    canvas.delete(ALL)

   
#---mainloop---
window = Tk()
window.title('Etchsketch')
canvas = Canvas(bg=canvas_colour, height = canvas_height, width = canvas_width, highlightthickness = 0)
canvas.pack()

change_colour()

#---bind controls---
window.bind('<Up>', move_N)
window.bind('<Down>', move_S)
window.bind('<Right>', move_E)
window.bind('<Left>', move_W)
window.bind("<BackSpace>", erase)

window.mainloop()
