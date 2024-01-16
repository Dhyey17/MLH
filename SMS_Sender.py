# import requests
# from tkinter import *
# from tkinter import messagebox
# 
# 
# def send():
#     url = "https://www.fast2sms.com/dev/bulkV2"
#     querystring = {"authorization": "btYUDF3u4ljSPqaWZdhTMfJQr6oi8IRgx1pXzE27LeV5G9wsCcSGaP8AR4MvcextQwlu2YEpmJOV19Cq",
#                    "message": f"{message}", "language": "english", "route": "q", "numbers": f"{reciever_num}"}
#     headers = {
#         'cache-control': "no-cache"
#     }
#     
#     response = requests.request("GET", url, headers=headers, params=querystring)
#     
#     messagebox.showinfo("SMS Sender", response.text)
# 
# 
# root = Tk()
# root.geometry("300x230")
# root.title("SMS Sender")
# 
# reciever_num = StringVar()
# 
# numInput = Entry(root, width=20, textvariable=reciever_num)
# numInput.place(x=115, y=20)
# numLbl = Label(root, text="Receiver's Number: ")
# numLbl.place(x=4, y=20)
# 
# msgTxtBox = Text(root, height=5, width=20)
# message = msgTxtBox.get("1.0")
# msgLbl = Label(root, text="Message: ")
# msgTxtBox.place(x=115, y=60)
# msgLbl.place(x=4, y=60)
# 
# btn = Button(root, text='Send', bd='5', command=send)
# btn.place(x=130, y=180)
# root.mainloop()

import requests

reciver_num = input("Enter mobile number(without country code) you want to send message (Indian numbers only): ")
message = input("Enter the message you want to send: ")

url = "https://www.fast2sms.com/dev/bulkV2"

querystring = {"authorization": "btYUDF3u4ljSPqaWZdhTMfJQr6oi8IRgx1pXzE27LeV5G9wsCcSGaP8AR4MvcextQwlu2YEpmJOV19Cq",
               "message": f"{message}", "language": "english", "route": "q", "numbers": f"{reciver_num}"}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring, timeout=60)

print(response.text)
