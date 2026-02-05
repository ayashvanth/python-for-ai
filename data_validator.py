class DataValidator:
    def __init__(self):
        self.errors = []

    def validate_email(self, email):
        if "@" not in email:
            self.errors.append(f"Wrong Email Address:{email}")
            print("Wrong Email Address")

    def validate_age(self, age):
        if age < 18 and age > 40:
            self.errors.append(f"Invalid Age:{age}")
            print("Invaid Age")
    
    def get_errors(self):
        return self.errors
    
validatorInstance = DataValidator()

validatorInstance.validate_email("mr.abhishek.y#gmail.com")
validatorInstance.validate_age(32)

validatorInstance.get_errors()