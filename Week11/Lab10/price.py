class Price:
    def __init__(self, price=0.00):
        """ Construct a Price using two integers. """
        self.dollar = int(price // 1)
        self.cent = int((price - self.dollar) * 100)

    def __repr__(self):
        """ Return a string with the format “Class Price: $d.cc” """
        return "Class Price: ${}.{:02d}".format(self.dollar, self.cent)

    def __str__(self):
        """ Return a string with the format “$d.cc” """
        return "${}.{:02d}".format(self.dollar, self.cent)

    def __add__(self, other):
        """ Add two Price objects and return a Price object. """
        dollar = self.dollar + other.dollar
        cent = self.cent + other.cent

        if cent >= 100:
            cent -= 100
            dollar += 1

        price = dollar + (cent / 100)
        return Price(price)

    def __sub__(self, other):
        """ Subtract two Price objects and return a Price object. """
        dollar = self.dollar - other.dollar
        cent = self.cent - other.cent

        if cent < 0:
            cent += 100
            dollar -= 1

        price = dollar + (cent / 100)
        return Price(price)

    def __eq__(self, other):
        """ Return True if two Price objects are equal, False otherwise. """
        return self.dollar == other.dollar and self.cent == other.cent

    def __lt__(self, other):
        """ Return True if self is less than other, False otherwise. """
        if self.dollar < other.dollar:
            return True
        elif self.dollar == other.dollar and self.cent < other.cent:
            return True
        else:
            return False

    def __gt__(self, other):
        """ Return True if self is greater than other, False otherwise. """
        if self.dollar > other.dollar:
            return True
        elif self.dollar == other.dollar and self.cent > other.cent:
            return True
        else:
            return False
    
    def __le__(self, other):
        """ Return True if self is less than or equal to other, False otherwise. """
        if self.dollar < other.dollar:
            return True
        elif self.dollar == other.dollar and self.cent <= other.cent:
            return True
        else:
            return False

    def __ge__(self, other):
        """ Return True if self is greater than or equal to other, False otherwise. """
        if self.dollar > other.dollar:
            return True
        elif self.dollar == other.dollar and self.cent >= other.cent:
            return True
        else:
            return False