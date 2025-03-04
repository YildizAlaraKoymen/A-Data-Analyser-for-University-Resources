class Course:

    def __init__(self, ccode=0,cname=" "):
        self.ccode=ccode
        self.cname=cname
        self.sections = {}

    def addSection(self,section,capacity,no_registered,instructor):
        self.sections[section]=(instructor, capacity, no_registered)


    def __str__(self):
        sections_details = "\n".join(
            "Section = {}, Instructor = {}, Capacity = {}, Registered = {}".format(section, i[0], i[1], i[2])
            for section,
            i in self.sections.items())

        return "Details for {}:\n{}".format(self.ccode, sections_details)


    def getTotalCapacity(self):
        total = 0
        for section in self.sections:
            total += int(self.sections[section][1])

        return total

    def hasInstructor(self, instructor_name): #returns true if a specific instructor exists in course
        for section in self.sections:
            if instructor_name in self.sections[section][0]:
                return True

        return False

    def getTotalRegistered(self):
        total = 0
        for section in self.sections:
            total += int(self.sections[section][2])

        return total

    def isMultiSection(self):

        if len(self.sections) > 1:
            return True
        else:
            return False
