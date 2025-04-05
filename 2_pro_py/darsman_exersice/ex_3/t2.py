'''information calls customer -> creating contact book'''
class Address():
    def __init__(self,city,streat,num_home) -> None:
        self.city=city
        self.streat=streat
        self.num_home=num_home
        self.Address_dict={}

    def add_Address(self):
        self.Address_dict['city']=self.city
        self.Address_dict['streat']=self.streat
        self.Address_dict['home number']=self.num_home
        return self.Address_dict

    def __repr__(self):
        return f'city:{self.city} , streat:{self.streat} , home number:{self.num_home}'

class Person():
    def __init__(self,code,fname,lname,phon,email) -> None:
        self.code=code
        self.fname=fname
        self.lname=lname
        self.phon=phon
        self.email=email
        self.Person_dict={}
    
    def add_Person(self):
        self.Person_dict['code']=self.code
        self.Person_dict['fname']=self.fname
        self.Person_dict['lname']=self.lname
        self.Person_dict['phone']=self.phon
        self.Person_dict['email']=self.email
        return self.Person_dict

    def __repr__(self):
        return f'code:{self.code} , fname:{self.fname} , lname:{self.lname} , phone:{self.phon} , email{self.email}'

class Contact(Person,Address):
    def __init__(self, code, fname, lname, phon, email,city,streat,num_home) -> None:
        Person.__init__(self,code, fname, lname, phon, email)
        Address.__init__(self,city,streat,num_home)
        self.Contact_dict={}
    
    def add_Contact(self):
        dict1=self.add_Person()
        dict2=self.add_Address()
        for dic in (dict1,dict2):
            self.Contact_dict.update(dic)
        return self.Contact_dict

    def __repr__(self):
        return f'{Person.__repr__(self)},{Address.__repr__(self)}'
        
class PhoneBook():
    def __init__(self) -> None:
        self.phone_book=[]

    def add_Contact(self,contact_dict):
        self.phone_book.append(contact_dict)
        return self.phone_book

    def search_Customer(self,lname):
        self.tempList=[]
        for i in self.phone_book:
            if lname in i:
                self.tempList.append(i)
        if self.tempList == []:
            return f'Unknown Customer'
        else:
            for contact in self.tempList:
                contact=Contact(contact['code'],contact['fname'],contact['lname'],contact['phon'],contact['email'],contact['city'],contact['streat'],contact['num_home'])
                contact.__repr__()

    def __repr__(self):
        for contact in self.phone_book:
            for k,v in contact.items():
                print(k,':',v,end=' ')
            print()

###################test instance

contact1=Contact(124,'nekou','dfrm',47623,'nekou@gmail.com','Yk','LM',234)
contact1_dict=contact1.add_Contact()
print(contact1)

contact2=Contact(124,'nekou','dfrm',47623,'nekou@gmail.com','Yk','LM',234)
contact2_dict=contact2.add_Contact()
print(contact2)

contact3=Contact(124,'nekou','dfrm',47623,'nekou@gmail.com','Yk','LM',234)
contact3_dict=contact3.add_Contact()
print(contact3)

PhoneBook1=PhoneBook()
PhoneBook1.add_Contact(contact1_dict)
PhoneBook1.add_Contact(contact2_dict)
PhoneBook1.add_Contact(contact3_dict)

print(PhoneBook1.search_Customer('dfrm'))


