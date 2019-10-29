from datetime import date

def hello_world(return_val):
	return return_val

def return_data_structure():
	return date.today()

def accept_object_reference(today):
	return today.year

class HelloWorld:

    def __init__(self):
        self.message = "Hello World Class"

    def hello_world(self):
        return self.message
