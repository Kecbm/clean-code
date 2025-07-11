d = None; # time in days


days_since_the_last_purchase = None;
days_until_next_invoice = None;
total_business_days_in_month = None;
days_since_last_login = None;

# “Programmers create problems for themselves when they write code solely for the compiler or interpreter.”

# code without purpose
class TheClass:
    def __init__(self, theList):
        self.theList = theList

    def getThem(self):
        return sum(self.theList) / len(self.theList)


# names more meaningful
class StatisticsCalculator:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def calculate_average(self):
        return sum(self.numbers) / len(self.numbers)


# refactor of the names
class StudentGradeCalculator:
    def __init__(self, grades):
        self.student_grades = grades
    
    def calculate_grade_average(self):
        return sum(self.student_grades) / len(self.student_grades)


# methods with nice names
class UserSystem:
    def __init__(self, usersData):
        self.student_data = usersData

    def validate_credentials(self):
        return 'Method to validate credentials'

    def update_profile(self):
        return 'Method to update profile'

    def send_password_reset_email(self):
        return 'Method to send password reset email'