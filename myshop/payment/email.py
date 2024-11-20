import smtplib

class EmailService():
    def __init__(self, sender: str, password: str):
        self.sender = sender
        self.password = password

    def send_mail(self, receiver: str, message: str, subject: str = ""):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.sender, self.password)
        msg = f'Subject: {subject}\n\n{message}'
        server.sendmail(self.sender, receiver, msg)
        server.quit()