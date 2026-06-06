import sqlite3

class Seat:

    database = "cinema.db"

    def __init__(self, seat_id):
        self.seat_id = seat_id

    @classmethod
    def get_empty_seats(cls):
        connection = sqlite3.connect(database=cls.database)
        cursor = connection.cursor()
        cursor.execute("""
                       SELECT "seat_id"
                       FROM "Seat"
                       WHERE "taken" = 0
                       """)
        result = cursor.fetchall()
        connection.close()

        seats_str = " "
        i = 0

        for x in result:
            seats_str += x[0]
            if i != len(result) - 1:
                seats_str += ', '
            i += 1

        return seats_str

    def get_price(self):
        connection = sqlite3.connect(database=self.database)
        cursor = connection.cursor()
        cursor.execute("""
                       SELECT "price"
                       FROM "Seat"
                       WHERE "seat_id" = ?
                       """, [self.seat_id])
        result = cursor.fetchone()
        connection.close()
        return float(result[0])

    def is_free(self):
        connection = sqlite3.connect(database=self.database)
        cursor = connection.cursor()
        cursor.execute("""
            SELECT "taken" FROM "Seat" WHERE "seat_id" = ?
        """, [self.seat_id])
        result = cursor.fetchone()
        connection.close()
        if(int(result[0]) == 1):
            return False
        else:
            return True

    def occupy(self):
            try:
                connection = sqlite3.connect(database=self.database)
                connection.execute("""
                               UPDATE "Seat"
                               SET "taken" = 1
                               WHERE "seat_id" = ?
                               """, [self.seat_id])
                connection.commit()
                connection.close()
                return True
            except:
                return False


if __name__ == "__main__":
    print(Seat("A3").occupy())

