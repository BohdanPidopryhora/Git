def creation(name, pnumber):
    contacts.append([name, pnumber])

def find_contact(name):
    for i, contact in enumerate(contacts):
        if contact[i] == name:
            return i
    
def read(name):
    print contacts[find_contact(name)][1]

def update(name):
    contacts[find_contact(name)][1] = pnumber

def delete(name):
    contacts[find_contact(name)][1] = []


contacts = []
if __name__ == '__main__':
    while True:
        action = raw_input()
        if action in "Cc":
            name = raw_input("new_contact_name? ")
            pnumber = raw_input("new_contact_pnumber? ")
            creation(name, pnumber)
            continue
        if action in "Rr":
            name = raw_input("read_contact_name? ")
            read(name)
            continue
        if action in "Uu":
            name = raw_input("what_contact_you_want_to_update? ")
            pnumber = raw_input("please_write_a_new_" + name + " number? ")
            update(name)
            continue
        if action in "Dd":
            name = raw_input("what_contact_you_want_to_delete? ")
            delete(name)
            continue
        if action in "RA":
            print contacts
            continue
        
            

