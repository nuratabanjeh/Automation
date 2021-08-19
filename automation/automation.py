
import re 
def extract_phones_and_emails():
    with open('./assets/potential-contacts.txt','r') as f:
        
        content = f.read()
        phone_numbers=re.findall(r"\d{3}[-\-\s]\d{3}[-\-\s]\d{4}|\(\d{3}\)\s*\d{3}[-\-\s]\d{4}|\d{3}[-\-\s]\d{4}", content)
        emails=re.findall(r'[\w\.-]+@[\w\.-]+',content)
        sorted_email=sorted(set(emails))
        sorted_phone_num=sorted(set(phone_numbers))
        string_emails = ""

        for i in sorted_email:
            string_emails += i + "\n\n"

        string_phone_num = ""
        for i in sorted_phone_num:
            string_phone_num += i + "\n\n"

        with open('./assets/phone_numbers.txt','w') as f:
             f.write(string_phone_num)

        with open('./assets/emails.txt','w') as f:
             f.write(string_emails)


   



extract_phones_and_emails()