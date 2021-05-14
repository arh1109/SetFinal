""" Script that reads course_list.txt, creates a Course obj from each line
    and store the Courses in a Set"""
from course import Course
from linkedset import LinkedSet

""" Reads a txt list of Courses and adds them to a Set. Returns a Set of Courses. 
    Txt file should have values in order of 
    [term] [section] [available] [capacity] [subject] [course_number] [title]"""
def readAndCreateSet():
    f = open('course-list.txt', 'r')
    set = LinkedSet()
    for line in f:
        course = None
        if line != '\n':
            # Split into two halves
            splitted = line.split('\'')
            # splitted[1] has course name which spaces
            # and cannot be parsed normally.
            name = splitted[1]

            splitAgain = splitted[0].split(' ')
            term = splitAgain[0]
            section = splitAgain[1]
            available = splitAgain[2]
            capacity = splitAgain[3]
            subject = splitAgain[4]
            course_number = splitAgain[5]
            course = Course(term, subject, course_number, section, name, available, capacity)
            set.add(course)
    #print(set)
    return set
    f.close()



setty = readAndCreateSet()



