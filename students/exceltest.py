import pandas as pd

data = pd.read_excel (r'Student.xlsx')
df = pd.DataFrame(data)

def enrollment():
    for i in df.index :
        print(df['enrollment'][i])

def name():
    for i in df.index:
        print(df['name'][i])

#INSERT/SAVE DATA TO DATABASE

'''
stu = students(request)
    for i in df.index:
        stu.name = str(df['name'][i])
        stu.enrollment_no = str(df['enrollment'][i])
        stu.save()
        print(df['name'][i])
    
    print("save to db")

'''

'''
stu=students.objects.all()
    for i in stu:
        print(i.enrollment_no)
        a = students.objects.get(enrollment_no=f'{i.enrollment_no}')
        a.branch = 'computer science'
        a.save()

'''

