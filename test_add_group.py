# -*- coding: utf-8 -*-
import unittest
from group import Group
from application import Application


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_test_add_group(self):
        self.app.do_login(username="admin", password="secret")
        self.app.create_new_group(Group(name="groupA", header="group header", footer="group footer"))
        self.app.do_logout()

    def tearDown(self):
        self.app.destroy()


if __name__ == '__main__':
    unittest.main()
