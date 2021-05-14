

class Course(object):
    """ Represents a college course """

    # Constructor
    def __init__(self, term=None, subject=None, course_number=None, section=None, name = None,
                 available = 0, capacity = 0):
        self.term = term                    #Su2021, Fa2021
        self.subject = subject              #CSC, MAT, CHM, PHY, ENG, HUM, BUS
        self.course_number = course_number  #210
        self.section = section              #0001
        self.name = name                    # Advanced Java Programming
        self.capacity = capacity            # 65
        self.available = available          # 59


    def __str__(self):
        return self.term + ' ' + self.subject +'-'+ self.course_number + '-'+self.section + ' ' + \
            self.available + '/' + self.capacity


    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other):
            return False
        # Courses could be retaken to get better grade. However no 2 classes w/ same
        # term-subject-course_number should ever be taken in the same term.
        if self.term != other.term or self.subject != other.subject or self.course_number \
            != other.course_number:
            return False
        return True

