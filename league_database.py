# pickle mod permits loading and saving of most object types
# pickle preserves object identity when multiple references to the same object are pickled/unpickled
import os.path # used to determine if file exists and to rename file in save()
import pickle
import csv # imported for reading and writing csv file

# create a main in lieu of tests
# utilize singleton_pattern for following methods
class LeagueDatabase:
    _sole_instance = None

    # returns the sole instance of this database, creating one if it doesn't exist yet
    @classmethod
    def instance(cls):
        if cls._sole_instance is None: # if sole instance is none
            cls._sole_instance = cls() # create one
            return cls._sole_instance # return the sole instance

    # creates a list for _leagues
    def __init__(self):
        self._leagues = []

    # similar method as class example, 'rb' read in binary for loading
    @classmethod
    def load(cls, file_name):
        try: # attempt to load data from file and store into _sole_instance
            # open using read in binary 'rb'
            with open(file_name, mode='rb') as file:
                return pickle.load(file) # load data from file (pickle)
            # return console message if filenotfound
        except FileNotFoundError:
            print('File not found.')

    # list of leagues being managed
    @property
    def leagues(self):
        return self._leagues

    # private variable holding last id number
    def _last_oid(self):
        self._last_oid = 0

    # add the specified league to the leagues list
    def add_league(self, league):
        if league not in self.leagues:
            self._leagues.append(league)

    # remove the specified league from the leagues list.
    # If league is not in the leagues list, simply do nothing (not an error).
    def remove_league(self, league):
        if league in self._leagues:
            self._leagues.remove(league)

    # return the league with the given name or None of no such league exists
    def league_named(self, name):
        for league in self._leagues: # iterate through league
            if league == name: # if league equals given name
                return league # return the league
        return None # else...

    #  increment _last_id and return its new value (used to generate oid's for your objects)
    def next_oid(self):
        self._last_oid += 1 # increment last id
        return self._last_oid

    #  save this database on the specified file.
    #  Before saving, check if the file exists and if it does,
    #  rename it to file_name with ".backup" added.
    #  Learning Python by Mark Lutz 4th ed., page 236
    #  'wb' opens file in binary format for writing, used for dump
    # https://pynative.com/python-rename-file/#:~:text=renaming%20a%20file-,Rename%20a%20file%20after%20checking%20whether%20it%20exists,function%20before%20renaming%20a%20file.
    def save(self, file_name):
        # os is a mod that provides file usage options such as checking existing files and renaming
        if os.path.exists(file_name): # does it exist?
            os.rename(file_name, file_name + ".backup") # if so, rename file_name
            # open using write in binary 'wb'
        with open(file_name, 'wb') as file:
            # "Write the pickled representation of the object obj to the open file object file"
            pickle.dump(self._sole_instance, file)

    # load the teams and team members in a league from a CSV formatted file.
    # The file will contain three columns: team name, team member name, email.
    # The first line of the file will be a "header" line and should be ignored.
    # The file will be UTF-8 encoded and may contain non-ASCII text.
    # Note that the first argument to this method must be a league object, not the name of a league.
    # If an error occurs while loading a league, display a message on the console.
    # https://www.tutorialspoint.com/How-to-read-and-write-unicode-UTF-8-files-in-Python
    # https://stackoverflow.com/questions/904041/reading-a-utf8-csv-file-with-python
    # https://docs.python.org/3/library/csv.html
    # https://alexwlchan.net/2018/reading-a-utf8-encoded-csv/
    def import_league_teams(self, league, file_name):
        try: # open file in csv formatted file (encoding utf-8)
            with open(file_name, 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file, header=None) # create reader and ignore header
                # set the three columns names and iterate through csv
                for three_columns in csv_reader:
                    # get data
                    team_name, team_member_name, email = three_columns
                    self.add_league(team_name) # add team to league
                    league.add_league(team_member_name, email) # add team member to league
        except Exception as error:
            print("Error occurs while writing league.", error)



    # write the specified league to a CSV formatted file.
    # The first line of the file must be a "header" row containing the following text (without the leading spaces):
    # Team name, Member name, Member email. If an error occurs while writing a league, display a message on the console.
    # https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/
    # https: // docs.python.org / 3 / library / csv.html
    def export_league_teams(self, league, file_name):
        try: # attempt to open and write data (encoding utf-8)
            with open(file_name, 'w', encoding='utf-8') as file:
                csv_writer = csv.writer(file) # create writer
                # write all the elements in rows using writerows()
                csv_writer.writerows(["Team name", "Member name", "Member email"])
        except Exception as error:
            print("Error occurs while writing league.", error)













