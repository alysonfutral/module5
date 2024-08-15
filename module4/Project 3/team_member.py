# all cases covered
# TESTS PASSED
from identified_object import IdentifiedObject

class TeamMember(IdentifiedObject):

    @property
    def name(self): # prop, needs setter
        return self._name

    @name.setter
    def name(self, name): # setter for name
        self._name = name

    @property
    def email(self): # prop, needs setter
        return self._email

    @email.setter
    def email(self, email): # setter for email
        self._email = email

    # initialization method that sets the oid,
    # name and email properties as specified in the arguments
    # (note: should call superclass constructor)
    def __init__(self, oid, name, email):
        super().__init__(oid)
        self._name = name
        self._email = email

    # use the emailer argument to send an email to to this member
    def send_email(self, emailer, subject, message):
        # use emailer.py arg to send email to THIS member
        # implement a list in emailer args [], which is this member to recieve the email
        emailer.send_plain_email([self.email], subject, message)

    # return a string like the following: "Name<Email>"
    def __str__(self): # test wants it formatted like this*
        return f"{self.name}<{self.email}>"


