# Create a dictionary containing course numbers and the room numbers:
course_room_dictionary = {"CSC101": "3004", "CSC102": "4501", "CSC103": "6755", "NET110": "1244", "COM241": "1411"}

# Create a dictionary containing course numbers and the names of the instructors:
course_instructor_dictionary = {"CSC101": "Haynes", "CSC102": "Alvarado", "CSC103": "Rich", "NET110": "Burke", "COM241": "Lee"}

# Create a dictionary containing course numbers and the meeting times:
course_meeting_dictionary = {"CSC101": "8:00 a.m.", "CSC102": "9:00 a.m.", "CSC103": "10:00 a.m.", "NET110": "11:00 a.m.", "COM241": "1:00 p.m."}
while True:
    course = input ("Enter a course number: ").upper()
    if course in course_room_dictionary.keys():
        print(f"Course: {course} - Room: {course_room_dictionary[course]} - Instructor: {course_instructor_dictionary[course]} - Meeting Time: {course_meeting_dictionary[course]}")
        break
    else:
        print(f"Course {course} not found.")