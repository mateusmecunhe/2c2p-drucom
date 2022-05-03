import csv
from distutils.log import error
from warnings import catch_warnings


class Pledge:
    def __init__(self):
        pass


def read_drucom_report(filename='drucom_input'):
    with open(f'{filename}.csv', newline='') as csvfile:
        list_of_pledges = []
        reader = csv.DictReader(csvfile)
        for row in reader:
            donation_date = row.get('Date').split(' ')[0].split('/')            
            p = Pledge()
            p.COUNTRY = row.get('Market')
            p.FLAG = 'NEW'
            p.CHARITY_CODE = ''
            p.SERIAL_NO = None
            p.ID_NUMBER = ''
            p.TITLE = row.get('Personal title')
            p.FIRSTNAME = row.get('First name')
            p.LASTNAME = row.get('Last name')
            p.ALTERNATE_NAME = ''
            p.GENDER = ''
            p.DOB = row.get('Date of birth')
            p.RACE = ''
            p.TEL_HSE = row.get('Phone')
            p.TEL_HP = row.get('Phone')
            p.TEL_OFF = ''
            p.FAX = ''
            p.EMAIL = row.get('Email')
            p.ADDRESS1 = ''
            p.ADDRESS2 = ''
            p.ADDRESS3 = ''
            p.ADDRESS4 = ''
            p.POSTCODE = ''
            p.CITY = ''
            p.STATE = ''
            p.ADDRESS_COUNTRY = ''
            p.SPOKEN_LANGUAGE = ''
            p.OPTOUT_EMAIL = 'Y' if row.get(
                'Consent Preference - Email') == 'off' else 'N'
            p.OPTOUT_POSTAL = 'Y' if row.get(
                'Consent Preference - Mail') == 'off' else 'N'
            p.RECRUITER_CODE = ''
            p.SUB_RECRUITER_CODE = ''
            p.RECRUITER_BATCH_NUMBER = ''
            p.CHARITY_SOURCE_CODE = ''
            p.CAMPAIGN_CODE = row.get('Campaign ID').split(' ')[0]
            p.CAMPAIGN_DESCRIPTION = " ".join(_ for _ in row.get('Campaign ID').split(
                ' ')[1::]) if row.get('Campaign ID').split(' ')[1::] else ''
            p.FUNDCODE = ''
            p.SIGNUP_DATE = f'{donation_date[1]}/{donation_date[0]}/{donation_date[2]}'
            p.AGENT_ID = ''
            p.AGENT_NAME = ''
            p.drucom_DONATION_AMOUNT = row.get('Donation Amount')
            p.FREQUENCY = '0' if row.get('Donation type') == 'One-off' else '1'
            p.PROCESSING_BANK = ''
            p.BANK_ACCOUNT_NUMBER = ''
            p.BANK_ACCOUNT_BANK_CODE = ''
            p.BANK_ACCOUNT_BRANCH_CODE = ''
            p.BANK_ACCOUNT_HOLDER_NAME = ''
            p.BANK_ACCOUNT_HOLDER_ID_NUMBER = ''
            p.BANK_ACCOUNT_HOLDER_ADDRESS = ''
            p.CREDIT_CARD_NUMBER = ''
            p.CREDIT_CARD_EXPIRY_DATE = ''
            p.CREDIT_CARD_TYPE = ''
            p.CREDIT_CARD_PAYMENT_TYPE = ''
            p.CREDIT_CARD_LEVEL = ''
            p.CREDIT_CARD_ISSUING_BANK_NAME = ''
            p.CREDIT_CARD_ISSUING_BANK_CODE = ''
            p.CREDIT_CARD_HOLDER_NAME = ''
            p.TER_REQUIRED = ''
            p.REMARKS = ''
            p.CHANNEL = ''
            p.AUTO_CHANGE_AMOUNT_TYPE = ''
            p.AUTO_CHANGE_AMOUNT_INTERVAL = ''
            p.AUTO_CHANGE_AMOUNT = ''
            p.PLEDGE_STATUS = ''
            p.CONTRACT_CODE = ''
            p.ANALYSIS_CODE = ''
            p.CUSTOMERS_NAME = ''
            p.BANK_ACCOUNT_BILL_KEY = ''
            p.ALTERNATE_FIRSTNAME = ''
            p.ALTERNATE_LASTNAME = ''
            p.EVENT_CODE = ''
            p.LOCATION_CODE = ''
            p.drucom_TRANSACTION_ID = row.get('Transaction ID')
            p.CAMPAIGN_ID = row.get('Campaign ID'),
            list_of_pledges.append(p)

        return list_of_pledges


def read_2c2p_export(data, filename='2c2p_input'):
    with open(f'{filename}.csv', newline='') as csvfile:
        csvfile.readline()
        reader = csv.DictReader(csvfile)
        pledges = []
        for row in reader:
            trans_id = row.get('Transaction ID')
            pledge = list(filter(lambda x: x.drucom_TRANSACTION_ID == trans_id, data))
            if pledge:
                pledge = pledge[0]
                pledge.CREDIT_CARD_NUMBER = row.get('Card No / Wallet')
                pledge.DONATION_AMOUNT = row.get('Transaction Amount').replace('.', '').replace(',', '.')
                pledge.PAID_AMOUNT_NET = row.get('Net AmountMYR')
                pledge.PLEDGE_STATUS = row.get('Status')
                pledge.DATE_PAYMENT = row.get('Settlement Date/Time')
                pledge.CREDIT_CARD_ISSUING_BANK_NAME = row.get('Card Issuer')
                pledge.CHANNEL = row.get('Payment Channel')
                pledges.append(pledge)
        return pledges


fieldnames = [
    'FLAG', 'CHARITY_CODE', 'SERIAL_NO', 'ID_NUMBER', 'TITLE', 'FIRSTNAME', 'LASTNAME', 'ALTERNATE_NAME', 'GENDER',
    'DOB', 'RACE', 'TEL_HSE', 'TEL_HP', 'TEL_OFF', 'FAX', 'EMAIL', 'ADDRESS1', 'ADDRESS2', 'ADDRESS3', 'ADDRESS4',
    'POSTCODE', 'CITY', 'STATE', 'ADDRESS_COUNTRY', 'SPOKEN_LANGUAGE', 'OPTOUT_EMAIL', 'OPTOUT_POSTAL', 'RECRUITER_CODE',
    'SUB_RECRUITER_CODE', 'RECRUITER_BATCH_NUMBER', 'CHARITY_SOURCE_CODE', 'CAMPAIGN_CODE', 'CAMPAIGN_DESCRIPTION',
    'FUNDCODE', 'SIGNUP_DATE', 'AGENT_ID', 'AGENT_NAME', 'DONATION_AMOUNT', 'FREQUENCY', 'PROCESSING_BANK',
    'BANK_ACCOUNT_NUMBER', 'BANK_ACCOUNT_BANK_CODE', 'BANK_ACCOUNT_BRANCH_CODE', 'BANK_ACCOUNT_HOLDER_NAME',
    'BANK_ACCOUNT_HOLDER_ID_NUMBER', 'CREDIT_CARD_NUMBER', 'CREDIT_CARD_EXPIRY_DATE', 'CREDIT_CARD_TYPE', 'CREDIT_CARD_PAYMENT_TYPE',
    'CREDIT_CARD_ISSUING_BANK_NAME', 'CREDIT_CARD_ISSUING_BANK_CODE', 'CREDIT_CARD_HOLDER_NAME', 'TER_REQUIRED', 'REMARKS', 'CHANNEL'
]


pledge_fieldnames = [
    "COUNTRY",
    "FLAG",
    "CHARITY_CODE",
    "SERIAL_NO",
    "ID_NUMBER",
    "TITLE",
    "CUSTOMER'S NAME",
    "FIRSTNAME",
    "LASTNAME",
    "ALTERNATE_NAME",
    "ALTERNATE_FIRSTNAME",
    "ALTERNATE_LASTNAME",
    "GENDER",
    "DOB",
    "RACE",
    "TEL_HSE",
    "TEL_HP",
    "TEL_OFF",
    "FAX",
    "EMAIL",
    "ADDRESS1",
    "ADDRESS2",
    "ADDRESS3",
    "ADDRESS4",
    "POSTCODE",
    "CITY",
    "STATE",
    "ADDRESS_COUNTRY",
    "SPOKEN_LANGUAGE",
    "OPTOUT_EMAIL",
    "OPTOUT_POSTAL",
    "RECRUITER_CODE",
    "SUB_RECRUITER_CODE",
    "RECRUITER_BATCH_NUMBER",
    "CHARITY_SOURCE_CODE",
    "CAMPAIGN_CODE",
    "CAMPAIGN_DESCRIPTION",
    "FUNDCODE",
    "SIGNUP_DATE",
    "AGENT_ID",
    "AGENT_NAME",
    "DONATION_AMOUNT",
    "FREQUENCY",
    "PROCESSING_BANK",
    "BANK_ACCOUNT_NUMBER",
    "BANK_ACCOUNT_BILL_KEY",
    "BANK_ACCOUNT_BANK_CODE",
    "BANK_ACCOUNT_BRANCH_CODE",
    "BANK_ACCOUNT_HOLDER_NAME",
    "BANK_ACCOUNT_HOLDER_ID_NUMBER",
    "BANK_ACCOUNT_HOLDER_ADDRESS",
    "CREDIT_CARD_NUMBER",
    "CREDIT_CARD_EXPIRY_DATE",
    "CREDIT_CARD_TYPE",
    "CREDIT_CARD_PAYMENT_TYPE",
    "CREDIT_CARD_LEVEL",
    "CREDIT_CARD_ISSUING_BANK_NAME",
    "CREDIT_CARD_ISSUING_BANK_CODE",
    "CREDIT_CARD_HOLDER_NAME",
    "TER_REQUIRED",
    "REMARKS",
    "CHANNEL",
    "AUTO_CHANGE_AMOUNT_TYPE",
    "AUTO_CHANGE_AMOUNT_INTERVAL",
    "AUTO_CHANGE_AMOUNT",
    "PLEDGE_STATUS",
    "CONTRACT_CODE",
    "ANALYSIS_CODE",
    "EVENT_CODE",
    "LOCATION_CODE"
]

gift_fieldnames = [
    'COUNTRY',
    'FLAG',
    'CHARITY_CODE',
    'SERIAL_NO',
    'CHARITY_TRANS_ID',
    'PAID_AMOUNT',
    'DATE_PAYMENT',
    'REQUESTED_AMOUNT',
    'AUTHORIZATION_INDICATOR',
    'REJECT_REASON_CODE',
    'REJECT_REASON_DESCRIPTION',
    'PROCESSING_BANK'
]

donor_fieldnames = [
]


def write_pledge(data):

    with open('sg_pledge_output.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=pledge_fieldnames)
        writer.writeheader()
        for p in data:
            if not p.CREDIT_CARD_NUMBER:
                continue
            
            writer.writerow(
                {
                    "COUNTRY": p.COUNTRY,
                    "FLAG": p.FLAG,
                    "CHARITY_CODE": 'UNHCR',
                    "SERIAL_NO": None,
                    "ID_NUMBER": '', #TODO,
                    "TITLE": p.TITLE,
                    "CUSTOMER'S NAME": f'{p.FIRSTNAME} {p.LASTNAME}',
                    "FIRSTNAME": p.FIRSTNAME,
                    "LASTNAME": p.LASTNAME,
                    "ALTERNATE_NAME": None,
                    "ALTERNATE_FIRSTNAME": None,
                    "ALTERNATE_LASTNAME": None,
                    "GENDER": p.GENDER,
                    "DOB": p.DOB,
                    "RACE": p.RACE,
                    "TEL_HSE": None,
                    "TEL_HP": p.TEL_HP,
                    "TEL_OFF": p.TEL_OFF,
                    "FAX": p.FAX,
                    "EMAIL": p.EMAIL,
                    "ADDRESS1": p.ADDRESS1,
                    "ADDRESS2": p.ADDRESS2,
                    "ADDRESS3": p.ADDRESS3,
                    "ADDRESS4": p.ADDRESS4,
                    "POSTCODE": p.POSTCODE,
                    "CITY": p.CITY,
                    "STATE": p.STATE,
                    "ADDRESS_COUNTRY": p.ADDRESS_COUNTRY,
                    "SPOKEN_LANGUAGE": p.SPOKEN_LANGUAGE,
                    "OPTOUT_EMAIL": p.OPTOUT_EMAIL,
                    "OPTOUT_POSTAL": p.OPTOUT_POSTAL,
                    "RECRUITER_CODE": 'UNHCR_OL',
                    "SUB_RECRUITER_CODE": None,
                    "RECRUITER_BATCH_NUMBER": None,
                    "CHARITY_SOURCE_CODE": None,
                    "CAMPAIGN_CODE": p.CAMPAIGN_CODE,
                    "CAMPAIGN_DESCRIPTION": p.CAMPAIGN_DESCRIPTION,
                    "FUNDCODE": p.FUNDCODE,
                    "SIGNUP_DATE": p.SIGNUP_DATE,
                    "AGENT_ID": p.drucom_TRANSACTION_ID,
                    "AGENT_NAME": p.AGENT_NAME,
                    "DONATION_AMOUNT": p.DONATION_AMOUNT,
                    "FREQUENCY": p.FREQUENCY,
                    "PROCESSING_BANK": get_processing_bank_value(p.CHANNEL), #p.PROCESSING_BANK,
                    "BANK_ACCOUNT_NUMBER": p.BANK_ACCOUNT_NUMBER,
                    "BANK_ACCOUNT_BANK_CODE": p.BANK_ACCOUNT_BANK_CODE,
                    "BANK_ACCOUNT_BRANCH_CODE": p.BANK_ACCOUNT_BRANCH_CODE,
                    "BANK_ACCOUNT_HOLDER_NAME": p.BANK_ACCOUNT_HOLDER_NAME,
                    "BANK_ACCOUNT_HOLDER_ID_NUMBER": p.BANK_ACCOUNT_HOLDER_ID_NUMBER,
                    "BANK_ACCOUNT_HOLDER_ADDRESS": p.BANK_ACCOUNT_HOLDER_ADDRESS,
                    "CREDIT_CARD_NUMBER": p.CREDIT_CARD_NUMBER,
                    "CREDIT_CARD_EXPIRY_DATE": p.CREDIT_CARD_EXPIRY_DATE,
                    "CREDIT_CARD_TYPE": p.CREDIT_CARD_TYPE,
                    "CREDIT_CARD_PAYMENT_TYPE": p.CREDIT_CARD_PAYMENT_TYPE,
                    "CREDIT_CARD_LEVEL": p.CREDIT_CARD_LEVEL,
                    "CREDIT_CARD_ISSUING_BANK_NAME": p.CREDIT_CARD_ISSUING_BANK_NAME,
                    "CREDIT_CARD_ISSUING_BANK_CODE": p.CREDIT_CARD_ISSUING_BANK_CODE,
                    "CREDIT_CARD_HOLDER_NAME": p.CREDIT_CARD_HOLDER_NAME,
                    "TER_REQUIRED": p.TER_REQUIRED,
                    "REMARKS": p.CHANNEL,
                    "CHANNEL": 'WEB',
                    "AUTO_CHANGE_AMOUNT_TYPE": p.AUTO_CHANGE_AMOUNT_TYPE,
                    "AUTO_CHANGE_AMOUNT_INTERVAL": p.AUTO_CHANGE_AMOUNT_INTERVAL,
                    "AUTO_CHANGE_AMOUNT": p.AUTO_CHANGE_AMOUNT,
                    "PLEDGE_STATUS": None, #TODO p.PLEDGE_STATUS,
                    "CONTRACT_CODE": p.CONTRACT_CODE,
                    "ANALYSIS_CODE": p.ANALYSIS_CODE,
                    "BANK_ACCOUNT_BILL_KEY": p.BANK_ACCOUNT_BILL_KEY,
                    "EVENT_CODE": p.EVENT_CODE,
                    "LOCATION_CODE": p.LOCATION_CODE,

                }
            )


def write_gifts(data):
    with open('sg_gifts_output.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=gift_fieldnames)
        writer.writeheader()
        for p in data:
            
            writer.writerow(
                {
                    'COUNTRY': p.COUNTRY,
                    'FLAG': p.FLAG,
                    'CHARITY_CODE': p.COUNTRY,
                    'SERIAL_NO': None,
                    'CHARITY_TRANS_ID': p.drucom_TRANSACTION_ID,
                    'PAID_AMOUNT': p.DONATION_AMOUNT,
                    'DATE_PAYMENT': format_2c2p_date(p.DATE_PAYMENT), #p.DATE_PAYMENT,
                    'REQUESTED_AMOUNT': p.drucom_DONATION_AMOUNT,
                    'AUTHORIZATION_INDICATOR': 'APP' if p.PLEDGE_STATUS == 'Settled' else 'REJ',
                    'REJECT_REASON_CODE': '',
                    'REJECT_REASON_DESCRIPTION': '',
                    'PROCESSING_BANK': get_processing_bank_value(p.CHANNEL)
                }
            )

def get_processing_bank_value(bank):
    
    bank = bank.lower()
    data = {
            'fpx': 'MANUAL',
            'grab': 'EWALLET',
            'boost': 'EWALLET',
            'tng': 'EWALLET',
    }
    return data.get(bank) or '2C2P'

def format_2c2p_date(date_string):
    #input format: YYYY/MM/DD HH:MM:SS
    try:
        donation_date = date_string.split(' ')[0].split('/')       
    except Exception:
        print(f'error on date {date_string}: {Exception} \n expected input format: YYYY/MM/DD HH:MM:SS ')
        return None
    return f'{donation_date[2]}/{donation_date[1]}/{donation_date[0]}'
    
    

if __name__ == "__main__":
    from datetime import datetime

    now = datetime.now()
    
    data = read_drucom_report()
    finalized_data = read_2c2p_export(data=data)
    write_pledge(finalized_data)
    write_gifts(finalized_data)
    then = datetime.now()
    print(then - now)

