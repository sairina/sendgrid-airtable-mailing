from airtable import Airtable

def get_emails(base, table):
    airtable = Airtable(base, table)
    airtable_emails = airtable.get_all(fields='Email')
    emails = []
    for email in airtable_emails:
        emails.append(email['fields']['Email'])
    return emails