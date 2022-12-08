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
    self.__studentYearOfEdu= None
    self.__studentResidPrefer = None
    self.__studentRoomPref = None
    self.__studentSpecMedCond= None
    self.__studentResidPrefer= None
    self.__studentRoomPrefer= None

  def getPhoneNum(self):
    return self.__studentPhoneNum

  def getEmail(self):
    return self.__studentEmail

  def getAge(self):
    return self.__studentAge

  def getYearOfEdu():
    return self.__studentYearOfEdu

  def getSpecMedCond():
    return self.__studentSpecMedCond

  def getStudentResidPrefer():
    return self.__studentResidPrefer

  def getRoomPref(self):
    return self.__studentRoomPref

  def modifyApplication(self):
    return True

  def submitNewApplication(self):
    return True

  def showRoomInfo (self):
    return True

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
  
  def housingApplication(self):
    answerEmail=input('Please enter your email: ')
    self.__studentEmail = answerEmail
    answerPhone=input('Please enter your phone number: ')
    self.__studentPhoneNum = answerPhone
    answerAge= input('Please enter your age: ')
    self.__studentAge = answerAge
    answerYearOfEdu= input('Please enter your year of education: ')
    self.__studentYearOfEdu=answerYearOfEdu
    answerMedicalConditions= input('Please enter if you have any medical conditions: ')
    self.__studentSpecMedCond=answerMedicalConditions
    answerResidencePreference=input('Please tell us if you have any residence preference: ')
    self.__studentResidPrefer= answerResidencePreference
    answerRoomPreference= input('Please tell us if you have any room preference: ')
    self.__studentRoomPrefer=answerRoomPreference 

class Faculty(User):
  def __init__(self, userLogin, userPassword, userName, userSurname):
    super().__init__(userLogin, userPassword, userName, userSurname)

  def showAllStudentNames(self):
    for student in db.keys():
      return student
    
  def showSpecificStudentInfo(self, userName):
# We should have a user ID system implmented, rather than looking up students by first and last name. This will stop the issue of having duplicate students with the same name. If there is a duplicate, this function should present faculty with the option to pick which student they mean (for example, by also displaying birthdate or another identifying piece of info)
    return True



  def createHousingPlan():
    # run through some algorithm to find and return the ideal housing plan
    return True
    
def addNewFacultyMember():
  if not('faculty' in db.keys()):
    db['faculty'] = []
  login = input('Choose your login: ')
  indicator = False
  while indicator == False:
    flag = True
    for user in db['faculty']:
      if user.__userLogin == login:
        flag = False
    if flag == False:
      print('Such login already exsists.')
      login = input('Choose your login: ')
    else:
      indicator = True
  password = input('Choose your password: ')
  verification = input('Repeat your password: ')
  while password != verification:
    print('The passwords do not match. Try again.')
    password = input('Choose your password: ')
    verification = input('Repeat your password: ')
  facultyName = input('Enter your name: ')
  facultySurname = input('Enter your surname: ')
  newFaculty = Faculty(login, password, facultyName, facultySurname)
  db['faculty'].add(newFaculty)

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


def facultyLogIn():
  username = input('What is your username: ')
  for faculty in db['faculty']:
    if faculty.getUserName() == username:
      continue
    else:
      print('This username does not exist.')
      return False
      password = input('Enter password: ')
  if db['faculty'].getPassword() == password:
    print('Login successful.')
    return True
  else:
    print('Incorrect password.')
    return False

def studentLogIn():
  username = input('What is your username: ')
  for student in db['students']:
    if student.getUserName() == username:
      continue
    else:
      print('This username does not exist.')
      return False
      password = input('Enter password: ')
  if db['students'].getPassword() == password:
    print('Login successful.')
    return True
  else:
    print('Incorrect password.')
    return False

def adminLogIn():
  print ('Welcome to the faculty log in portal!')
  username=input('Please enter your username: ')
  if username in db:
    password=input('Please enter your password: ')
    if db[username]==password:
      'Welcome!'
    else:
      print('Please try again.')
      facultyLogIn()
  else:
    print('Please try again.')
    facultyLogIn()
  # just check with admin, if data exists and password/username are matching

def logOut():
  print('You have successfully logged out')
  mainScreen()

def newStudentAccount():
  if not('students' in db.keys()):
    db['students'] = []
  login = input('Choose your login: ')
  indicator = False
  while indicator == False:
    flag = True
    for user in db['students']:
      if user.__userLogin == login:
        flag = False
    if flag == False:
      print('Such login already exsists.')
      login = input('Choose your login: ')
    else:
      indicator = True
  password = input('Choose your password: ')
  verification = input('Repeat your password: ')
  while password != verification:
    print('The passwords do not match. Try again.')
    password = input('Choose your password: ')
    verification = input('Repeat your password: ')
  studentName = input('Enter your name: ')
  studentSurname = input('Enter your surname: ')
  newStudent = Student(login, password, studentName, studentSurname)
  db['students'].add(newStudent)
  return newStudent


def mainScreen():
  print('Welcome to the Student Housing Management System!')
  print('Enter 1 to log in as student, enter 2 to sign up, enter 3 to log in as a faculty member, enter 4 to log out.')
  mainScreenInput = input('Your answer: ')
  if mainScreenInput == '1':
    studentLogIn()
  elif mainScreenInput == '2':
    newStudentAccount()
  elif mainScreenInput == '3':
    facultyLogIn()
  elif mainScreenInput=='4':
    logOut()
  else:
    print('Please enter a valid input and try again.')
    mainScreen()
  