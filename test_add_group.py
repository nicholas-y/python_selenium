# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False},
                            firefox_binary="c:/Program Files/Mozilla Firefox/firefox.exe")
        self.wd.implicitly_wait(60)

    def test_test_add_group(self):
        self.do_login(username="admin", password="secret")
        self.create_new_group(Group(name="groupA", header="group header", footer="group footer"))
        self.logout()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def create_new_group(self, group):
        wd = self.wd
        self.open_group_page()
        # open create group page
        wd.find_element_by_name("new").click()
        # enter group name
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        # enter group header
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        # enter group footer
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # click submit button
        wd.find_element_by_name("submit").click()
        # open group list page
        wd.find_element_by_link_text("group page").click()

    def open_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def do_login(self, username, password):
        wd = self.wd
        self.open_login_page()
        # enter username
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        # enter password
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        # click login button
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_login_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
