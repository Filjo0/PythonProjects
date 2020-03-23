"""
Chapter 9.
1. Add three methods to the Student class that compare two Student objects. One
method should test for equality. A second method should test for less than. The
third method should test for greater than or equal to. In each case, the method
returns the result of the comparison of the two students’
"""


class Student(object):

    def __init__(self, name, number):
        """Constructor creates a Student with the given
        name and number of scores and sets all scores
        to 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the Ch9's name."""
        return self.name

    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]

    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)

    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def __str__(self):
        """Returns the string representation of the
        Ch9."""
        return "Name: " + self.name + "\nScores: " + \
               " ".join(map(str, self.scores))

    def equal_name(self, other):
        if not isinstance(other, Student):
            return NotImplemented

        return self.name == other.name

    def less_than_name(self, other):
        if not isinstance(other, Student):
            return NotImplemented

        return self.name <= other.name

    def greater_than_name(self, other):
        if not isinstance(other, Student):
            return NotImplemented

        return self.name >= other.name
