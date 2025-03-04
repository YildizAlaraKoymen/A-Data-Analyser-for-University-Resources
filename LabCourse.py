from Course import *

class LabCourse(Course):

    def __init__(self, ccode=0,cname=" "):
        Course.__init__(self, ccode, cname)
        self.labsections = {}


    def addLabSection(self,section,capacity,no_registered,instructor):
        self.labsections[section] = (instructor,capacity,no_registered)

    def getLabCapacity(self):
        sum(i[1] for i in self.labsections.values())

    def __str__(self):
        Course.__str__(self) #Calling from parent class
        labsection_details ="\n".join("Lab Section = {}, Instructor = {}, Capacity = {}, Registered = {}".format( section,i[0],i[1],i[2])
        for section,
        i in self.labsections.items())

        sections_details = "\n".join("Section = {}, Instructor = {}, Capacity = {}, Registered = {}".format(section, i[0], i[1], i[2])
        for section,
        i in self.sections.items())
        return "Details for {}:\n{}\n{}".format(self.ccode, labsection_details, sections_details)

    def isMultiSection(self):

        if len(self.labsections) > 1:
            return True
        else:
            return False


