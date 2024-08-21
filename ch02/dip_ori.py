class Email:
    def send_email(self, message):
        print(f"Sending email: {message}")


class Notification:
    def __init__(self):
        self.email = Email()

    def send(self, message):
        self.email.send_email(message)
