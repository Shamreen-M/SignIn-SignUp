# This is database for SignIn-SignUp Project
account=dict() #account={'admin':'password'}
saveSecQuest=dict() #saveSecQuest={'admin':{'question1':'answer1','question2':'answer2','question3':'answer3'}}

# Passing some default data values to database
account={'Shamreen':'Password@1234'}
saveSecQuest={'admin':{'Q1':'Cat','Q2':'Sunita','Q3':'Bangalore'}}

# Method for saving security questions
def saveSecurityQuestions(username):
    if username not in saveSecQuest:
        ans1=input("Which is your Favorite Pet ? \n").lower()
        ans2=input("Who is your First Teacher ? \n").lower()
        ans3=input("Which is your Birth Place ? \n").lower()
        saveSecQuest.update({username:{'Q1':ans1,'Q2':ans2,'Q3':ans3}})
        print("Securty Questions are updated..")
    else:
        print("Invalid username")
    
# Method for signup
def SignUp():
    username=input("Enter New Username: ").lower()
    if username not in account:
        password=input("Enter Password: ")
        if checkPasswordStrength(password)==1:
            confirmPassword=input("Confirm Password again: ")
            if password==confirmPassword:
                account.update({username:password})
                saveSecurityQuestions(username)
                print(f'Username {username} added Successfully!!')
            else:
                print("Password doesn't match")
        else:
            print("Error - Password doesn't match criteria")
                
    else:
        print("Error - Username already exists!!")
    
# Method for login
def login(username,password):
    if username in account:
        if password == account.get(username):
            print("Login successful!!")
        else:
            print("Error - Username or password is incorrect")
    else:
        print("Error - Username or password is incorrect")
        
# Method for checking password strength
def checkPasswordStrength(password):
    digit=special=upper=lower=0
    if len(password)>=8:
        for char in password:
            if char.isdigit():
                digit+=1
            elif char.isalpha():
                if char.islower():
                    lower=lower+1
                elif char.isupper():
                    upper=upper+1
            elif char in list(['#','@','$','_']):
                special=special+1
        if digit>=1 and lower>=1 and upper>=1 and special>=1:
            return 1
    return 0

# Method to reset password
def resetPassword(username):
    if username in account:
        flag=0
        print("--- Answer Security Questions to reset Password ---")
        ans1=input("Which is your Favorite Pet ? \n").lower()
        ans2=input("Who is your First Teacher ? \n").lower()
        ans3=input("Which is your Birth Place ? \n").lower()
        if ans1==saveSecQuest.get(username).get('Q1'):
            flag+=1 
        if ans2==saveSecQuest.get(username).get('Q2'):
            flag+=1 
        if ans3==saveSecQuest.get(username).get('Q3'):
            flag+=1 
        if flag>=2:
            newPass=input("Enter New Password: ")
            confirmPass=input("Confirm Password again: ")
            if newPass==confirmPass:
                if checkPasswordStrength(newPass)==1:
                    account.update({username:newPass})
                    print("Password Reseted Successfully!!")
                else: 
                    print("Error - Password doesn't match criteria ")
            print("Error - Incorrect Password")
        else:
            print("Error - Unable to reset password due to failed authentication")
    else:
        print("Error - Username doesn't exists")
        
# Method to change password
def changePassword(username):
    if username in account:
        currPass=input("Enter Current Password: ")
        if currPass==account[username]:
            newPass=input("Enter New Password: ")
            if newPass!=currPass:
                if checkPasswordStrength(newPass)==1:
                    confirmPass=input("Confirm New Password again:")
                    if newPass==confirmPass:
                        account.update({username:newPass})
                        print("Password Changed Successfully!!")
                    else:
                        print("Error - Password doesn't match")
                else:
                    print("Error - Password doesn't match criteria")
            else:
                print("Error - Password is repeated")
        else:
            print("Error - Current Password is incorrect")
    else:
        print("Error - Username doesn't exists")
    
# Method to delete username
def deleteUsername(username):
    if username in account:
        if username in saveSecQuest:
            password=input("Enter Password for authentication: ")
            if password == account.get(username):
                account.pop(username)
                saveSecQuest.pop(username)
                print("Record deleted!!")
            else: print("Error - Password is incorrect.. Unable to delete record")
        else: print("Error - Unable to delete record")
    else: print("Error - Username doesn't exists")

# Method to print usernames in account
def printUsername():
    if len(account)==0:
        print("No data in account")
    else:
        print("All usernames in account: ")
        for ele in list(account.keys()): print(ele)
