"""
Problem: A school wants to store a student's name,age,marks from three tests 
and a collection of related details 
1.Decomposition: student's Name(string), age(int),marks(float/int),comments(string) 
2. student_marks(list),student_details(dictionary),
"""
student_name = "John"
student_age = 15
student_marks = [45.5,65.0,80.5]

student_details = {
    "name": student_name,
    "age":student_age,
    "marks": student_marks
}

print(type(student_name))
print(type(student_age))
print(type(student_marks))
print(type(student_details))
print(student_details["name"])
print(student_marks[0])



