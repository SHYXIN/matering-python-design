import hashlib
import abc

class SensitiveInfo(abc.ABC):
    def __init__(self):
        self.users = ["nick", "tom", "ben", "mike"]

    def read(self):
        nb = len(self.users)
        print(f"There are {nb} users: {' '.join(self.users)}")

    def add(self, user):
        self.users.append(user)
        print(f"Added user {user}")

class Info:
    """Protection proxy to SensitiveInfo"""

    _instance = None  # Singleton instance of SensitiveInfo

    def __init__(self):
        if not Info._instance:
            Info._instance = SensitiveInfo()
        self.protected = Info._instance
        self.secret_hash = hashlib.sha256("0xdeadbeef".encode()).hexdigest()

    def read(self):
        self.protected.read()

    def add(self, user):
        sec = input("What is the secret? ")
        sec_hash = hashlib.sha256(sec.encode()).hexdigest()
        if sec_hash == self.secret_hash:
            self.protected.add(user)
        else:
            print("That's wrong!")

    def remove(self, user):
        sec = input("What is the secret? ")
        sec_hash = hashlib.sha256(sec.encode()).hexdigest()
        if sec_hash == self.secret_hash:
            if user in self.protected.users:
                self.protected.users.remove(user)
                print(f"Removed user {user}")
            else:
                print(f"User {user} not found!")
        else:
            print("That's wrong!")

def main():
    info = Info()
    while True:
        print("1. Read list |==| 2. Add user |==| 3. Remove user |==| 4. Quit")
        key = input("Choose option: ")
        if key == "1":
            info.read()
        elif key == "2":
            name = input("Choose name: ")
            info.add(name)
        elif key == "3":
            name = input("Choose name: ")
            info.remove(name)
        elif key == "4":
            exit()
        else:
            print(f"Unknown option: {key}")

if __name__ == "__main__":
    main()
