'''
Create a parent class Notification with a method send(). Override this method in EmailNotification, SMSNotification, and PushNotification
to display different messages
'''

class Notification:
    def send(self):
        print("Sending the Notification")

class EmailNotification(Notification):
    def send(self):
        print("Sending from Email notification ")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS Notification")

class PushNotification(Notification):
    def send(self):
        print("Sending from Push Notification")


EN = EmailNotification()
SMSN = SMSNotification()
PN = PushNotification()

EN.send()
SMSN.send()
PN.send()

# Run time polymorphism because at runtime it decides which send() method to execute.