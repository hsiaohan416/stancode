"""
File: draw_line
Name:Sharon
-------------------------
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10
window = GWindow()
click_times = 0
x1 = 0
y1 = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(click)


def click(event):
    global click_times, x1, y1
    click_times += 1
    if click_times % 2 != 0:               # After clicking the first time, the program will remember our clicking spot
                                           # as the global variable (x1, y1) and draw a circle on the spot.
        point_1 = GOval(SIZE, SIZE)
        window.add(point_1, event.x-SIZE/2, event.y-SIZE/2)
        x1 = event.x
        y1 = event.y
    if click_times % 2 == 0:                    # When the second click was clicked, the system will remove the previous
                                                # circle, and draw a line from (x1, y1) to the second clicking spot.
        point_1 = window.get_object_at(x1, y1)
        window.remove(point_1)
        line = GLine(x1, y1, event.x, event.y)
        window.add(line)


if __name__ == "__main__":
    main()
