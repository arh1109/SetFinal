"""
create a simple program to do course registration. The user can add courses, drop courses and list courses he is
enrolled in. A set will be used to store the data. The members of the set are the courses the user are enrolled in.
Set is chosen because a student should not enroll in the same course twice, and the courses are not in any order.
The node data for the LinkedSet will usually hold Course objects found in course.py
"""

from linkedset import LinkedSet
from load_course_list import readAndCreateSet

""" Helper Function that processes user input for addCourse()"""
def processSemesterTerm(s3):
    print('Enter a semester to register for: ')
    # Get the user input value
    a_term = input("For Su2021 enter [1]: \n"
                   "For Fa2021 enter [2]: \n")
    # Only two choices for term so don't need a semester_list and for loop
    # filter out nonmatching semester terms
    if a_term == '1':
        # Remove all of the Su2021 in the course list
        for i in s3:
            if i.term == 'Fa2021':
                s3.remove(i)
    elif a_term == '2':
        # Remove all of the Su2021 in the course list
        for i in s3:
            if i.term == 'Su2021':
                s3.remove(i)
    else:
        s3.clear()
    return s3

""" Helper Function that processes user input for addCourse()"""
def processSubject(s3, temporary_subject_set):
    print('Enter a subject to register for: ')
    # Gets the subject from the course catalong. Append the subjects to a temporary LinkedSet
    for i in s3:
        temporary_subject_set.add(i.subject)
    j = 0
    subject_list = list()

    # Loop through the temporary subject set and append it to the list called subject_list
    for i in temporary_subject_set:
        j += 1
        subject_list.append(i)
        print('To choose ' + i + ' select: [' + str(j) + ']')
    
    # Get user input for the subject choice
    subject_choice = input('Enter choice here: ')

    # Try to get the integer value of the input. If the user input is not a number, end 
    try:
        int_choice = int(subject_choice)
    except:
        s3.clear()
        return s3

    # End if the subject choice is not within the subject list
    if int(subject_choice) > len(subject_list) or int(subject_choice) < 1:
        s3.clear()
        return s3

    # Get actual subject value
    subject = subject_list[int(subject_choice) - 1]

    # filter out nonmatching subjects
    for i in s3:
        if i.subject != subject:
            s3.remove(i)
    return s3

""" Helper Function that processes user input for addCourse()"""
def processCourseNumber(s3, temporary_course_number):
    # Append the course number to a temporary LinkedSet for storage keeping
    for i in s3:
        temporary_course_number.add(i.course_number)
    print('Course numbers to register for')
    j = 0
    course_number_list = list()

    # Loop through the temporary course number and append it to the list called course_number_list
    for i in temporary_course_number:
        j += 1
        course_number_list.append(i)
        print('To choose ' + i + ' select: [' + str(j) + ']')

    # Get user input for the course number
    course_choice = input('Enter choice here: ')

    # Try to get the integer value of the input. If the user input is not a number, end 
    try:
        int_choice = int(course_choice)
    except:
        s3.clear()
        return s3
    
    # End if the subject choice is not within the subject list
    if int(course_choice) > len(course_number_list) or int(course_choice) < 1:
        s3.clear()
        return s3
    
    # Get actual course number
    course_num = course_number_list[int(course_choice) - 1]

    # filter out nonmatching course numbers
    for i in s3:
        if i.course_number != course_num:
            s3.remove(i)
    return s3

""" Helper Function that processes user input for addCourse()"""
def processSectionNumber(s3, temporary_section_number):
    # Append the section number to a temporary LinkedSet for storage keeping
    for i in s3:
        temporary_section_number.add(i.section)
    print('Section numbers to register for: ')
    j = 0
    section_number_list = list()

    # Loop through the temporary section number and append it to the list called section_number_list
    for i in temporary_section_number:
        j += 1
        section_number_list.append(i)
        print('To choose ' + i + ' select: [' + str(j) + ']')

    # Get user input for the section number
    section_choice = input('Enter choice here: ')

    # Try to get the integer value of the input. If the user input is not a number, end 
    try:
        int_choice = int(section_choice)
    except:
        s3.clear()
        return s3
    
    # End if the subject number is not within the subject list
    if int(section_choice) > len(section_number_list) or int(section_choice) < 1:
        s3.clear()
        return s3

    # Get actual section number
    section_num = section_number_list[int(section_choice) - 1]

    # filter out nonmatching section numbers, only one element should remain
    for i in s3:
        if i.section != section_num:
            s3.remove(i)
    return s3


""" Section of code responsible for adding classes
    Parameters: student's set of registered courses
    and the set of courses offered by the university."""
def addCourse(s, courseCatalogSet):
    a_class = '0'
    b_flag = True
    
    while a_class != 'n' and b_flag == True:

        print("\nAdd a Course to Plan")
        """ Create temporary variables stored below. s3 starts as a clone of courseCatalogSet.
            It is gradually filtered by removing courses that do not match user's choices. 
            
            Temporary sets are created and used primarily for displaying data to the user.
            Temporary lists will be used for indexing and matching user choices to course node objects.
            Also new entries are checked to prevent student from adding two identical subject - course numbers."""
        s3 = courseCatalogSet.clone()
        temporary_subject_set = LinkedSet()
        temporary_course_number = LinkedSet()
        temporary_section_number = LinkedSet()

        # Process semester term
        s3 = processSemesterTerm(s3)
        print()

        # if there are no classes that were processed for the semester term, exit and print out that
        # input is not valid
        if len(s3) == 0:    #
            print('Invalid Input')
            b_flag = False
            continue

        # Process subject
        s3 = processSubject(s3, temporary_subject_set)
        print()

        # if the subject is not valid, exit and print out that the input is not valid
        if len(s3) == 0:
            print('Invalid Input')
            b_flag = False
            continue

        # Process course number
        s3 = processCourseNumber(s3, temporary_course_number)
        print()

        # if the course number is not valid, print out the input is not valid
        if len(s3) == 0:
            print('Invalid Input')
            b_flag = False
            continue

        # Process section number
        processSectionNumber(s3, temporary_section_number)
        print()

        # if the section number is not valid, print out the input
        if len(s3) == 0:
            print('Invalid Input')
            b_flag = False
            continue

        # Check if student has already registered for this course
        duplicateCourse = False
        # Loop through each of set of the student's registered courses
        for i in s:
            # Check to maek sure that the registered subject is the same as the processed one
            # also check to make sure the registered course number is also the same as the processed one.
            # if it is, then it is a duplicate. identify it as a duplicate
            if i.subject == s3.items.data.subject and i.course_number == s3.items.data.course_number:
                print('You already registered for this course')
                duplicateCourse = True
        # Finally add the course to student's courses, as long it is not a duplicate
        if not duplicateCourse:
            print('Successfully registered for course! ', s3)
            print()
            # Add the processed course to the student's course
            s += s3

        # Prompt the user if they want to continue
        a_class = input('Continue? [Y/N]').lower()
    return s



def dropCourse(s):
    """ Function is responsible for accepting user input and dropping a course the user is registered in."""
    class_list = list()

    # Add all of the registered courses to a list
    for i in s:
        class_list.append(i)

    user_choice = '-1'
    while user_choice != '0':
        print("\nCurrent classes are : ")
        j = 0
        for i in s:
            j += 1
            print('Course ' + str(i) + ' Enter [' + str(j) + '] to drop')
        print('Enter [0] to Exit')
        user_choice = input("Enter a class to drop: ")

        # Perform a data type validation. Make sure that the user_choice can be converted into an integer
        try:
            int_choice = int(user_choice)
        except:
            break
        
        # Check to make sure that the user_choice is valid
        if int(user_choice) <= 0 or int(user_choice) > (len(class_list)):
            print('Invalid Choice')
        else:
            # Loop through the registered class and remove if it is present
            for i in s:
                if i == class_list[int(user_choice)-1]:
                    s.remove(i)
                    print('Successfully dropped ' + str(i) + "!")

    return s

# Directly print out the course that was registered
def viewCourse(s):
    print("\nClasses you will be registered for: ", s)
    print()
    return s

""" A function that displays a school's set of courses available. Uses Helper functions printAllAvailableCourses,
    filterByTerm, displayAvailableSubjects, and filterBySubject. """
def viewAvailableCourses(courseCatalog, subject_set):

    user_choice = '-1'
    while user_choice != '0':
        # Construct subject_list for use w/ option 3
        subject_list = list()
        for i in subject_set:
            subject_list.append(i)

        # Prompt user for input
        user_choice = input('Enter 0 to stop: \n'
                        'To view all courses available enter [1]\n'
                        'To view all courses by term enter [2]:\n' \
                        'To view all courses by subject enter [3]:\n'\
                        )
        # If the user chooses 1, run the printAllAvailableCourses and print out all of the courses
        # If the user chooses 2, view all the courses by the term
        # If the user chooses 3, view the courses by the subject
        if user_choice == '1':
            printAllAvailableCourses(courseCatalog)
        elif user_choice == '2':
            term = input('To view Summer 2021 enter [1]:\n'
                         'To view Fall 2021 enter [2]:\n')
            if term == '1':
                filterByTerm(courseCatalog, 'Su2021')
            else:
                filterByTerm(courseCatalog, 'Fa2021')
        elif user_choice == '3':
            j = 0
            for i in subject_list:
                j += 1
                print('To choose ' + i + ' select: [' + str(j) + ']')
            subject_choice = input('Enter choice here: ')
            print()
            try:
                int_choice = int(subject_choice)
            except:
                break
            if int(subject_choice) <= 0 or int(subject_choice) > (len(subject_list)):
                print('Invalid Choice')
                continue
            filterBySubject(courseCatalog, subject_list[int(subject_choice) - 1])


def printAllAvailableCourses(s2):
    # Loop through the entire course catalog and print value
    for i in s2:
        print(i)
    print()

def filterByTerm(s2, term):
    filtered = list()
    # Loop through catalog and append only the term selected
    for i in s2:
        if i.term == term:
            filtered.append(i)

    # Print out each of the fitlered term values
    for i in filtered:
        print(str(i))
    print()

def displayAvailableSubjects(s2):
    filtered = LinkedSet()
    # Loop through the catalog and append the subjects
    for i in s2:
        filtered.add(i.subject)
    # Return subjects
    return filtered


def filterBySubject(s2, subject):
    filtered = list()
    # Loop through and append the class data for the subject selected
    for i in s2:
        if i.subject == subject:
            filtered.append(i)

    # Validation for checking to make sure the selected subject is valid
    if len(filtered) == 0:
        print('Invalid Subject choice: ', subject)
    
    # Print the filtered data
    for i in filtered:
        print(str(i))
    print()


""" Main entry into the program and also the Main menu for a student to register for classes."""
def main(setType):
    s = LinkedSet()
    courseCatalogSet = readAndCreateSet()
    subject_set = displayAvailableSubjects(courseCatalogSet)

    director = "main"

    while director != "0":
        # homepage where user is introduced to program
        print("Wake Tech Course Registration Program Main Menu:\n\n"
              "In this program you will be able to add, drop and view your classes for next semester.\n"
              "If you would like to add classes to your schedule enter [1]\n"
              "If you would like to drop classes from your schedule, enter [2]\n"
              "If you would like to view you class schedule, enter [3]\n"
              "If you would like to view available courses, enter [4]\n"
              "You can exit the program by entering [0].\n")
        director = input("\nWhat would you like to do? ")

        if director == "1":
            s = addCourse(s, courseCatalogSet)

        # section of code responsible for dropping classes
        elif director == "2":
            dropCourse(s)

        # section of code responsible for displaying set of classes
        elif director == "3":
            viewCourse(s)

        elif director == "4":
            viewAvailableCourses(courseCatalogSet, subject_set)
        else:
            print('Invalid Choice: ', str(director))


    print("Goodbye!")


main(LinkedSet)
