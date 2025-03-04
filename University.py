import re  # to use regular expressions
from Department import *
from LabCourse import *
import matplotlib.pyplot as plt


class University:
    def __init__(self, uname=" ", ubranch=" "):
        self.uname = uname
        self.ubranch = ubranch
        self.departments = []

    def loadUniversity(self, departmentsFilename, coursesFilename):

        # Reading records from departments.txt
        try:
            file_departments = open(departmentsFilename, 'r')
        except IOError:
            print("Departments file not found")
            exit(1)

        records_department = file_departments.read().split("\n")
        file_departments.close()

        print("Departments:")
        for record in records_department[1:]:  # Skip header
            fields = record.split(",")
            if len(fields) >= 3:
                dept_code, short_name, dept_name = fields[0], fields[1], fields[2]
                # Changed to get class instead

                if self.doesDepartmentExist(dept_code):
                    print("Department already exists, skipping Department Code: {}, Short Name: {}, Department Name: {}".format(
                        dept_code, short_name, dept_name
                    ))
                    continue

                self.addDepartment(dept_name, short_name, dept_code)

                # Printing departments info
                print("Department Code: {}, Short Name: {}, Department Name: {}".format(
                    dept_code, short_name, dept_name
                ))
        print("\n")

        # Using regular expression to validate course code format
        course_code_format = re.compile(r'^[A-Z]{3,4}\s?\d{3,4}$')

        # Reading records from courses.txt
        try:
            file_courses = open(coursesFilename, "r")
        except IOError:
            print("Courses file not found")
            exit(1)

        records_courses = file_courses.read().split("\n")
        file_courses.close()

        print("Courses:")
        for record in records_courses[1:]:  # Skip header
            fields = record.split(",")
            if len(fields) >= 7:
                dept_code, course_code, course_name, instructor, section, capacity, registered_students = (
                    fields[0],
                    fields[1],
                    fields[2],
                    fields[3],
                    fields[4],
                    fields[5],
                    fields[6]
                )

                # Validating course code format
                if not course_code_format.match(course_code):
                    print("Invalid course code format for course {}. Skipping.".format(course_code))
                    continue

                # Ensuring that the course code starts with department's short name
                department = next((d for d in self.departments if d.dcode == dept_code),None)

                if department is None:
                    print(f"Department with short name {dept_code} not found. Skipping.")
                    continue


                lab_pattern = r"Lab\d+"
                section_pattern = r"S\d+"

                # Distinguishing between lecture (Sx) and lab (Labx) sections
                # Done with regex

                dep_index = self.getDepartmentIndex(dept_code)
                if dep_index == -1:
                    print("Department doesn't exist!")
                    continue

                if re.search(lab_pattern, section):
                    if not self.departments[dep_index].doesCourseExist(course_code):
                        self.departments[dep_index].addCourse(course_code, course_name, True)
                    course_index = self.departments[dep_index].getCourseIndex(course_code)
                    self.departments[dep_index].courses[course_index].addLabSection(section, capacity, registered_students, instructor)
                elif re.search(section_pattern, section):
                    if not self.departments[dep_index].doesCourseExist(course_code):
                        self.departments[dep_index].addCourse(course_code, course_name, False)
                    course_index = self.departments[dep_index].getCourseIndex(course_code)
                    self.departments[dep_index].courses[course_index].addSection(section, capacity, registered_students, instructor)
                else:
                    print("Unrecognized section type for section {}. Skipping.".format(section))
                    continue

                # Printing the course data
                print(
                    "Department Code: {}, Course Code: {}, Course Name: {}, Instructor: {}, Section: {}, Capacity: {}, Registered: {}".format(
                        dept_code, course_code, course_name, instructor, section, capacity, registered_students
                    ))
        print("\n")

    def doesDepartmentExist(self, dept_code):
        for department in self.departments:
            if department.dcode == dept_code:
                return True

        return False

    def getDepartmentIndex(self, dept_code):
        for department in self.departments:
            if department.dcode == dept_code:
                return self.departments.index(department)
        return -1

    def addDepartment(self, dname, dshortname, dcode):
        new_department = Department(dname, dshortname, dcode)
        self.departments.append(new_department)

    def formatMessage(self, text = "-", width = 100):
        return f"{text.center(width, '-')}"

    def printLabCourses(self):
        print(self.formatMessage("Lab Courses"))
        lab_course = []
        for department in self.departments:
            lab_courses = department.getLabCourses()
            for course in lab_courses:
                print(course)
        if len(lab_course) == 0:
            print("No lab courses found")
        print(self.formatMessage())

    def printDepartmentSizes(self):
        if len(self.departments) == 0:
            print("No departments found")
        else:
            if sum(department.isNotEmpty() for department in self.departments) == 0:
                print("No courses found")
            else:
                print(self.formatMessage("Department Sizes"))
                department_labels = []
                sizes = []
                for department in self.departments:
                    department_labels.append(department.dshortname)
                    sizes.append(department.getDepartmentCapacity())

                plt.pie(sizes, labels=department_labels)
                plt.title('Department Sizes')
                plt.show()
                print(self.formatMessage())

    def printInstructorCourses(self):
        if len(self.departments) == 0:
            print("No departments found")
        else:
            if sum(department.isNotEmpty() for department in self.departments) == 0:
                print("No courses found")
            else:
                print(self.formatMessage("Instructor Courses"))
                course_list = []
                instructor_name = input("Name of instructor: ")
                for department in self.departments:
                    temp = department.getInstructor(instructor_name)
                    if temp:
                        course_list.extend(temp)

                if len(course_list) == 0:
                    print("Instructor {} not found".format(instructor_name))
                    self.printInstructorCourses()

                else:
                    count = 0
                    for course in course_list:
                        count += 1
                        print("{}. {}".format(count, course.cname))

                    valid_response = True
                    while valid_response:
                        if count == 1:#If there is only 1 course don't ask for input
                            course_num = count
                        else:
                            course_num = int(input("Select course to print [1 - {}]: ".format(count)))
                        if course_num > len(course_list) or course_num < 1:
                            print('Invalid input "{}" Enter again'.format(course_num))
                        else:
                            print(course_list[course_num - 1])
                            valid_response = False
                    print(self.formatMessage())

    def printUnpopulatedCourses(self):
        print(self.formatMessage("Unpopulated Courses"))
        unpopulated_courses = []
        for department in self.departments:
            unpopulated_courses = department.getUnpopulatedCourses()
            for course in unpopulated_courses:
                print(course)
        if len(unpopulated_courses) == 0:
            print("There aren't courses with less than 5 students")

        print(self.formatMessage())

    def printMultisectionCourses(self):
        print(self.formatMessage("Multisection Courses"))
        multi_section_courses = []
        for department in self.departments:
            multi_section_courses = department.getMultisectionCourses()
            for course in multi_section_courses:
                print(course)
        if len(multi_section_courses) == 0:
            print("There aren't any multisection courses found")
        print(self.formatMessage())

    def printTopCourses(self):
        print(self.formatMessage("Top Courses"))
        top_courses = []
        for department in self.departments:
            top_courses = department.getTopCourses()
            for course in top_courses:
                print(course)
        if len(top_courses) == 0:
            print("There aren't any courses found")
        print(self.formatMessage())

