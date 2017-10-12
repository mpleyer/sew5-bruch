class Bruch(object):
    """
    Class that tries to represent the behaviour of fractions
    mainly with operators and other private functions
    """

    def __init__(self, zaehler, nenner=1):
        """
        Constructor for fractions
        :param zaehler: The numerator of the fraction
        :param nenner: The denominator of the fraction
        """
        if type(zaehler) is Bruch:
            self.zaehler = zaehler.zaehler
            self.nenner = zaehler.nenner
        else:
            if type(zaehler) is not int or type(nenner) is not int:
                raise TypeError

            if nenner == 0:
                raise ZeroDivisionError

            self.zaehler = zaehler
            self.nenner = nenner

    def __eq__(self, other):
        """
        Compares two fractions based on their float-value
        :param other: The second fraction to compare
        :return: True if both are equal in their float-value, False otherwise
        """
        return float(self) == float(other)


    def __add__(self, other):
        """
        Add 2 fractions together or
        add a fraction to an int

        :param other: fraction or number to add
        :return: new fraction with the result of the addition
        """
        if type(other) is not Bruch:
            if type(other) is int:
                other = Bruch(other, 1)
            else:
                raise TypeError
        z1 = self.zaehler * other.nenner
        z2 = other.zaehler * self.nenner
        n = self.nenner * other.nenner
        return Bruch(z1 + z2, n)

    def __iadd__(self, other):
        """
        Incremental addition of fractions using +=
        :param other: fraction or number to add
        :return: new fraction with the result of the addition
        """
        return self + other

    def __radd__(self, other):
        """
        Reverse addition for fractions: int + fraction
        :param other: See param of :func:`__add__`
        :return: See return of :func:`__add__`
        """
        return self.__add__(other)

    def __float__(self):
        """
        Computes the float-value of a fraction. Basically a division between numerator and denominator
        :return: The float-value of the fraction
        """
        return float(self.zaehler) / float(self.nenner)

    def __abs__(self):
        """
        Computes the absolute value of a fraction. Always positive.
        :return: The absolute value of a fraction
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __int__(self):
        """
        Show fraction as rounded float
        :return: integer with rounded n/d
        """
        return round(float(self))

    def __invert__(self):
        """
        Inverts the fraction. Swaps numerator with denominator
        :return: The inverted fraction
        """
        return Bruch(self.nenner, self.zaehler)

    def __neg__(self):
        """
        Negates the fraction. Negates the numerator
        :return: The negated fraction
        """
        return Bruch(-self.zaehler, self.nenner)

    def __pow__(self, power, modulo=None):
        """
        Takes the fraction to the given power.
        :param power: Specifies how often to multiply the fraction with itself
        :param modulo: None
        :return: The fraction taken to the given power
        """
        if type(power) == float:
            raise TypeError
        return Bruch(self.zaehler ** power, self.nenner ** power)

    @staticmethod
    def __makeBruch(value):
        """
        Static method to create a fraction with an int
        :param value: of the nominator of the fraction
        :return: the created fraction
        """
        if type(value) is not int:
            raise TypeError
        return Bruch(value, 1)

    def __truediv__(self, other):
        """
        Divides the fraction with another one or an int
        :param other: The second fraction or an int which act as divisor
        :return: new fraction with the result of the division
        """
        if type(other) == int:
            if self == 0:
                raise ZeroDivisionError
            return float(self)*float(1/other)
        elif type(other) == Bruch:
            return float(self)*float(~other)
        else:
            raise TypeError

    def __itruediv__(self, other):
        """
        Incremental division for fractions: /=
        :param other: The second fraction or an int which act as divisor
        :return: new fraction with the result of the division
        """
        return self / other

    def __rtruediv__(self, other):
        """
        Reverse division for fractions: int / fraction
        :param other: The second fraction or an int which act as divisor
        :return: new fraction with the result of the division
        """
        return self.__truediv__(other)

    def __mul__(self, other):
        """
        Multiplies the fraction with another one or an int
        :param other: The second fraction or an int which acts as factor
        :return: The product - Result of the multiplication
        """
        if type(other) == int:
            return Bruch(self.zaehler*other, self.nenner)
        elif type(other) == Bruch:
            return Bruch(self.zaehler * other.zaehler, self.nenner * other.nenner)
        else:
            raise TypeError

    def __ge__(self, other):
        """
        Compares two fractions with >=
        :param other: The second fraction
        :return: True if float-value of self is greater or equal to float-value of other
        """
        return float(self) >= float(other)

    def __gt__(self, other):
        """
        Compares two fractions with >
        :param other: The second fraction
        :return: True if float-value of self is greater than float-value of other
        """
        return float(self) > float(other)

    def __le__(self, other):
        """
        Compares two fractions with <=
        :param other: The second fraction
        :return: True if float-value of self is lesser or equal to float-value of other
        """
        return float(self) <= float(other)

    def __lt__(self, other):
        """
        Compares two fractions with <
        :param other: The second fraction
        :return: True if float-value of self is less than float-value of other
        """
        return float(self) < float(other)

    def __imul__(self, other):
        """
        Incremental multiplication for fractions: \*=
        :param other: See param of :func:`__mul__`
        :return: See return of :func:`__mul__`
        """
        return self.__mul__(other)

    def __rmul__(self, other):
        """
        Reverse multiplication for fractions: int * fraction
        :param other: See param of :func:`__mul__`
        :return: See return of :func:`__mul__`
        """
        return self.__mul__(other)

    def __sub__(self, other):
        """
        Subtracts a fraction or an int from this one
        :param other: The second fraction or an int which acts as minuend
        :return: The difference - Result of the subtraction
        """
        if type(other) == int:
            return Bruch((self.zaehler - other * self.nenner), self.nenner)
        elif type(other) == Bruch:
            return Bruch((self.zaehler * other.nenner - other.zaehler * self.nenner), (self.nenner * other.nenner))
        else:
            raise TypeError

    def __isub__(self, other):
        """
        Incremental subtraction for fractions: \-\-=
        :param other: See param of :func:`__sub__`
        :return: See return of :func:`__sub__`
        """
        return self.__sub__(other)

    def __rsub__(self, other):
        """
        Reverse subtraction for fractions: int - fraction
        :param other: The subtrahend - has to be transformed to a fraction in order to work properly
        :return: See return of :func:`__sub__`
                """
        other = Bruch(other)
        return other.__sub__(self)

    def __str__(self):
        """
        Show fraction as string.
        :return: "(Numerator/Denominator)"
        """
        if (self.zaehler < 0) and (self.nenner < 0):
            return "("+str(self.zaehler * -1) + "/" + str(self.nenner * -1) + ")"
        elif self.nenner == 1:
            return "("+str(self.zaehler) + ")"
        return "("+str(self.zaehler) + "/" + str(self.nenner) + ")"


    def __iter__(self):
        """
        Iterates through a fraction
        :return: Iterator of the tuple: (numerator, denominator)
        """
        return (self.zaehler, self.nenner).__iter__()