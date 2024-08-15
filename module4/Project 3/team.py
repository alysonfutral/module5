# ALL CASES COVERED
# ALL TESTS PASSED
from identified_object import IdentifiedObject

class Team(IdentifiedObject):

    @property
    def name(self): # name prop needs a setter
        return self._name

    @name.setter
    def name(self, name): # setter for name()
        self._name = name

    @property
    def members(self): # read only prop
        return self._members


    #  initialization method that sets the oid and name properties
    #  as specified in the arguments
    #  (note: should call superclass constructor)
    def __init__(self, oid, name):
        super().__init__(oid) # calling super() from ancestor
        self._name = name
        self._members = [] # list of team members

    # ignore request to add team member that is already in members
    # Python Crash Course 2nd ed, pg76-77
    def add_member(self, member):
        if member in self._members: # check if member is in list of members
            return # if the team member is in the list, leave
        else: # if the team member is not in the list, add them
            self._members.append(member)


    # return the member of this team whose name equals s
    # (case sensitive) or None if no such member exists
    # M2-80 List Comp "transform" example, page 3,4,5
    def member_named(self, s):
        for member in self._members: # for members in the list
            if member.name == s: # if members name equals 's'
                return member
        return None # if no such member exists

    # remove the specified member from this team
    # Python Crash Course 2nd ed, pg40
    def remove_member(self, member):
        if member in self._members: # if member in specified list
            self._members.remove(member) # remove specified member



    # use the emailer.py argument to send an email to all members
    # of a team except those whose email address is None.
    # This method should send a single email so if the team
    # has N members, the recipient list will have N elements.
    def send_email(self, emailer, subject, message):
        # use a list comp to set recipients var as the list of emails
        # [expression for control_var in collection,IF MEMBERS EMAIL IS NOT NONE] --> send email
        recipients = [member.email for member in self._members if member.email is not None]
        # use emailer.py arg to send email to recipients
        emailer.send_plain_email(recipients, subject, message)



    # return a string like the following: "Team Name: N members"
    def __str__(self):
        return f"{self.name} {self.members} members"


