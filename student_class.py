def student_class():
    while True:
        try:
            total_students = int(input("Enter the total number of students in the class: "))
            math_students = int(input("Enter the number of students with mathematics: "))
            bio_students = int(input("Enter the number of students with bio: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid value in integer .")
        
            
    without_math_bio = total_students - (math_students + bio_students)
    with_math_bio = math_students + bio_students
    
    if with_math_bio > total_students:
        print('Run again! You give wrong input please give the values within the total number of students')
             
        
    else:
        print(f"Number of students without Math and Bio: {without_math_bio}")
        print(f"Number of students with Math and Bio: {with_math_bio}")

student_class()
