import sqlite3

class Card:

    database = 'banking.db'

    def __init__(self, type, number, cvc, holder):
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder

    def validate(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM "Card" WHERE 
                "type" = ? and
                "cvc" = ? and
                "holder" = ? and
                "number" = ? 
        """, [self.type, self.cvc, self.holder, self.number])

        result = cursor.fetchall()
        connection.close()
        if(len(result) == 0):
            return False
        else:
            return True

    def get_balance(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute(""" SELECT "balance" FROM "Card" 
                           WHERE "holder" = ? and "number" = ?
        """, [self.holder, self.number])
        result = cursor.fetchone()
        connection.close()
        return (result[0])


    def deduct_price(self, price):
        connection = sqlite3.connect(self.database)
        connection.execute("""
                       UPDATE "Card" SET "balance" =  ? WHERE "holder" = ? and "number" = ?
                       """, [(self.get_balance() - price), self.holder, self.number])
        connection.commit()
        connection.close()

if(__name__ == "__main__"):
    card = Card("Visa", "12345678", "123", "John Smith")
    print(card.validate())
    print(card.get_balance())
    card.deduct_price(float(50))
    print(card.get_balance())
