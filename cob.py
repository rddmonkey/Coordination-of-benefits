import pyperclip as pc


class Cob:
    def __init__(self, *, primary, allowed, coins=0, deduct=0):
        self.primary = primary
        self.allowed = allowed
        self.coins = coins
        self.deduct = deduct

    def primaryhallowed(self):
        return f"Primary payment = ${self.primary}, Allowable = ${self.allowed}. Primary payment exceeds allowable"

    def primaryzerodeduct(self):
        return f"Primary payment = ${self.primary}, Allowable = ${self.allowed}. coins = ${self.coins}. " \
               f"Deduct = ${self.deduct}. Paying Deduct, {self.deduct}, as Deduct is less than Allowable."

    def allowlessdeduct(self):
        return f"Primary payment = ${self.primary}, Allowable = ${self.allowed}. coins = ${self.coins}. " \
               f"Deduct = ${self.deduct}. Paying Allowable, {self.allowed}, as allowable is less than deduct."


if __name__ == "__main__":
    print(f"Please enter Primary payment: ")
    primarypay = input()
    while not isinstance(primarypay, (int,float)):
        try:
            primarypay = float(primarypay)
        except ValueError:
            print(f"{primarypay} is not a valid number! ")
            print(f"Please enter Primary payment: ")
            primarypay = input()

    print(f"Please enter Allowable: ")
    allowedpay = input()
    while not isinstance(allowedpay, (int, float)):
        try:
            allowedpay = float(allowedpay)
        except ValueError:
            print(f"{allowedpay} is not a valid number! ")
            print(f"Please enter Allowable: ")
            allowedpay = input()

    if primarypay < allowedpay:
        print(f"Please enter coinsurance: ")
        coinspay = input()
        while not isinstance(coinspay, (int,float)):
            try:
                coinspay = float(coinspay)
            except ValueError:
                print(f"{coinspay} is not a valid number! ")
                print(f"Please enter coinsurance: ")
                coinspay = input()

        print(f"Please enter Deduct: ")
        deductpay = input()
        while not isinstance(deductpay, (int,float)):
            try:
                deductpay = float(deductpay)
            except ValueError:
                print(f"{deductpay} is not a valid number! ")
                print(f"Please enter Deduct: ")
                deductpay = input()

    if primarypay > allowedpay:
        print(Cob(primary=primarypay, allowed=allowedpay).primaryhallowed())

    elif deductpay < allowedpay:
        print(Cob(primary=primarypay, allowed=allowedpay, deduct=deductpay).primaryzerodeduct())

    elif deductpay > allowedpay:
        print(Cob(primary=primarypay, allowed=allowedpay, deduct=deductpay).allowlessdeduct())
