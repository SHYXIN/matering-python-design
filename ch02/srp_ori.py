class Report:

    def __init__(self, content):
        self.content = content

    def generate(self):
        print(f"Report content: {self.content}")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(self.contnet)
