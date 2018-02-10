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