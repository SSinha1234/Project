# Objective :- Password strength checker that evaluates the strength of user provided password.

# Condition for password strength
# min 8 chars, digit, uppercase, lowercase, special chars

import re

def check_password_strength(Password):

    if len(Password) < 8:
        return "weak: Password must be 8 chars"
    
    if not any (char.isdigit() for char in Password): # check whether char is digit 
        return "weak: Password must contain digit"
    
    if not any(char.isupper() for char in Password):
        return"weak: Password must contain Upper Case"
    
    if not any(char.islower() for char in Password):
        return "weak:Password contain lower case "
    
    if not re.search(r'[1@#$%^(){}<>.?]',Password):
        return "weak: Password must contain a special character"
    
    return "Strong: Your Password is secure"

# Password = input("enter the password")
# result = check_password_strength(Password) # this will take once again need to run the code so create checker for reuse
# print(result)


# Password Checker

def Password_checker():
    print("welcome! to the password strength checker")

    while True:
        Password = input("Enter your password(or type 'exit' to quit):")

        if Password.lower() == 'exit':
           print("Thank you for using this tool")
           break
        result = check_password_strength(Password)
        print(result)
    
# # Run the password checker tool 

if __name__ == "__main__":
    Password_checker()
    
   
  



        
