"""
    @project: stuPython
    @Author：Murk
    @file： 4.6 match语句.py
    @date：2024/1/18 21:07
    @Desc: 
"""

""" 语法一："""


def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 401 | 403 | 404:
            return "Not allowed"
        case _:
            return "Something's wrong with the internet"


print(http_error(200))

""" 语法二："""
# point is an (x, y) tuple
x = 1
y = 2
match (x, y):
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

""" 语法三： """


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")


var = 1
Point(1, var)
Point(1, y=var)
Point(x=1, y=var)
Point(y=var, x=1)
where_is(Point(var, 0))

print('----------------------- ')

from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
