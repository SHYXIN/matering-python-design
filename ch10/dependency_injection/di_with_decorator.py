from typing import Protocol


class NotificationSender(Protocol):
    def send(self, message: str):
        """Send a notification with the given message"""
        ...


class EmailSender:
    def send(self, message: str):
        # Here you might integrate with an email service API
        print(f"Sending Email: {message}")

class SMSSender:
    def send(self, message: str):
        # Here you might integrate with an SMS service API
        print(f"Sending SMS: {message}")


def inject_sender(sender_cls):
    def decorator(cls):
        cls.sender = sender_cls()
        return cls
    return decorator

@inject_sender(EmailSender)
class NotificationService:
    sender: NotificationSender = None  # This will be set by the decorator

    def notify(self, message):
        self.sender.send(message)


# # 手动应用装饰器
# NotificationService = inject_sender(EmailSender)(NotificationService)

# # 创建 NotificationService 实例并使用
# notification_service = NotificationService()
# notification_service.notify("Hello, this is a test notification")

if __name__ == "__main__":
    service = NotificationService()
    service.notify("Hello, this is a test notification")
