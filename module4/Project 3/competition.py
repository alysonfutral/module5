# ALL TESTS PASSING
from datetime import datetime
from identified_object import IdentifiedObject

class Competition(IdentifiedObject):

    # list containing two teams that are competing against each other
    @property
    def teams_competing(self): # no setter
        return self._teams_competing


    #  optional (may be None) -- a Python datetime objects
    #  (not a string!) indicating when the competition will begin.
    @property
    def date_time(self): # prop, needs setter
        return self._date_time

    @date_time.setter
    def date_time(self, date_time): # date_time setter
        self._date_time = date_time

    # prop, needs setter
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location): # location setter
        self._location = location

    # initialization method that sets the oid, teams,
    # location and date_time properties as specified in the
    # arguments (note: should call superclass constructor).
    # Note: teams should be a list.  See above for the type of
    # the datetime argument.
    def __init__(self, oid, teams, location, date_time):
        super().__init__(oid)
        self._teams_competing = teams
        self._location = location
        # "date_time may be None," set format as m/d/yy h:m
        # used ternary operation to determine if date_time should be omitted
        # use string parse time for objects to print in correct format
        self._date_time = date_time # if date_time is None else datetime.strptime(date_time, "%m/%d/%Y %H:%M")

    # use the emailer argument to send an email to all members
    # of all teams in this competition without duplicates.
    # That is, a team member may be on multiple teams that
    # may be competing against each other.  Only send one email
    # to each team member on all of the teams in this competition.
    # This method should send a single email so if the teams have
    # N and M members respectively, the recipient list will have
    # N+M elements assuming all of the members were distinct.
    # If the teams have S "shared" members then we'd expect a single
    # email with N+M-S recipients.
    def send_email(self, emailer, subject, message):
        send_emails = [] # create list to store emails

        for team in self.teams_competing: # loop through each team competing
            for member in team.members: # loop through each member of specific team
                # check if team members email is not None and that the team members
                # email has not already recieved an email to ensure no team member
                # recieves them twice (duplicates)
                if member.email is not None and member.email not in send_emails:
                    # if true, append new email to email list []
                    send_emails.append(member.email)

        # once the loops above have completed, the emails can be sent to the team members
        for email in send_emails:
            emailer.send_plain_email(email, subject, message)


    # return a string like the following: "Competition at location
    # on date_time with N teams" (note: date_time may be None in
    # which case just omit the "on date_time" part.  If present, format
    # the date_time property similar to the following example
    # "12/31/1995 19:30".
    def __str__(self):
        if self.date_time is not None:
            # format the string using strf to allow correct layout
            date_time_format = self.date_time.strftime("%m/%d/%Y %H:%M")
            return f"Competition at {self.location} on {date_time_format} with {self.teams_competing} teams"
        else: # omit datetime if None
            return f"Competition at {self.location} with {self.teams_competing} teams"