class SessionHelper:

    def __init__(self, app):
        self.app = app

    def do_login(self, username, password):
        wd = self.app.wd
        self.app.open_login_page()
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

    def do_logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        if self.is_logged_in():
            self.do_logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout"))

    def is_logged_in_as(self, username):
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text[1:-1]

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.do_logout()
        self.do_login(username, password)