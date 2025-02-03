class Bank:
    bank_name='SBI'
    def __init__(self,username,age,bal):
        self.username = username
        self.age = age
        self.user_balance = bal

    def get_info(self):
        print(f'''User Name: {self.username} and 
        user balance: {self.user_balance} 
        for Bank : {self.bank_name}''')
b1 = Bank('Pooja',26,55000)
print(b1.bank_name) #SBI
print(Bank.bank_name) #SBI
b1.get_info()