#OOP(Modeling)
#Object Oriented Programing
#has classes and objects

#Classes
# has properties/attributes

#ie student
#first name
#lastname
#reg-no
#contact
#email
#address

#creating classes
#cohort class
#it starts with a capital letter

#class Cohort:
    #name
    #description
    #start_date
    #end_date

#with in thne cohort class, add a constructor for the cohort class
#(read about construction in w3 schools)
#add a method to  the class that prints the cohort name and total number
#of students
# create a new instance/object of the cohort class




class Cohort:


    def __init__(self, name, students=None):
        
        self.name = name
        self.students = students if students else []

    def add_student(self, student):
        
        self.students.append(student)

    def remove_student(self, student):
       
        if student in self.students:
            self.students.remove(student)

    def print_cohort_info(self):
        
        print(f"Cohort Name: {self.name}")
        print(f"Total Students: {len(self.students)}")

# Example Usage:

if __name__ == "__main__":
    # Create a new Cohort object
    cohort_4 = Cohort("Cohort 4")

    # Add students to the cohort
    cohort_4.add_student("Brenda")
    cohort_4.add_student("Harriet")
    cohort_4.add_student("Monica")

    # Print cohort information
    cohort_4.print_cohort_info()

    # Remove a student from the cohort
    cohort_4.remove_student("Brenda")

    # Print updated cohort information
    print("\nUpdated Cohort Information:")
    cohort_4.print_cohort_info()


