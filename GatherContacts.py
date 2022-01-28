from gen_emails import *
from make_requests import *
import sys


def main(company, pages, domain, format, outfile):
    raw_contacts = gather_contacts(company, pages)
    # # used for testing
    # backup(raw_contacts)
    emails = gen_emails(domain, format, raw_contacts)
    export_csv(emails, outfile)

def usage():
    formats = ["flast", "lastf", "firstlast", "firstdotlast", "firstl", "lastfirst", "first_dot_m_dot_last"]
    print("[~] Usage:\n \tpy .\GatherContacts.py ""company_name"" num_of_pages domain.com firstdotlast ""Company-Contact-List.csv""")
    print("[~] Supported Email Format Options:")
    for f in formats:
        print("\t"+f)

def backup(contacts):
    file = open("temp.csv", "w")
    for cont in contacts:
        file.write(cont+"\n")
    file.close()

def export_csv(emails, outfile):
    file = open(outfile, "w")
    for email in emails:
        file.write(email+"\n")
    file.close()

if __name__ == "__main__":
    try:
        company = sys.argv[1]
        pages = int(sys.argv[2])
        domain = sys.argv[3]
        format = sys.argv[4]
        outfile = sys.argv[5]
        main(company, pages, domain, format, outfile)
    except IndexError as ie:
        print(ie)
        usage()
    except KeyboardInterrupt:
        print("[~] User interrupted, stopping script.")

