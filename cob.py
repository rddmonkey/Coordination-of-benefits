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
        return f"{cobinfo} Paying Deduct, {self.deduct}, as Deduct is less than Allowable minus" \
               f" primary payment."

    def differencedeductsame(self):
        return f"{cobinfo} Deduct equals difference between allowable minus primary payment, " \
               f"paying deduct ${self.deduct}"

    def allowlessdeduct(self):
        solution = self.allowed - self.primary
        return f"{cobinfo} Paying Difference between Allowable minus Primary payment" \
               f" ${solution}, as allowable is less than deduct."

    def deductcoinsnotzero(self):
        return f"{cobinfo} Paying Deduct + coins = {self.deduct} + {self.coins} = {(self.deduct + self.coins)} as this " \
               f"is less than allowable minus primary payment"

    def coinsplusdeducthigherdifference(self):
        return f"{cobinfo} Paying difference between allowable minus primary payment {difference}" \
               f" as this is less than deduct plus coins"

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


    difference = allowedpay - primarypay

    cobinfo = f"Primary payment = ${primarypay}, Allowable = ${allowedpay}. coins = ${coinspay}. " \
                  f"Deduct = ${deductpay}. Allowable minus primary payment = ${allowedpay} - ${primarypay}" \
                  f" = {difference}."

    if primarypay > allowedpay:
        #if Primary payment exceeds allowable
        print(Cob(primary=primarypay, allowed=allowedpay).primaryhallowed())

    elif deductpay == difference:
        #if deduct equals allowable minus primary payment
        #paying deduct
        print(Cob(primary=primarypay,allowed=allowedpay,deduct=deductpay,coins=coinspay).differencedeductsame())

    elif deductpay < difference and coinspay == 0:
        #if deduct is less than difference between allowable minus primary and there is no coins
        #paying deduct
        print(Cob(primary=primarypay, allowed=allowedpay, deduct=deductpay,coins=coinspay).primaryzerodeduct())

    elif deductpay < difference and coinspay != 0:
        if coinspay + deductpay > difference:
            print(Cob(primary=primarypay,allowed=allowedpay,deduct=deductpay,coins=coinspay).coinsplusdeducthigherdifference())
        else:
            print(Cob(primary=primarypay,allowed=allowedpay,deduct=deductpay,coins=coinspay).deductcoinsnotzero())


