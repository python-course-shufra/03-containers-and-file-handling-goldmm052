classroom = [
    {
        'name': 'Alice',
        'email': 'alice@example.com',
        'grades': [
            ('math', 91),
            ('english', 78),
            ('math', 90),
            ('history', 34),
            ('math', 95),
        ],
    },
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'grades': [
            ('math', 85),
            ('english', 92),
            ('history', 75),
        ],
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'grades': [
            ('physics', 78),
            ('english', 81),
            ('english', 89),
            ('history', 68),
            ('english', 82),
            ('physics', 91),
        ],
    },
]


def index(name):
    for i,student in enumerate(classroom) :
        if name==student['name']:
            return i
    return -1
def add_student(name, email=None):
    if index(name)==-1:
        if email==None:
          
            email=name.lower()+'@example.com'
        classroom.append({'name':name,'email':email,'grades':[],});
    else:
        print("the student is exist!");
def delete_student(name):
    i=index(name)
    if i==-1:
        print("the student is not exist!")
    else:
        del classroom[i]
def set_email(name, new_email):
    i=index(name)
    if i==-1:
        print("the student is not exist!")
    else:
        
        for student in classroom:
            if student['name'] == name:
                 student['email'] = new_email
                 break
def add_grade(name, profession, grade):
    i=index(name)
    if i==-1:
        print("the student is not exist!")
    else:
        for student in classroom:
            if student['name'] == name:
                  student['grades'].append((profession, grade))
                  break

def avg_grade(name, profession):
    for student in classroom:
        if student['name'] == name:
            grades = [grade for subj, grade in student['grades'] if subj == profession]
            if len(grades) > 0:
                gpa = sum(grades) / len(grades)
                return gpa
            else:
                return None
    return None

def get_professions(name):
   grades_list = []
   subjects = []
   for student in classroom:
        if student['name'] == name:
            for subject, _ in student['grades']:
                 if subject not in subjects:
                     subjects.append(subject)

   print(subjects)
