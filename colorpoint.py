from classexample import Point

#Just to test that Point was imported as expected
#a = Point(5, 5)
#print(a)

class ColorPoint(Point):
    #this is a class that inherits from Point
    COLORS = ["red", "green", "blue", "yellow", "black", "cyan"]
    def __init__(self, x, y, color):
        #self.x = x
        #self.y = y
        super().__init__(x, y) #Calling the parent init method
        if color in self.COLORS:
            self.color = color
        else:
            raise Exception(f"This is an unsupported color. Allowed colors are {self.COLORS}")

    @property
    def distance_origin(self):
        """
        Distance from origin
        :return:
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5
    @classmethod
    def add_extra_color(cls, color):
        """
        Add a new color to the list of colors
        :param color: the name of the color to be added
        :return:
        """
        cls.COLORS.append(color)


    def __str__(self):
        return f"{self.color}<{self.x}, {self.y}>"

#import random
#lets do 5 random color points
#color_points = []
#for _ in range(5):
#    color_point = ColorPoint(random.randint(1,100),
#                             random.randint(1,100),
#                             random.choice(colors))
#    color_points.append(color_point)

#print(color_points)
if __name__ == "__main__":
    #we added thi sif to not show all the below lines when importing into advanced point
    red_point = ColorPoint(10, 10, "red")
    ColorPoint.add_extra_color("orange")
    orange_point = ColorPoint(20, 20, "orange")
    red_point.x = 30
    #print(f"{red_point} has distance to origin = {red_point.distance_origin()}") before it was a property
    print(f"{red_point} has distance to origin = {red_point.distance_origin}") #after it is a property