import requests
import json
import datetime
from os.path import dirname, join

print(datetime.datetime.now())
date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
print(date)

url="https://sandbox.api.visa.com/visadirect/fundstransfer/v1/pushfundstransactions"

key = join(dirname(__file__), "key_510b3ab1-03c1-4e90-81f3-6f10d876a58d.pem")
cert = join(dirname(__file__), "cert.pem")



headers={"Accept":"application/json"}

user_id="4YGY6OCK9LJMYB64O2X821d0_K6FiBVMMm7ERR4QrwxytU1PQ"
password="VBYB1VYpqJ3qZctXEw6"

body={}

timeout=10

payload = json.loads('''
{
"acquirerCountryCode": "840",
"acquiringBin": "408999",
"amount": "124.05",
"businessApplicationId": "AA",
"cardAcceptor": {
"address": {
"country": "USA",
"county": "San Mateo",
"state": "CA",
"zipCode": "94404"
},
"idCode": "CA-IDCode-77765",
"name": "Visa Inc. USA-Foster City",
"terminalId": "TID-9999"
},
"localTransactionDateTime": "'''+date+'''",
"merchantCategoryCode": "6012",
"pointOfServiceData": {
"motoECIIndicator": "0",
"panEntryMode": "90",
"posConditionCode": "00"
},
"recipientName": "rohan",
"recipientPrimaryAccountNumber": "4957030420210496",
"retrievalReferenceNumber": "412770451018",
"senderAccountNumber": "4653459515756154",
"senderAddress": "901 Metro Center Blvd",
"senderCity": "Foster City",
"senderCountryCode": "124",
"senderName": "Mohammed Qasim",
"senderReference": "",
"senderStateCode": "CA",
"sourceOfFundsCode": "05",
"systemsTraceAuditNumber": "451018",
"transactionCurrencyCode": "USD",
"settlementServiceIndicator": "9",
"colombiaNationalServiceData": {
"countryCodeNationalService": "170",
"nationalReimbursementFee": "20.00",
"nationalNetMiscAmountType": "A",
"nationalNetReimbursementFeeBaseAmount": "20.00",
"nationalNetMiscAmount": "10.00",
"addValueTaxReturn": "10.00",
"taxAmountConsumption": "10.00",
"addValueTaxAmount": "10.00",
"costTransactionIndicator": "0",
"emvTransactionIndicator": "1",
"nationalChargebackReason": "11"
}
}
''')

def callVisaDirect():
    r = requests.post(url,
                    # verify = ('put the CA certificate pem file path here'),
                    cert = (cert,key),
                    headers = headers,
                    auth = (user_id, password),
                    # data = body,
                    json=payload,
                    timeout=timeout)
    print(r.text)
    return r.text

if __name__ == '__main__':
    r=callVisaDirect()
    print(r.text)