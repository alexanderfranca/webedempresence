import pymssql
from webpresence.link import Link

import pprint


link = Link(host='localhost', user='edempresence', password='3d3mzeppelin%ZEPPELIN', database='edempresence', webhost='http://www.edem.g12.br/edempresence/')

links = link.check_cpf('004900', '025.206.077-69')


