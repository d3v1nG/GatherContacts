import csv
import sys


def gen_emails(domain, email_format, raw_contacts):
    domain = "@"+domain
    clean_contacts = sanitize_contacts(raw_contacts)
    finished_contacts = []
    # dude fix this mess already
    for contact in clean_contacts:
        contact = contact.split(" ")
        # add switch for different formats
        if email_format == "flast":
            finished_contacts.append(f_last(contact, domain))
        elif email_format == "lastf":
            finished_contacts.append(last_f(contact, domain))
        elif email_format == "firstlast":
            finished_contacts.append(first_last(contact, domain))
        elif email_format == "firstdotlast":
            finished_contacts.append(first_dot_last(contact, domain))
        elif email_format == "firstl":
            finished_contacts.append(first_l(contact, domain))
        elif email_format == "lastfirst":
            finished_contacts.append(last_first(contact, domain))
        elif email_format == "first_dot_m_dot_last":
            finished_contacts.append(first_dot_m_dot_last(contact, domain))
        elif email_format == "first":
            finished_contacts.append(first(contact, domain))
    return finished_contacts
    
# been getting lots of certs/dr prefixes in names, so lets sanitize 
def sanitize_contacts(contacts):
    clean_contacts = []
    for contact in contacts:
        temp_contact = contact.split(",")
        curr = temp_contact[0]
        # weird thing, but gen_emails expects 3 names (first, last, middle)
        # it checks to see if middle is blank, so its easiest to give (first, last) a middle blank name
        if len(curr.split(" ")) == 2:
            curr = curr + " "
        clean_contacts.append(curr)
        # input("PAUSED")
    return clean_contacts

def first(contact, domain):
    email = ""
    if (contact[2] == ""):
        email = contact[0]+domain
    else:
        email = contact[0]+domain
    return email.lower() 

# {f}{last}@domain.com
def f_last(contact, domain):
    email = ""
    if (contact[2] == ""):
        email = contact[0][0]+contact[1]+domain
    else:
        email = contact[0][0]+contact[2]+domain
    return email.lower() 
        
# {last}{f}@domain.com
def last_f(contact, domain):
    email = ""
    if (len(contact[2]) == 0):
        email = contact[1]+contact[0][0]+domain
    else:
        email = contact[2]+contact[0][0]+domain
    return email.lower()

def first_dot_m_dot_last(contact, domain):
    email = ""
    if (len(contact[2]) == 0):
        email = contact[0]+"."+contact[1]+domain
    else:
        email = contact[0] +"."+ contact[1][0] +"."+ contact[2]+domain
    
    return email.lower()

# {first}{last}@domain.com
def first_last(contact, domain):
    email = ""
    if (len(contact[2]) == 0):
        email = contact[0]+contact[1]+domain
    else:
        email = contact[0]+contact[2]+domain
    return email.lower()

# {last}{first}@domain.com
def last_first(contact, domain):
    email = ""
    if (len(contact[2]) == 0):
        email = contact[1]+contact[0]+domain
    else:
        email = contact[2]+contact[0]+domain
    return email.lower()

# {first}.{last}@domain.com
def first_dot_last(contact, domain):
    email = ""
    # print(contact)
    if (len(contact[2]) == 0):
        email = contact[0]+"."+contact[1]+domain
    else:
        email = contact[0]+"."+contact[2]+domain
    # print(email.lower())
    return email.lower()

def first_l(contact, domain):
    email = ""
    if (len(contact[2]) == 0):
        email = contact[0]+contact[1][0]+domain
    else:
        email = contact[0]+contact[2][0]+domain
    return email.lower()

if __name__ == "__main__":
    domain = "@"+str(sys.argv[1])
    email_format = sys.argv[2]
    company = sys.argv[3]
    # gen_emails(domain, email_format)
