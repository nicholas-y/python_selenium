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
        self.fill_contact_form(contact)
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
        self.fill_contact_form(contact)
        # click Update button
        wd.find_element_by_name("update").click()
        # open contacts list page
        self.app.open_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.fill_contact_form_field("firstname", contact.firstname)
        self.fill_contact_form_field("middlename", contact.middlename)
        self.fill_contact_form_field("lastname", contact.lastname)
        self.fill_contact_form_field("nickname", contact.nickname)
        self.fill_contact_form_field("title", contact.title)
        self.fill_contact_form_field("company", contact.company)
        self.fill_contact_form_field("address", contact.address)
        self.fill_contact_form_field("home", contact.homephone)
        self.fill_contact_form_field("email", contact.email)
        # enter Birthday
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").click()

        self.fill_contact_form_field("byear", contact.birth_year)
        # enter secondary contact info
        self.fill_contact_form_field("address2", contact.secondary_address)
        self.fill_contact_form_field("phone2", contact.secondary_homephone)
        self.fill_contact_form_field("notes", contact.notes)

    def fill_contact_form_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            # enter contact info
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))
