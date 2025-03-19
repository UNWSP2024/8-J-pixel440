# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.
def main():
    courses = {}


    print("Please enter all your course information and type 'exit' when your done.")

    while True:
        course_id = input("Please enter your course ID (e.g., 'COS 2005'): ").strip()
        if course_id.lower() == 'exit':
            break

        course_name = input(f"Please enter the course name for {course_id}: ").strip()

        courses[course_id] = course_name


    subject = input("Please enter the class subject (e.g., 'COS') to search for: ").strip()


    print(f"\nCourses for subject {subject}:")

    found = False
    for course_id, course_name in courses.items():
        if course_id.startswith(subject):
            print(f"{course_id}, {course_name}")
            found = True

    if not found:
        print(f"Sorry, there aren't any classes listed for '{subject}'.")



main()
