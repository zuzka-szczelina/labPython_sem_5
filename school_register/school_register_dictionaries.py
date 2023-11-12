import json
import example_register_generation


def student_class_average(school_class, student_name, student_surname):
    average = None
    for student in school_class['students']:
        if all([student['name'] == student_name, student['surname'] == student_surname]):
            average = sum(student['score'])/len(student['score'])
    return average

def student_total_average(register_name, student_name, student_surname):
    class_averages = []
    for school_class in register_name['classes'].values():
        for student in school_class['students']:
            if all([student['name'] == student_name, student['surname'] == student_surname]):
                class_averages.append(sum(student['score'])/len(student['score']))
    average = sum(class_averages)/len(class_averages)
    return average

def student_total_attendance(register_name, student_name, student_surname):
    all_lessons = 0
    attended_lessons = 0
    for school_class in register_name['classes'].values():
        for student in school_class['students']:
            if all([student['name'] == student_name, student['surname'] == student_surname]):
                all_lessons += len(student['attendance'])
                attended_lessons += list(student['attendance'].values()).count(1)
    total_attendance = {'attended': attended_lessons,
                        "absent": all_lessons - attended_lessons,
                        "percentage_attendance": attended_lessons/all_lessons
                    }
    return total_attendance


if __name__ == "__main__":

    with open('register.json') as f:
       register = json.load(f)
    print("whole register:\n{}".format(json.dumps(register, indent=2)))

    school_class = register['classes']['physics']
    student_name = school_class['students'][0]['name']
    student_surname = school_class['students'][0]['surname']

    class_average1 = student_class_average(school_class,student_name,student_surname)
    print("{} {} average in {} is {}"
          .format(student_name, student_surname, school_class['name'], class_average1))

    total_average1 = student_total_average(register, student_name, student_surname)
    print("{} {} total average is {}"
          .format(student_name, student_surname, total_average1))

    total_attendance1 = student_total_attendance(register, student_name, student_surname)
print("{} {} total attendance is {}"
      .format(student_name, student_surname, total_attendance1))