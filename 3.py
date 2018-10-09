"""Returns:
if age > 25: “Hello <name> <surname>! How are you doing?”
if age <= 25: “Yo <name> <surname>! How are you doing?”

Requirements:
Name, surname - should be required parameters.
Age is optional (equals 18 by default)
Function should handle other positional and keyword parameters."""


def say_hello(name, surname, age=None):
    try:
        if not all((isinstance(name, str), isinstance(surname, str))):
            raise ValueError
        if age is None or not isinstance(age, int): age = 18
        if age >= 25:
            return 'Hello {} {}! How are you doing?'.format(name, surname)
        else:
            return 'Yo {} {}! How are you doing?'.format(name, surname)
    except ValueError:
        print('Please check your informaton')
        return ''
name = input('Enter your name: ')
surname = input('Enter your surname: ')
age = input('Enter your age: ')
print(say_hello(name, surname, age))
