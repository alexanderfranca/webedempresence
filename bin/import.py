import pymssql
from webpresence.presence import Presence 


pre = Presence(host='localhost', user='edempresence', password='3d3mzeppelin%ZEPPELIN', database='edempresence')

pre.import_presences(filepath='/home/alexander/presences.txt')

