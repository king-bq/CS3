class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount
        
    def get_name(self):
        return self.__name
        
    def set_name(self, name):
        self.__name = name
        
    def get_bill_amount(self):
        return self.__bill_amount
        
    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount
        
    def calculate_bill(self):
        print(f"Patient Name: {self.get_name()}")
        print(f"Original Bill: ₱{float(self.get_bill_amount())}")
        print(f"Final Bill: ₱{float(self.get_bill_amount())}\n")

class SeniorPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        print(f"Patient Name: {self.get_name()}")
        print(f"Original Bill: ₱{float(self.get_bill_amount())}")
        print(f"Final Bill: ₱{(self.get_bill_amount() - self.get_bill_amount() * 0.2)}\n")
    
class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        print(f"Patient Name: {self.get_name()}")
        print(f"Original Bill: ₱{float(self.get_bill_amount())}")
        print(f"Final Bill: ₱{(self.get_bill_amount() - self.get_bill_amount() * 0.15)}\n")

print("Hospital Billing System\n-----------------------")

regular_patient = Patient("Juan Dela Cruz", 15000)
regular_patient.calculate_bill()

senior_patient = SeniorPatient("Maria Santos", 15000)
senior_patient.calculate_bill()

philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000)
philhealth_patient.calculate_bill()
