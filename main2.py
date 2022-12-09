# coded some rough class stuff, mostly just thought we should get something down in replit. feel free to edit
from replit import db

db['StudentCount'] = 0
db['FacultyCount'] = 0

for elem in db.keys():
  if elem[:7] == 'student':
    db['StudentCount'] += 1
  elif elem[:7] == 'faculty':
    db['FacultyCount'] += 1

class User:
  def __init__(self, userLogin, userPassword, userName, userSurname):
    """This is the in it function, which starts the class. It also contains the main data that the objects in the class will require such as user name and password."""
    self.__userLogin = userLogin
    self.__userPassword = userPassword
    self.__userName = userName
    self.__userSurname = userSurname

  def getFullName(self):
    """This function combines the first name and the surname to get the full name. """
    return self.__userName + ' ' + self.__userSurname

  def getUserLogin(self):
    return self.__userLogin

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

  def getYearOfEdu(self):
    return self.__studentYearOfEdu

  def getSpecMedCond(self):
    return self.__studentSpecMedCond

  def getStudentResidPrefer(self):
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
    answerEmailVer= False
    answerEmail=input('Please enter your email: ')
    if ' ' not in answerEmail and "@" in answerEmail:
      answerEmailVer= True
    while answerEmailVer== False:
      print ('Please enter a valid email.')
      answerEmail=input('Please enter your email: ')    
    if answerEmailVer== True:
      self.__studentEmail = answerEmail
    answerPhone=input('Please enter your phone number: ')
    answerPhoneVer= False
    if len(answerPhone)==10 and type(int(answerPhone))==int:
       answerPhoneVer= True
    while answerPhoneVer== False:
      print('Your phone number must have 10 numbers and must only contain numbers.')
      answerPhone=input('Please enter your phone number: ')
    if answerPhoneVer==True:
      self.__studentPhoneNum = answerPhone

    answerAgeVer=False
    answerAge= input('Please enter your age: ')
    if int(answerAge)>=18:
      answerAgeVer=True
    while answerAgeVer==False:
      print('You must be at least 18 years old')
      answerAge= input('Please enter your age: ')
    if answerAgeVer==True:
      self.__studentAge = answerAge

    answerYearOfEdu=False
    answerYearOfEdu= input('Please enter your year of education: ')
    if len(answerYearOfEdu)==4 and type(int(answerYearOfEdu))==int:
      answerYearOfEduVer=True
    while answerYearOfEduVer==False:
      print('Your answer must contain 4 digits.')
      answerYearOfEdu = input('Please enter your year of education: ')
    if answerYearOfEduVer==True:
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





def studentLogIn():
  username = input('What is your username: ')
  for item in db.keys():
    if 'student' in item:
      print(db[item])
      if db[item].getUserLogin() == username:
        userKey = item
        continue
    else:
      print('This username does not exist.')
      return False
      password = input('Enter password: ')
  if db[userKey].getPassword() == password:
    print('Login successful.')
    return True
  else:
    print('Incorrect password.')
    return False

def facultyLogIn():
  print ('Welcome to the faculty log in portal!')
  username=input('Please enter your username: ')
  for instance in db[db.keys()]:
    if instance.getUserLogin() == username:
      password=input('Please enter your password: ')
      if instance.getPassword() == password:
        'Welcome!'
      else:
        print('Please try again.')
        facultyLogIn()
    else:
      print('Please try again.')
      facultyLogIn()

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
  login = input('Choose your login: ')
  indicator = False
  while indicator == False:
    flag = True
    for user in db.keys():
      if user[:7] == 'student' or user[:7] == 'faculty':
        if db[user].getUserLogin() == login:
          flag = False
          break
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
  studentID = 'student' + str(db['StudentCount'] + 1)
  print('Welcome to the system!')
  print('Your student ID:', studentID)
  newStudent = Student(login, password, studentName, studentSurname)
  db[studentID] = newStudent


def mainScreen():
  print('Welcome to the Student Housing Management System!')
  print('Enter 1 to create a new account, enter 2 to log in as a student, enter 3 to log in as a faculty member, enter 4 to log out.')
  mainScreenInput = input('Your answer: ')
  if mainScreenInput == '1':
    newStudentAccount()
  elif mainScreenInput == '2':
    studentLogIn()
  elif mainScreenInput == '3':
    facultyLogIn()
  elif mainScreenInput=='4':
    logOut()
  else:
    print('Please enter a valid input and try again.')
    mainScreen()


def displayAllStudents():
  #Creates bugs, needs correction
  for item in db.keys():
    if item[:7] == 'student':
      print(db[item].getFullName())

# this is a model for how we will have student keys
James = UpperClassStudent('userLogin', 'userPassword', 'userName', 'userSurname')
db['student' + str(db['StudentCount'])] = James
print(db['student1'].getUserLogin())

print(db.keys())
mainScreen()