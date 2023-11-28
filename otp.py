import requests

import random
import math

url = "https://api.sendchamp.com/api/v1/whatsapp/message/send"
payload = {
  "custom_data": {
    "Body": {
      "1": "Damilola",
      "2": "Olotu",
      "3": "Lagos"
    }
  },
  "sender": "2347067959173",
  "recipient": "917355057737",
  "template_code": "TEMPLATE_CODE",
  "type": "template"
}
headers = {
  "Accept": "application/json",
  "Content-Type": "application/json",
  "Authorization": "Bearer <Access Key>"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)

def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

print("Your OTP is:", generateOTP())

import requests

servicePlanId = ""
apiToken = ""
sinchNumber = ""
toNumber = "+917355057737"
url = "https://us.sms.api.sinch.com/xms/v1/" + servicePlanId + "/batches"

payload = {
  "from": sinchNumber,
  "to": [
    toNumber
  ],
  "body": "Hello how are you"
}

headers = {
  "Content-Type": "application/json",
  "Authorization": "Bearer " + apiToken
}

response = requests.post(url, json=payload, headers=headers)

data = response.json()
print(data)