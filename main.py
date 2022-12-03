# coded some rough class stuff, mostly just thought we should get something down in replit. feel free to edit

from replit import db
# main screen. displays options: log in student, log in admin, create account student
class Student:
  def __init__(self, name, password, dormpref, smoker):
    self.name = name
    self.password = password
    self.dormpref = dormpref
    self.smoker = smoker

  def updateDormPref(self, newdormpref):
    return True

  def updateIsSmoker(self, bool):
    return True

  def returnIsSmoker(self):
    return self.IsSmoker

  def returnDormPref(self):
    return self.DormPref

class Admin:
  def __init__(self, name, password):
    self.name = name
    self.password = password


def studentLogIn():
  return True

def adminLogIn():
  return True

def newStudentAccount():
  return True


def MainScreen():
  mainScreenInput = input('Enter 1 to log in as student, 2 to log in as admin, 3 to create a new account.')
  if mainScreenInput == 1:
    studentLogIn()
  if mainScreenInput == 2:
    adminLogIn()
  if mainScreenInput == 3:
    newStudentAccount()
  else:
    print('value error. put this statement in a loop and restart')
  

    
# create account student:
  # application asks for an account name, asks for a password, checks in database if the account exists previously. If not, student account is created.

# from student account:
  # program displays options to update housing preferences. This means, for every value saved in the student class (init as null), can access and edit. Additionally, maybe an option to 'complete housing survey' and the program will automatically guide the student through updating all pieces of data in their instance of the student class.

# From admin account:
  # can view any data, compile reports on overall dataset. Has an option to generate housing preferences, which will run all existing student classes through some sort of algorithm and return housing assignments


