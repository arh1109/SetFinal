# SetFinal
This project is a Python application that simulates a college student’s course registration. The program allows a user to add, drop, view available courses, and view a student’s schedule. 

Our project uses the set data structure to store Course objects defined in a Course class. A set data structure was appropriate for this functionality because courses should be nonduplicate objects when used globally. Also, courses are considered be unique when owned by a different student. We, as a group, chose not to implement a separate Student class, but this could be added on in the future.

The Set implementation we chose was the class LinkedSet. A LinkedSet uses a linked list to store data. Due to this structure of data, LinkedSets have slower operations when compared to a hash set implementation. This is because a LinkedSet must traverse the entire set for searching, adding, and removing elements. For smaller applications, the delay is hardly noticeable. 

Our project uses the classes listed below. The main view component of our application is in testset.py and should be used to launch the application. 



load_course_list.py:
Reads a text file with a list of Courses and adds them to a linked set utilizing the 'linkedset.py' file. A txt file called 'course-list.txt' contains text data for courses. 'course-list.txt' is split and the values combined are the constructor for the course class constructor in 'course.py'. Once the file has been added to the set 'load_course_list_txt.py', the method returns a linked set (named set).
   
course.py:
Creates class object for the class course consisting of the term, subject, course number, section number, name, capacity, and the available seats left in the class. This information is all taken from 'course-list.txt' in 'load_course_list_txt.py'. 'course.py' makes sure no two classes can be taken within the same term. The user of this program can see this by attempting to register for the same two courses within the same term.


linkedset.py:
A linked-based set implementation that uses the node class to construct a set. This file has not been modified from its code in the data structures folder.


node.py:
Links items in a set one after another.



course_registration.py:
Contains the logic and views of the application. The main function holds important variables for storing a LinkedSet for a user of the application and another LinkedSet for storing the entire course catalog which is constructed in load_course_list_txt.py. 


<img src="https://user-images.githubusercontent.com/32178968/118325791-fa927980-b4d1-11eb-820b-9c5e21ba53e0.png" alt="MarineGEO circle logo" width="50%" />
