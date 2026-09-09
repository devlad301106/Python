import json
import random
import string 
from pathlib import Path

class Bank:

    db = 'data.json'
    data = []

    try:
        if Path(db).exists():
            with open(db, "r") as fd:
                data = json.loads(fd.read())
        else:
            print("No such file exists!")

    except Exception as err:
        print(f"AN exception occurs as {err}")

    @classmethod
    def __update(cls):
        with open(cls.db, "w") as f:
            f.write(json.dumps(cls.data))

    @classmethod
    def __accountNogenerate(cls):
        alpha = random.choices(string.ascii_letters,k = 3)
        num = random.choices(string.digits,k = 3)
        spchar = random.choices("!@#$%^&*",k = 1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)
    
    
    def createaccount(self):
        info ={
            "name" : input("Enter your Name: "),
            "age" : int(input("ENter your age: ")),
            "email" : input("Enter your email address: "),
            "pin" : int(input("Tell yor pin: ")),
            "accountNo." : Bank.__accountNogenerate(),
            "balance" : 0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry! you cannot create your account.")

        else:
            print("Your account has been created successfully!")

            for i in info:
                print(f"{i} : {info[i]}")

            print("PLease note down your account number!")

            Bank.data.append(info)

            Bank.__update()

    def depositMoney(self):
        accnumber = input("Enter your Account number: ")
        pin = int(input("Enter your pin: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin] 

        if userdata == False:
            print("Sorry! account does not exist.")

        else:
            amount = int(input("Enter the amount you want to deposit: "))
            if amount > 10000 and amount < 0:
                print("Sorry! amount is too big, you can deposit money less than 10000.")

            else:
                print(userdata)
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited successfully!")


user = Bank()

print("Enter 1 to create a new account.")
print("Enter 2 to deosit money in Bank.")
print("Enter 3 to withdraw the money.")
print("Enter 4 for details.")
print("Enter 5 for updating the details.")
print("Enter 6 to delete the account.")

check = int(input("Enter your reponse: "))

if check == 1:
    user.createaccount()

if check == 2:
    user.depositMoney()