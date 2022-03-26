from email.policy import default


def modules():
    print("Enter module code")
    module = input()

    switcher = {
        'CSC1006' : 'Mathematics 2',
        'CSC1007' : 'Operating Systems',
        'CSC1008' : 'Data Structures and Algorithms',
        'CSC1009' : 'Object Oriented Programming',
        'CSC1010' : 'Computer Networks',
    }

    print(switcher[module])

def numbers():
    number = 102
    for i in range(102-66):
        if number % 2 == 1:
            print(number)
        number -= 1
        
modules()
numbers()