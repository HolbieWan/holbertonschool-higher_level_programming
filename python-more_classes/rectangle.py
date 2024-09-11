#/usr/bin/python3
"""Creating a class that difines a rectangle"""

class Rectangle:
  """Class that defines a rectangle with private instance attributes"""
  number_of_instances = 0
  print_symbol = "#"

  def __init__(self, width=0, height=0):
    """ to innitialize an instance of the class Rectangle"""
    self.width = width
    self.height = height
    Rectangle.number_of_instances += 1

  @property
  def width(self):
    """ to retieve the width of a rectangle"""
    return self.__width
  
  @width.setter
  def width(self, value):
    """ to set the width of a rectangle"""
    if not isinstance(value, int):
      raise TypeError("width must be an integer")
    if value < 0:
      raise ValueError("width must be >= 0")
    self.__width = value

  @property
  def height(self):
    """ to retrieve the heigth of a rectangle"""
    return self.__height
  
  @height.setter
  def height(self, value):
    """ to set the width of a rectangle"""
    if not isinstance(value, int):
      raise TypeError("width must be an integer")
    if value < 0:
      raise ValueError("width must be >= 0")
    self.__height = value

  def area(self):
    """ that return the area of a rectangle instance"""
    return self.__width * self.__height

  def perimeter(self):
    """ that returns the perimeter of a rectangle instance"""
    if self.__width == 0 or self.__height == 0:
      return 0
    else:
      return (self.__width * 2) + (self.__height * 2)

  def print_rectangle(self):
    """ that prints a rectangle instance"""
    if self.width == 0 or self.height == 0:
      return ("")
    for i in range(self.height):
      for j in range(self.width):
        print("#", end="")
      print()

  def __str__(self):
    """Method that returns the printable string representation of the Rectangle."""
    str_rectangle = ""
    if self.width == 0 or self.height == 0:
      return ("")
    
    for i in range(self.height):
      str_rectangle += str(self.print_symbol) * self.width
      if i < self.height - 1:
        str_rectangle += "\n"

    return str_rectangle
  
  def __repr__(self) -> str:
    """Method that returns a string that recreates a new instance of Rectangle by using eval()"""
    return f"Rectangle({self.width}, {self.height})"

  def __del__(self):
    """Method that deletes an instance of Rectangle displaying a message """
    print("Bye rectangle...")
    self.number_of_instances -= 1

  @staticmethod
  def bigger_or_equal(rect_1, rect_2):
    """Static method"""
    if not isinstance(rect_1, Rectangle):
      raise TypeError("rect_1 must be an instance of Rectangle")
    if not isinstance(rect_2, Rectangle):
      raise TypeError("rect_2 must be an instance of Rectangle")
    if rect_1.area() == rect_2.area():
      return rect_1
    if rect_1.area() > rect_2.area():
      return rect_1
    
  @classmethod
  def square(cls, size=0):
    cls.width = cls.height = size
    return cls()
    
# rectangle_1 = Rectangle(4, 2)
# rectangle_1.print_rectangle()