
def add_user():

    user_data = {
        "name": input("Enter name: "),
        "surname": input("Enter surname: "),
        "age": input("Enter age: "),
        "birthdate": input("Enter birthdate"),
        "number": input("Enter number: ")
    }
    
    lugat = {user_data}
    return lugat

user_main = add_user()

print(user_main)
