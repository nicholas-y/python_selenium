import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name='addressbook', user="root", password="")

try:
    # l = db.get_contacts_not_in_group(Group(id="12"))
    # for item in l:
    #     print(item)
    # print(len(l))
    #
    # l_in_group = db.get_contacts_in_group(Group(id="12"))
    # for item in l_in_group:
    #     print(item)
    # print(len(l_in_group))

    # l_without_group = db.get_contacts_without_group()
    # for item in l_without_group:
    #     print(item)
    # print(len(l_without_group))

    l_group_with_contacts = db.get_groups_with_contacts()
    for item in l_group_with_contacts:
        print(item)
    print(len(l_group_with_contacts))

finally:
    pass


