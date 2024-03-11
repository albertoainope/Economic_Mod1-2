class Point: #Programmers use upper case
    def __init__(self, x, y):
        """
        Init method that initializes the point with X and Y
        :param x: X coordinate value
        :param y: Y coordinate value
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        How to print this point?
        :return:
        """
        return f"<x={self.x}, y={self.y}>"
    #We can put attributes inside the class
    #init method tells us how to initialize the class, first parameter is self
    def __repr__(self):
        """
        How to print if in a list?
        :return:
        """
        return self.__str__()
    def distance_origin(self):
        """
        Distance from origin
        :return:
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __gt__(self, other):
        """
        How to compare 2 points?
        :param other: the other point we are comparing against
        :return:
        """
        my_size = self.distance_origin()
        their_size = other.distance_origin()
        return my_size > their_size

    def __eq__(self, other):
        """
        How to compare with ==?
        :param other: the other point we are comparing against
        :return:
        """
        return self.distance_origin() == other.distance_origin()

if __name__ == "__main__":
    #use for loop to instantiate 5 points
    import random
    points = []
    for i in range(5):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        points.append(Point(x, y))

    for _ in range(5):
        points.append(Point(random.randint(0, 100), random.randint(0, 100)))

    for point in points:
        print(point) #it prints the ID of the object

    print(points) #Here it iterates and calls point repr

    # repr --> representation of the object

    a = Point(3, 4)
    b = Point(12,5)
    c = Point(5, 12)
    print(b < a)
    print(a == c) #It calls the __gt__ method __gt__
    points.sort()
    print(f"The biggest point is: {points[-1]} and the smallest point is: {points[0]}")

    #Inheritance

