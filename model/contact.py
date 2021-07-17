class ContactInfoBday:
    def __init__(self, bday_day, bday_month,  bday_year):
        self.bday_day = bday_day
        self. bday_month=bday_month
        self.bday_year=bday_year

class ContactInfoName:
    def __init__(self, first_name, middle_name, last_name):
        self.first_name =first_name
        self.middle_name=middle_name
        self.last_name=last_name

class ContactPhones:
    def __init__(self, mobile, home_phone, work_phone):
        self.mobile = mobile
        self.home_phone = home_phone
        self.work_phone = work_phone

class ContactEmails:
    def __init__(self, email, email2, email3):
        self.email = email
        self.email2 = email2
        self.email3 = email3

class ContactSecondary:
    def __init__(self, address2, phone2, notes):
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
