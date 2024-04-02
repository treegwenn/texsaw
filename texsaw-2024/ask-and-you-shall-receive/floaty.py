import smtplib

class floaty:
    def __init__(self):
        self.email = "your-email-here"
        self.password = "your-password-here"
        self.flag = "real-flag-here"
        self.fake = "fake-flag-here"
        self.sendto = ""

#set who messege gets sent to
    def setSender(self, email):
        self.sendto = email

#Check Responds for flag or fake
    def checkResponds(self, responds):
        if "flag" in responds:
            self.sendFlag()
        else:
            self.sendFake()

#Send Flag if requested
    def sendFlag(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.email,self.password)
        server.sendmail(self.email, self.sendto, self.flag)
        server.quit()

#Send Fake messege if flag not requested
    def sendFake(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.email,self.password)
        server.sendmail(self.email, self.sendto, self.fake)
        server.quit()
