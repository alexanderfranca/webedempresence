import pymssql
from Mssql import *
from User import *

import pprint


#mssql = Mssql(host='10.0.0.249', user='sa', password='M@sterkey', database='SophiA')
#tudo = mssql.gera_dados_alunos()
#
#pprint.pprint(tudo)


user = User(host='localhost', user='edempresence', password='3d3mzeppelin%ZEPPELIN', database='edempresence')

#user.update_users(dados_alunos=tudo)

tokens = user.generate_tokens()

user.update_tokens(tokens)

