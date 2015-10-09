def creation(name, pnumber):
    cont[name] = pnumber
    
def read(name):
    print cont[name]

def update(name):
    cont[name] = pnumber

def delete(name):
    del cont[name]

cont = {}
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
        
            

