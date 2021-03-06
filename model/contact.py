from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, homephone=None, mobilephone=None, workphone=None, email=None, email2=None, email3=None,
                 birth_year=None, secondary_address=None, secondary_homephone=None, notes=None, id=None, all_phones=None,
                 all_emails=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.birth_year = birth_year
        self.secondary_address = secondary_address
        self.secondary_homephone = secondary_homephone
        self.notes = notes
        self.id = id
        self.all_phones = all_phones
        self.all_emails = all_emails

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.lastname, self.firstname, self.address)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname) \
               and (self.firstname is None or other.firstname is None or self.firstname == other.firstname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
