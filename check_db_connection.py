import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name='addressbook', user="root", password="")

try:
    l = db.get_contacts_not_in_group(Group(id="12"))
    for item in l:
        print(item)
    print(len(l))

    l_in_group = db.get_contacts_in_group(Group(id="12"))
    for item in l_in_group:
        print(item)
    print(len(l_in_group))
finally:
    pass


