# coded some rough class stuff, mostly just thought we should get something down in replit. feel free to edit
from replit import db
class User:
  def __init__(self, userLogin, userPassword, userName, userSurname):
    self.__userLogin = userLogin
    self.__userPassword = userPassword
    self.__userName = userName
    self.__userSurname = userSurname

  def getFullName(self):
    return self.__userName + ' ' + self.__userSurname

class Student(User):
  def __init__(self, userLogin, userPassword, userName, userSurname, studentEmail, studentPhoneNum, studentAge, studentResidPrefer, studentRoomPref):
    User.__init__(self, userLogin, userPassword, userName, userSurname)
    self.__studentEmail = studentEmail
    self.__studentPhoneNum = studentPhoneNum
    self.__studentAge = studentAge
    self.__studentResidPrefer = studentResidPrefer
    self.__studentRoomPref = studentRoomPref

  def getPhoneNum(self):
    return self.__studentPhoneNum

  def getEmail(self):
    return self.__studentEmail

  def modifyApplication(self):
    return True

  def getRoomPref(self):
    return self.__studentRoomPref

  class Faculty(User):
    def __init__(self, userLogin, userPassword, userName, userSurname):
      User.__init__(self, userLogin, userPassword, userName, userSurname)

  def showAllStudentNames(self):
    return True

  def showSpecificStudentInfo(self, userName):
# We should have a user ID system implmented, rather than looking up students by first and last name. This will stop the issue of having duplicate students with the same name. If there is a duplicate, this function should present faculty with the option to pick which student they mean (for example, by also displaying birthdate or another identifying piece of info)
    return True

  def addNewFacultyMember():
    # init new instance of faculty class
    return True

  def createHousingPlan():
    # run through some algorithm to find and return the ideal housing plan
    return True

class UpperClassStudent(Student):
  def __init__(self, userLogin, userPassword, userName, userSurname, studentEmail, studentPhoneNum, studentAge, studentResidPrefer, studentRoomPref, studentRoommatePref):
    Student.__init__(self, userLogin, userPassword, userName, userSurname, studentEmail, studentPhoneNum, studentAge, studentResidPrefer, studentRoomPref)
    self.__studentRoommatePref = studentRoommatePref

  def getStudentRoommatePref(self):
    return self.__studentRoommatePref

  def updateStudentRoommatePref(self, newPref):
    self.__studentRoommatePref = newPref





test = UpperClassStudent('userLogin', 'userPassword', 'userName', 'userSurname', 'studentEmail', 'studentPhoneNum', 'studentAge', 'studentResidPrefer', 'studentRoomPref', 'studentRoommatePref')
print(test.getStudentRoommatePref())

def studentLogIn():
  # check if data exists and password/username are matching
  return True

def adminLogIn():
  # just check with admin, if data exists and password/username are matching
  return True

def newStudentAccount():
  # gather info here

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
  