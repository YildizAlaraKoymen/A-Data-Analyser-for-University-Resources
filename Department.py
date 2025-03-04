from Course import Course
from LabCourse import LabCourse


class Department:
    def __init__(self, dname= "?", dshortname="?",dcode=0):
        self.dname = dname
        self.dshortname = dshortname
        self.dcode = dcode
        self.courses = []

    def addCourse(self,ccode,cname,isLabCourse):
        if isLabCourse:
            course = LabCourse(ccode,cname)
        else:
            course = Course(ccode,cname)
        self.courses.append(course)

    def getLabCourses(self): return [course for course in self.courses if isinstance(course, LabCourse)]

    def getTotalLabCapacity(self):
        return sum(course.getLabCapacity() for course in self.courses if isinstance(course,LabCourse))

    def getUnpopulatedCourses(self):
        unpopulated_courses = []
        for course in self.courses:
            if course.getTotalRegistered()<5:
                unpopulated_courses.append(course)
        return unpopulated_courses

    def getMultisectionCourses(self):
        multisection_courses = []
        for course in self.courses:
            if course.isMultiSection():
                multisection_courses.append(course)
        return multisection_courses

    def getTopCourses(self):
        sorted_courses = sorted(self.courses, key=lambda course: course.getTotalRegistered(), reverse=True)
        #if no courses added
        if not sorted_courses:
            return []
        max_registered = sorted_courses[0].getTotalRegistered()
        top_courses = [course for course in sorted_courses if course.getTotalRegistered() == max_registered]
        return top_courses

    #Helper Functions

    def isNotEmpty(self):
        if len(self.courses) == 0:
            return 0
        else:
            return 1

    def getDepartmentCapacity(self):
        total = sum(course.getTotalCapacity() for course in self.courses)
        return total

    def getInstructor(self, instructor_name):
        course_list = []
        for course in self.courses:
            if course.hasInstructor(instructor_name):
                course_list.append(course)
        return course_list

    def doesCourseExist(self, ccode):
        for course in self.courses:
            if course.ccode == ccode:
                return True

        return False

    def getCourseIndex(self, ccode):
        for course in self.courses:
            if course.ccode == ccode:
                return self.courses.index(course)
        return -1



