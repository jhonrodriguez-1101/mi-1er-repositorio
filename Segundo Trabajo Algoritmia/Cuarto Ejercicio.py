student_scores = {
    "Harry" : 88,
    "Ron" : 78,
    "Hermione" : 95,
    "Draco" : 75,
    "neville" : 60,
}
student_grades = {}
for estudiantes, nota in student_scores .items():
    if nota >= 91: 
        student_grades[estudiantes] = "Sobresaliente"
    elif nota <= 90 and nota >= 81:
        student_grades[estudiantes] = "Excelente"
    elif nota <= 80 and nota >= 71:
        student_grades[estudiantes] = "Aceptable"
    elif nota <= 70:
        student_grades[estudiantes] = "Mal"
print (student_grades)



