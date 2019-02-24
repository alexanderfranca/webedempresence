import pymssql
from Mssql import *
from User import *
from Link import *
from Comunicate import *

import pprint


#link = Link(host='localhost', user='edempresence', password='3d3mzeppelin%ZEPPELIN', database='edempresence', webhost='http://www.edem.g12.br/edempresence/')

#links = link.generate_links()

#print( link.get_link(matricula='003997'))

comunicate = Comunicate(host='localhost', user='edempresence', password='3d3mzeppelin%ZEPPELIN', database='edempresence', webhost='http://www.edem.g12.br/edempresence/')

comunicate.send_link_email_for_all()
