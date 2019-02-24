
import mysql.connector
import hashlib
import pprint
import sys

#create table users(id int not null primary key auto_increment
# sophia_codigo int
# sophia_codigo_familia int
# mae_cpf varchar(20)
# mae_email varchar(255)
# mae_nome varchar(255)
# matricula varchar(15)
# nome varchar(255)
# pai_cpf varchar(15)
# pai_email varchar(255)
# pai_nome varchar(255));

class User:

    def __init__(self, host, user, password, database):

        self.conn = mysql.connector.connect(host=host, user=user, password=password, database=database)

        self.cursor = self.conn.cursor(prepared=True)


    def update_users(self, dados_alunos):
        """
        Update the table Users.

        Args:
            dados_alunos(dict): Student's data.
        """

        for aluno in dados_alunos:

            self.cursor.execute('INSERT INTO users (sophia_codigo, sophia_codigo_familia,mae_cpf,mae_email,mae_nome,matricula,nome,pai_cpf,pai_email,pai_nome) VALUES (?,?,?,?,?,?,?,?,?,?)',
                    (
                        aluno['codigo'],
                        aluno['codigo_familia'],
                        aluno['mae_cpf'],
                        aluno['mae_email'],
                        aluno['mae_nome'],
                        aluno['matricula'],
                        aluno['nome'],
                        aluno['pai_cpf'],
                        aluno['pai_email'],
                        aluno['pai_nome']
                    )
                )

        self.conn.commit()

    def delete_users(self):
        """
        Empty all data from table Users.
        """

        self.cursor.execute('DELETE FROM users')
        self.conn.commit()

    def generate_tokens(self):
        """
        Generate a MD5 token for every user

        Returns:
            (list): List of dictionaries containing user enrollment number and respective token.
        """

        tokens = []
        token_data = {}

        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute('SELECT matricula, sophia_codigo, sophia_codigo_familia FROM users')

        users = self.cursor.fetchall()

        for data in users:
            string_to_token = str(data['matricula']) + str(data['sophia_codigo_familia']) + str(data['sophia_codigo'])
            token = hashlib.md5(string_to_token).hexdigest()

            token_data['matricula'] = data['matricula']
            token_data['token'] = token

            tokens.append(token_data)

            token_data = {}

        return tokens

    def update_tokens(self, tokens):
        """
        Run through users table and add token for users that doesn't has any yet.

        Args:
            tokens(list): A list of dictionaries containing student enrollment number and its respective token.
        """

        self.cursor = self.conn.cursor(prepared=True)

        for user in tokens:

            self.cursor.execute("SELECT * FROM tokens WHERE matricula='" + str(user['matricula']) + "'")

            count = len(self.cursor.fetchall())

            if count == 0:
                print('nao tem')
                self.cursor.execute('INSERT INTO tokens (matricula, token) VALUES( ?,? )', (user['matricula'], user['token'])) 
                self.conn.commit()

            else:
                print('TEMTE TEMTEMTEMTEMTEMTMTEM')
