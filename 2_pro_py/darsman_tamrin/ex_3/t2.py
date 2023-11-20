'''information calls customer -> creating contact book'''
class Address():
    def __init__(self,city,streat,num_home) -> None:
        self.city=city
        self.streat=streat
        self.num_home=num_home

class Person():
    def __init__(self,code,fname,lname,phon,email) -> None:
        self.code=code
        self.fname=fname
        self.lname=lname
        self.phon=phon
        self.email=email
    
class PhoneBook():
    def __init__(self) -> None:
        pass

    def add_Contact(self,contact):
        pass
class Contact(Address,Person):
    pass