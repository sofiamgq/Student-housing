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
  def __init__(self, userLogin, userPassword, userName, userSurname):
    super().__init__(userLogin, userPassword, userName, userSurname)
    self.__studentEmail = None
    self.__studentPhoneNum = None
    self.__studentAge = None
    self.__studentResidPrefer = None
    self.__studentRoomPref = None

  def getPhoneNum(self):
    return self.__studentPhoneNum

  def getEmail(self):
    return self.__studentEmail

  def modifyApplication(self):
    return True

  def getRoomPref(self):
    return self.__studentRoomPref

  def setStudentEmail(self, email):
    self.__studentEmail = email

  def setStudentPhoneNum(self, phoneNum):
    self.__studentPhoneNum = phoneNum

  def setStudentAge(self, age):
    self.__studentAge = age

  def setStudentResidPrefer(self, residPrefer):
    self.__studentResidPrefer = residPrefer

  def setRoomPrefer(self, roomPrefer):
    self.__studentRoomPref = roomPrefer

  class Faculty(User):
    def __init__(self, userLogin, userPassword, userName, userSurname):
      super().__init__(userLogin, userPassword, userName, userSurname)

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
  def __init__(self, userLogin, userPassword, userName, userSurname):
    super().__init__(userLogin, userPassword, userName, userSurname)
    self.__studentRoommatePref = None

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

def mainScreen():
  print('Welcome to the Student Housing Management System!')
  print('Enter 1 to log in as student, enter 2 to sign up, enter 3 to log in as a faculty member, enter 4 to log out.')
  mainScreenInput = input('Your answer: ')
  if mainScreenInput == '1':
    studentLogIn()
  elif mainScreenInput == '2':
    studentSignUp()
  elif mainScreenInput == '3':
    facultyLogIn()
  elif mainScreenInput=='4':
    logOut()
  else:
    print('Please enter a valid input and try again.')
    mainScreen()
  