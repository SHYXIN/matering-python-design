import unittest

from di_with_decorator import (
    NotificationSender,
    NotificationService,
    inject_sender,
)

class EmailSenderStub:
    def __init__(self):
        self.message_sent = []

    def send(self, message: str):
        self.message_sent.append(message)


class SMSSenderStub:
    def __init__(self):
        self.message_sent = []

    def send(self, message: str):
        self.message_sent.append(message)


class TestNotificationService(unittest.TestCase):
    def test_notify_with_email(self):
        email_stub = EmailSenderStub()

        service = NotificationService()
        service.sender = email_stub
        service.notify("Test Email Message")

        self.assertIn(
            "Test Email Message",
            email_stub.message_sent,
        )


    def test_notify_with_sms(self):
        sms_stub = SMSSenderStub()

        @inject_sender(SMSSenderStub)
        class CustomNotificationService:
            sender: NotificationSender = None

            def notify(self, message):
                self.sender.send(message)

        service = CustomNotificationService()
        service.sender = sms_stub
        service.notify("Test SMS Message")

        self.assertIn(
            "Test SMS Message", sms_stub.message_sent
        )

if __name__ == "__main__":
    unittest.main()
