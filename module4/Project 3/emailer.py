# do not test directly
# similar to singleton example in class, USE (CLS)

import yagmail # mod used to send emails


class Emailer:

    _sender_address = "" # store email address
    _sole_instance = None # store sole_instance

    # sets the class variable as specified
    @classmethod
    def configure(cls, sender_address):
        cls._sender_address = sender_address

    # return the only instance of this class
    @classmethod
    def instance(cls):
        if cls._sole_instance is None: # if sole_instance is none...
            cls._sole_instance = cls() # create an instance
            return cls._sole_instance

    # https://pypi.org/project/yagmail/#description
    # from the pypi.org website, example description
        # https://github.com/kootenpv/yagmail/blob/master/yagmail/__main__.py
    def send_plain_email(cls, recipients, subject, message):
        try: # attempt to send email using yagmail.STMP
            yag = yagmail.SMTP(cls._sender_address)
            yag.send(recipients, subject, message)
            print("Email sent!") # success
        except Exception as error: # unsuccessful
            print("An error occurred while sending.", error)



if __name__ == '__main__':
    Emailer.configure('alysonlfutral@gmail.com') # call configure() for senders address
    recipients = ['leighann98dance@gmail.com'] # to recieve the email
    subject = 'Testing for Yagmail Email' # subject of email
    message = 'Did this message go through? I do not know. Hopefully so!'
    emailer = Emailer.instance() # call instance() to return sole_instance of class
    emailer.send_plain_email(recipients, subject, message) # sends the email to recipitents including subject and message