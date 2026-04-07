#BD with dictionaries.
#You can authenticate using email: valentin@yahoo.com and password: Parola1
#Enjoy! 
from argon2 import PasswordHasher
import json
import pprint
pp = pprint.PrettyPrinter(indent=4)
ph = PasswordHasher()
users_db = {
    "valentin@yahoo.com":{
        "role":"administrator",
        "user":"Valentin",
        "password":"$argon2id$v=19$m=65536,t=3,p=4$VsTLYCH1tyT67FlPR92c+g$C4VhE3DkTY/JIEgZbeW+X+X6Zpa52SgDN9l17tETH4Q",
        "status":True},
    "beatrice@yahoo.com":{
        "role":"integrator",
        "user":"Beatrice",
        "password":"$argon2id$v=19$m=65536,t=3,p=4$Xztynrr4b2t0Q/3/5dA9KA$goTmxHl9/cG83tDGr/xyHEc6EA5fKmCGQ6mjRWfwfA8",
        "status":True},
    "teodor@yahoo.com":{
        "role":"subcont",
        "user":"Teodor",
        "password":"$argon2id$v=19$m=65536,t=3,p=4$upqR4iqvy1l0MH9/+DVCKQ$gAZFEZ3d4JeZO9esUk3AXBvJ+QE8a8oIwLRnVyZ7muE",
        "status":False
    
    }
    }

def create_user(users_db):
    print("Create user:")
    existing_email = ()
    while True:
        email = input("Email:")
        if email in users_db:
            print("This email is already in use, please fill again.")
        else:
            print("The email is available")
            break
    role = int(input("Please specify the role? \n 1.Administrator (Full rights) \n 2.Integrator (Few rights) \n 3.Subcont(Viewer rights) "))
    user = input("User: ")
    password = input("Password: ")
    hash_password = ph.hash(password)
        
    if role ==1:
        users_db.update({email:{"tip":"administrator","user":user,"password":hash_password,"status":True}})
        
    if role ==2:
        users_db.update({email:{"tip":"integrator","user":user,"password":hash_password,"status":True}})
        
    if role ==3:
        users_db.update({email:{"tip":"subcont","user":user,"password":hash_password,"status":True}})

def authentication(users_db):
    print("Welcome, please Login .")
    while True:
        aut_email = input("Email: ")
        aut_parola = input("Password: ")
        
        if aut_email in users_db and users_db[aut_email]["status"]==True:
            try:
                ph.verify(users_db[aut_email]["password"],aut_parola)
                print("You are logged in.")
                print(f"Welcome {aut_email}")
                if users_db[aut_email]["role"] == "administrator":
                    authenticated_admin(users_db)
                if users_db[aut_email]["role"] == "subcont":
                    authenticated_sub(users_db)
                if users_db[aut_email]["role"] =="integrator":
                    authenticated_int(users_db)
            except:
                print("Wrong password!")
        else:
            print("The account does not exist or it has been closed! ")

def delete_user(users_db):
    username = input("Please select the user email you want to delete: ")

    if username in users_db:
        while True:
            confirm = input(
                "Do you confirm the deletion?\n"
                "1. Yes (Warning: this is irreversible!)\n"
                "2. No\n"
                "Choose (1/2): "
            )

            if confirm == "1":
                del users_db[username]
                print(f"The user with the email address '{username}' has been successfully deleted.")
                break

            elif confirm == "2":
                print(f"The deletion of user with the email adress '{username}' has been canceled.")
                break

            else:
                print("Invalid response. Please choose 1 or 2.")
    else:
        print(f"The email adress '{username}' is not in the database.")

def authenticated_admin(users_db):
    print("ADMIN MENU")
    print("You have reached the main menu.")
    print("Please select what you want to do next.")

    while True:
        choice = input(
            "1. CREATE new user\n"
            "2. VIEW database\n"
            "3. EDIT users\n"
            "4. DELETE user\n"
            "5. Log out\n"
            "Your choice: "
        )

        if choice == "1":
            create_user(users_db)

        elif choice == "2":
            pp.pprint(users_db)

        elif choice == "3":
            edit_user(users_db)

        elif choice == "4":
            delete_user(users_db)

        elif choice == "5":
            print("You have successfully logged out.")
            authentication(users_db)
            break

        else:
            print("Invalid option. Please choose a valid number.")

def authenticated_sub(users_db):
    print("SUBACCOUNT MENU")
    print("You have reached the main menu.")
    print("Please select what you want to do now.")
    
    while True:
        try:
            action = int(input(
                "1. CREATE new user\n"
                "2. VIEW database\n"
                "3. Log out\n"
                "Waiting for your answer: "
            ))

            if action == 1:
                create_user(users_db)

            elif action == 2:
                print(users_db)

            elif action == 3:
                print("You have successfully logged out.")
                authentication(users_db)
                break

            else:
                print("Invalid option selected.")

        except ValueError:
            print("Please enter a valid number.")


# DB
def authenticated_int(users_db):
    print("INTEGRATOR MENU")
    print("You have reached the main menu.")
    print("Please select what you want to do now.")
    
    while True:
        try:
            action = int(input(
                "1. CREATE new user\n"
                "2. EDIT user\n"
                "3. VIEW database\n"
                "4. Log out\n"
                "Waiting for your answer: "
            ))

            if action == 1:
                create_user(users_db)

            elif action == 2:
                edit_user(users_db)

            elif action == 3:
                print(users_db)

            elif action == 4:
                print("You have successfully logged out.")
                authentication(users_db)
                break

            else:
                print("Invalid option selected.")

        except ValueError:
            print("Please enter a valid number.")

def edit_user(users_db):
    print("EDIT MENU")
    
    while True:
        try:
            action = int(input(
                "Edit user:\n"
                "1. Change password\n"
                "2. Change permissions\n"
                "3. Change status\n"
                "4. Return to main menu\n"
                "Your choice: "
            ))

            if action == 1:
                print("Choose the user's email.")
                print(users_db)
                email = input("Answer: ")

                if email in users_db:
                    print(f"Please enter the new password for user {email}:")
                    new = input("Answer: ")
                    new_password = ph.hash(new)
                    
                    # preserve existing data if needed
                    users_db[email]["password"] = new_password
                    print("Password updated successfully.")
                    break
                else:
                    print("Email address not found. Please try again.")

            elif action == 2:
                print("Choose the user's email.")
                print(users_db)
                email = input("Answer: ")

                if email in users_db:
                    try:
                        role_choice = int(input(
                            "Update permissions:\n"
                            "1. Administrator\n"
                            "2. Integrator\n"
                            "3. Subaccount\n"
                            "Your choice: "
                        ))

                        if role_choice == 1:
                            users_db[email]["tip"] = "administrator"
                        elif role_choice == 2:
                            users_db[email]["tip"] = "integrator"
                        elif role_choice == 3:
                            users_db[email]["tip"] = "subaccount"
                        else:
                            print("Invalid option.")
                            continue

                        print("Permissions updated successfully.")

                    except ValueError:
                        print("Please enter a valid number.")

                else:
                    print("Email address not found.")
            
            elif action ==3:
                print("Choose the user's email.")
                print(users_db)
                email = input("Answer: ")
                if email in users_db and users_db[email]["status"]==True:
                    print("This account is active, do you want to make it inactive?")
                    choice = int(input("1. Yes\n2. No"))
                    if choice ==1:
                        users_db[email]["status"]==False
                        print(f"The {email} account has been made inactive")
                    else:
                        print("The action has been canceled.")
                        break
                else:
                    print("This email is not in the data base.")
                    break
                    



            elif action == 4:
                authenticated_admin(users_db)
                break

            else:
                print("Invalid option, please try again.")

        except ValueError:
            print("Please enter a valid number.")

authentication(users_db)