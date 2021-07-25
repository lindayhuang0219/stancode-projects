"""
File: sierpinski.py
Name: Linda
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	The sierpinski triangle is a fractal attractive fixed set with the overall shape of an equilateral triangle,
	subdivided recursively into smaller equilateral triangles.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	prints the Sierpinski triangle on GWindow
	:param order: Controls the order of Sierpinski Triangle
	:param length: The length of Sierpinski Triangle
	:param upper_left_x: The upper left x coordinate of Sierpinski Triangle
	:param upper_left_y: The upper left y coordinate of Sierpinski Triangle
	"""
	sierpinski_triangle_helper(order, length, upper_left_x, upper_left_y)


def sierpinski_triangle_helper(order, length, upper_left_x, upper_left_y):
	"""
	:param order: Controls the order of Sierpinski Triangle
	:param length: The length of Sierpinski Triangle
	:param upper_left_x: The upper left x coordinate of Sierpinski Triangle
	:param upper_left_y: The upper left y coordinate of Sierpinski Triangle
	:return: prints the Sierpinski triangle on GWindow
	"""
	pause(10)
	if order > 0 :
		draw_triangle(length, upper_left_x, upper_left_y)
		sierpinski_triangle(order-1,length/2,upper_left_x,upper_left_y)
		sierpinski_triangle(order-1,length/2,upper_left_x+length/2,upper_left_y)
		sierpinski_triangle(order-1,length/2,upper_left_x+length/4,upper_left_y+0.433*length)
	else:
		return


def draw_triangle(length,upper_left_x, upper_left_y):
	"""
	draw the triangle on GWindow
	:param length: The length of Triangle
	:param upper_left_x: The upper left x coordinate of Triangle
	:param upper_left_y: The upper left y coordinate of Triangle
	"""

	upper = GLine(upper_left_x, upper_left_y, upper_left_x+length, upper_left_y)
	window.add(upper)
	left = GLine(upper_left_x, upper_left_y, upper_left_x+0.5*length, upper_left_y+0.866*length)
	window.add(left)
	right = GLine(upper_left_x+length, upper_left_y, upper_left_x+0.5*length, upper_left_y+0.866*length)
	window.add(right)


if __name__ == '__main__':
	main()