class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, homephone=None, email=None, birth_year=None,
                 secondary_address=None, secondary_homephone=None, notes=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.email = email
        self.birth_year = birth_year
        self.secondary_address = secondary_address
        self.secondary_homephone = secondary_homephone
        self.notes = notes