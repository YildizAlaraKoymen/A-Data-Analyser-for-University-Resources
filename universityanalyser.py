from University import *

def formatMenu(text = "-", width = 100):
    return f"{text.center(width, '-')}"

if __name__=='__main__':

    uni = University("METU", "NCC")
    uni.loadUniversity("departments.txt", "courses.txt")
    print(formatMenu("Welcome to METU NCC data analyser"))
    while True:
        print(formatMenu())
        print("1-Display the lab courses in METU NCC")
        print("2-Display department sizes in METU NCC")
        print("3-Display instructor courses in METU NCC")
        print("4-Display unpopulated courses in METU NCC")
        print("5-Display multi section courses in METU NCC")
        print("6-Display top courses in METU NCC")
        print("7-Exit")
        print(formatMenu())
        try:
            choice = int(input("Enter a number between 1 and 7: "))

            # Check if choice is within the valid range
            if choice < 1 or choice > 7:
                print("Invalid choice. Please enter a number between 1 and 7.")
                continue

            # Display menu options based on user's choice
            if choice == 1:
                uni.printLabCourses()

            elif choice == 2:
                uni.printDepartmentSizes()

            elif choice == 3:
                uni.printInstructorCourses()

            elif choice == 4:
                uni.printUnpopulatedCourses()

            elif choice == 5:
               uni.printMultisectionCourses() #fine

            elif choice == 6:
                uni.printTopCourses()

            elif choice == 7:
                print("Thanks for investigating our Data Analyser!")
                break

        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 7.")

    

