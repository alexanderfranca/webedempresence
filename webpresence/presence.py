
import mysql.connector

class Presence:

    def __init__(self, host, user, password, database):

        self.conn = mysql.connector.connect(host=host, user=user, password=password, database=database)

        self.cursor = self.conn.cursor(dictionary=True)

    def get_presence(self, matricula):

        self.cursor = self.conn.cursor(dictionary=True)

        presences = []

        self.cursor.execute("SELECT * FROM presence WHERE matricula='" + str(matricula) + "' ORDER BY year desc, month desc, day desc, hour desc, minute desc, second desc")

        data = self.cursor.fetchall()

        for presence in data:
            presences.append({ 'act': presence['act'], 'year': presence['year'], 'month': presence['month'], 'day': presence['day'], 'hour': presence['hour'], 'minute': presence['minute'], 'second': presence['second'], 'matricula': presence['matricula'] })

        return presences

    def import_presences(self, filepath):

        self.cursor = self.conn.cursor(prepared=True)

        with open(filepath) as presences:

            for line in presences:
                record = line.split(',')

                act = record[0]
                year = record[1]
                month = record[2]
                day = record[3]
                hour = record[4]
                minute = record[5]
                second = record[6]
                matricula = record[7].rstrip('\r\n')

                self.cursor.execute("SELECT * FROM presence WHERE year=? AND month=? AND day=? AND hour=? AND minute=? AND second=? AND matricula=?", (year, month, day, hour, minute, second, matricula))

                if len(self.cursor.fetchall()) > 0:
                    continue
                else:
                    self.cursor.execute("INSERT INTO presence (act, year, month, day, hour, minute, second, matricula) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (act, year, month, day, hour, minute, second, matricula))
                    self.conn.commit()
