# -*- coding: utf-8 -*-
import unittest
from contact import Contact
from application import Application

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.app = Application()
    
    def test_test_add_contact(self):
        self.app.do_login(username="admin", password="secret")
        self.app.create_new_contact(Contact(firstname="Tom", middlename="J", lastname="Tomson", nickname="Tm" ,
                                        title="Boss", company="Comp", address="address line", homephone="800-900",
                                        email="auto@test.com", birth_year="1970",
                                        secondary_address="address line secondary",
                                        secondary_homephone="801-901", notes="contact record"))
        self.app.do_logout()



    def tearDown(self):
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()
