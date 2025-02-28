class CoursePlanner:
    course_rooms = {
        "CSC101": "3004",
        "CSC102": "4501",
        "CSC103": "6755",
        "NET110": "1244",
        "COM241": "1411",
    }
    course_teachers = {
        "CSC101": "Haynes",
        "CSC102": "Alvarado",
        "CSC103": "Rich",
        "NET110": "Burke",
        "COM241": "Lee",
    }
    course_times = {
        "CSC101": "8:00 a.m.",
        "CSC102": "9:00 a.m.",
        "CSC103": "10:00 a.m.",
        "NET110": "11:00 a.m.",
        "COM241": "1:00 p.m.",
    }
    
    def __init__(self, course_rooms, course_teachers, course_times):
        if course_rooms is not None:
            self.course_rooms = course_rooms
        if course_teachers is not None:
            self.course_teachers = course_teachers
        if course_times is not None:
            self.course_times = course_times
            
    def get_user_input(self):
        course = input("Enter the course to know the info about: ")
        return course
    
    def get_course_info(self, course):
        print("".center(150, "-") + "\n", end="|")
        print("Course Info:".center(148) + "|\n", end="|")
        print("".center(148, "-") + "|\n", end="|")
        print(f"Course".center(49), end="|")
        print(f"Room".center(49), end="|")
        print(f"Time".center(48) + "|\n", end="|")
        print("".center(148, "-") + "|\n", end="|")
        if course in self.course_rooms:
            room = self.course_rooms[course]
            teacher = self.course_teachers[course]
            time = self.course_times[course]            
            print(f"{course}".center(49), end="|")
            print(f"{room}".center(49), end="|")
            print(f"{time}".center(48) + "|\n", end="|")
            print("".center(148, "_") + "|\n", end="")
        else:
            print(f"The course {course} not found.".center(148), end="|\n|")
            print("".center(148, "_"), end="|\n")
            
def main():
    coursePlanner = CoursePlanner(None, None, None)
    course = coursePlanner.get_user_input()
    coursePlanner.get_course_info(course)
    
if __name__ == "__main__":
    main()  