students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def disclosure_of_list(_list):
    return [nested_e for nested_list in _list for nested_e in nested_list]


def get_id_age(_students: dict):
    return [(student_id, student_info['age']) for student_id, student_info in _students.items()]


def get_interests_and_surnames(_students):
    return (
        set(disclosure_of_list([student['interests'] for student in _students.values()])),
        sum(len(student['surname']) for student in _students.values())
    )


students_id_age = get_id_age(students)
interests_surnames_length = get_interests_and_surnames(students)

print('Список пар "ID студента — возраст":', students_id_age)
print('Полный список интересов всех студентов:', interests_surnames_length[0])
print('Общая длина всех фамилий студентов:', interests_surnames_length[1])