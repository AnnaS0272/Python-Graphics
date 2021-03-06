


import tkinter
import time
import random

CANVAS_SIZE = 800
N_ROWS = 8
N_COLS = 8
SIZE = CANVAS_SIZE / N_ROWS - 1

def main():
    canvas = make_canvas(CANVAS_SIZE, CANVAS_SIZE, "Python Web")
    for row in range(N_ROWS):
        for col in range(N_COLS):
            draw_square(canvas, row, col)
    canvas.mainloop()

def draw_square(canvas, row, col):
    x = col * SIZE
    y = row * SIZE
    canvas.create_rectangle(x, y, x + SIZE, y + SIZE, outline="#000000", fill="#000000")
    sketch_pattern(canvas, x, y)

def sketch_pattern(canvas, x, y):
    # This loop will draw the pattern. This pattern is an optical illusion when straight lines are drawn from y to x
    # coordinates one by one at a set interval creating a perception of a curved space.
    for i in range(100):
        if i % 5 == 0:
            canvas.create_line(x, y + SIZE - i, x + i, y, fill="#777777")
            canvas.create_line(x + i, y, x + SIZE, y + i, fill="#F9F9F3")
            canvas.create_line(x + i, y + SIZE, x + SIZE, y + SIZE - i, fill="#FFFFFF")
            canvas.create_line(x, y + i, x + i, y + SIZE, fill="#F2F3F4")

######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height, title=None):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    objects = {}
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # add this so (0, 0) works correctly
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    return canvas


if __name__ == '__main__':
    main()
