class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_create_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        # open create new contact page
        self.open_create_contact_page()
        # enter contact info
        self.enter_contact_info(contact)
        # click Enter button
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def choose_first_contact(self):
        wd = self.app.wd
        # click on first contact checkbox
        wd.find_element_by_name("selected[]").click()

    def click_edit_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("img[title=\"Edit\"]").click()

    def delete_first(self):
        wd = self.app.wd
        # open home page with contacts list
        self.app.open_home_page()
        # choose contact
        self.choose_first_contact()
        # click Delete button
        wd.find_element_by_css_selector("input[value=\"Delete\"]").click()
        # accept alert
        wd.switch_to_alert().accept()
        # open home page with contacts list
        self.app.open_home_page()

    def edit_first(self, contact):
        wd = self.app.wd
        # open home page with contacts list
        self.app.open_home_page()
        # choose contact
        self.choose_first_contact()
        # click Edit button
        self.click_edit_button()
        # enter contact info
        self.enter_contact_info(contact)
        # click Update button
        wd.find_element_by_name("update").click()
        # open contacts list page
        self.app.open_home_page()

    def enter_contact_info(self, contact):
        wd = self.app.wd
        # enter contact info
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.homephone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # enter Birthday
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birth_year)
        # enter secondary contact info
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.secondary_address)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.secondary_homephone)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
