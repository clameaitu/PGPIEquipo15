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
    
    def build_msg(slef, order):
        msg = (
            f"Estimado {order.nombre},\n\n"
            f"Su pedido con codigo {order.codigo} ha sido tramitado con exito.\n\n"
            f"Para hacer un seguimiento de su pedido, puede introducir este codigo en nuestra pagina web.\n\n"
            f"Gracias por su compra.\n\n"
            f"Saludos cordiales,\nEl equipo de soporte"
        )
        return msg