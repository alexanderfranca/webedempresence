
import mysql.connector
import hashlib
from Link import *
import pprint
import sys

class Comunicate:

    def __init__(self, host, user, password, database, webhost):

        self.conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.cursor = self.conn.cursor(dictionary=True)

        self.link = Link(host=host,user=user,password=password,database=database, webhost=webhost)


    def send_link_email_for_all(self):

        self.cursor.execute('SELECT * FROM users INNER JOIN tokens WHERE users.matricula=tokens.matricula')

        users = self.cursor.fetchall()

        for user in users:
            print(user['nome'].encode('latin-1'))
            weblink = self.link.get_link(matricula=user['matricula'])
            print(weblink)
            
