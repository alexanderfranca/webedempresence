
import mysql.connector
import re
import sys 

class Link:
    """
    This class only generate web links for users.
    """

    def __init__(self, host, user, password, database, webhost):

        self.conn = mysql.connector.connect(host=host, user=user, password=password, database=database)

        self.cursor = self.conn.cursor(dictionary=True)

        self.webhost = webhost

    def generate_links(self):
        """
        Run through tokens table and generate the web link.

        Returns:
            (list): List of web links.
        """

        self.cursor.execute("SELECT * FROM tokens")

        data = self.cursor.fetchall()

        for user in data:
            print(str(self.webhost) + '?matricula=' + str(user['matricula']) + '&token=' + str(user['token']))

    def get_link(self, matricula):

        self.cursor.execute("SELECT * FROM tokens WHERE matricula='" + str(matricula) + "'")

        user = self.cursor.fetchone()

        return str(self.webhost) + '?matricula=' + str(user['matricula']) + '&token=' + str(user['token'])

    def check_cpf(self, matricula, cpf):

        if len(matricula) == 5:
            matricula = '0' + str(matricula)

        elif len(matricula) == 4:
            matricula = '00' + str(matricula)


        cpf = str(cpf).replace('.','')
        cpf = str(cpf).replace('-','')

        self.cursor.execute("SELECT * FROM users WHERE matricula='" + str(matricula) + "' AND (mae_cpf='" + str(cpf) + "' OR pai_cpf='" + str(cpf) + "')")

        result = self.cursor.fetchone()

        if len(result) > 0:
            return True
        else:
            return False

