def compute_final_grade(prelim_grade, midterm_grade, final_grade):
    return (prelim_grade * 0.30) + (midterm_grade * 0.30) + (final_grade * 0.40)
def get_grade_description(final_grade):
    if 97 <= final_grade <= 100:
        return 1.0, "Excellent"
    elif 94 <= final_grade <= 96:
        return 1.25, "unique"
    elif 91 <= final_grade <= 93:
        return 1.5, "Outstanding"
    elif 88 <= final_grade <= 90:
        return 1.75, "Very Good"
    elif 85 <= final_grade <= 87:
        return 2.0, "Good"
    elif 82 <= final_grade <= 84:
        return 2.25, "Satisfactory"
    elif 79 <= final_grade <= 81:
        return 2.5, "Not bad"
    elif 76 <= final_grade <= 78:
        return 2.75, "Passing"
    elif final_grade == 75:
        return 3.0, "Barely Passing"
    else:
        return 5.0, "Failing"

def validate_grade(grade):
    return 40 <= grade <= 100

def main():
    name = input("Enter student's name: ")
    section = input("Enter student's section: ")

    try:
        prelim_grade = float(input("Enter prelim grade (40-100): "))
        if not validate_grade(prelim_grade):
            raise ValueError("Prelim grade out of range")
        midterm_grade = float(input("Enter midterm grade (40-100): "))
        if not validate_grade(midterm_grade):
            raise ValueError("Midterm grade out of range")
        finals_grade = float(input("Enter finals grade (40-100: "))
        if not validate_grade(finals_grade):
            raise ValueError("Finals grade out of range")
    except ValueError as e:
        print("Error:", e)
        return

    final_grade = compute_final_grade(prelim_grade, midterm_grade, finals_grade)

    grade_points, description = get_grade_description(final_grade)

    print("\n--- Student Final Grade Report ---")
    print(f"Prelim Grade: {prelim_grade}")
    print(f"Midterm Grade: {midterm_grade}")
    print(f"Finals Grade: {finals_grade}")
    print(f"Final Grade: {final_grade:.2f}")
    print(f"Grade Points: {grade_points}")
    print(f"Description: {description}")

if __name__ == "__main__":
    main()
