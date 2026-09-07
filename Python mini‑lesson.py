# student_filter.py
# A simple Python script to filter student data by course

students = [
    {"name": "Amit", "course": "Python"},
    {"name": "Riya", "course": "Java"},
    {"name": "Nitin", "course": "Python"},
    {"name": "Sara", "course": "Web Development"}
]

def filter_students(course_name):
    result = [s for s in students if s["course"].lower() == course_name.lower()]
    return result

# Test the function
if __name__ == "__main__":
    course = "Python"
    filtered = filter_students(course)
    print(f"Students enrolled in {course}:")
    for s in filtered:
        print("-", s["name"])
