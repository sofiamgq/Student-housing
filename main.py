from replit import db
import os
#os.system("pip install pwinput")
import pwinput
from student_initialization import *
from faculty_initialization import *
from housing_application import *
from housing_assignment import *

def condPassword(password):
  """This function checks if the conditions for the password are fulfilled. If they are, it returns True, then it can be verified in the functions of study sign up and add faculty member."""
  number= False
  characters= False
  uppercase= False
  specialCharacter= False 
  chars = '!”#$%&()*+,-./:;<=>?@[\]^_`{|}~'
  for i in password:
    if i.isdigit():
      number=True
    if i.isupper():
      uppercase=True
    if i in chars:
      specialCharacter=True
  if len(password)>=8:
    characters=True
  if number and characters and uppercase and specialCharacter:
    return True
  else:
    return False

def newStudentAccount():
  """This function allows users to create a new student account."""
  login = input('Choose your login: ')
  indicator = False
  while indicator == False:
    flag = True
    for elem in db.keys():
      if 'Student' in elem:
        if db[elem]['studentLogin'] == login:
          flag = False
          break
    if flag == False:
      print('Such login already exsists.')
      login = input('Choose your login: ')
    else:
      indicator = True
    print ('Your password MUST cobtain at least 8 characters, 1 uppercase letter, 1 number and 1 special character')
    password = pwinput.pwinput(prompt='Enter your password: ', mask='*')
    #print ('here')
    if condPassword(password):
      #print ('got here')
      verification =  pwinput.pwinput(prompt='Repeat your password: ', mask='*')
      while password != verification:
        print('The passwords do not match. Try again.')
        password = pwinput.pwinput(prompt='Enter your password: ', mask='*')
        verification =  pwinput.pwinput(prompt='Repeat your password: ', mask='*')
    else:
      print ('Your password does not fulfill the requirements. Please try again.')
      newStudentAccount()
  studentName = input('Enter your name: ')
  studentSurname = input('Enter your surname: ')
  studentID = 'Student' + str(db['NumOfStud'] + 1)
  initializeStudent(login, password, studentName, studentSurname, studentID)
  db['NumOfStud'] += 1
  print('Welcome to the system, ' + studentFullName(studentID) + '!')
  print('Your student ID:', studentID)
  return studentID

def studentLogIn():
  """This function allows a student to log into their account if it exists."""
  login = input('Enter your login: ')
  flag = False
  while flag == False:
    for elem in db.keys():
      if 'Student' in elem:
        if db[elem]['studentLogin'] == login:
          currentUser = elem
          flag = True
          break
    if flag == False:
      print('There is no user with such login.')
      login = input('Enter your login: ')
  password =  pwinput.pwinput(prompt='Enter your password: ', mask='*')
  while password != db[currentUser]['studentPassword']:
    print('The password is incorrect. Try again.')
    password =  pwinput.pwinput(prompt='Enter your password: ', mask='*')
  print('Welcome, ' + studentFullName(currentUser) + '!')
  return currentUser

def facultyLogIn():
  """This function allows a faculty member to log into their account if it exists."""
  login = input('Enter your login: ')
  flag = False
  while flag == False:
    for elem in db.keys():
      if 'Faculty' in elem:
        if db[elem]['facultyLogin'] == login:
          currentUser = elem
          flag = True
          break
    if flag == False:
      print('There is no user with such login.')
      login = input('Enter your login: ')
  password =  pwinput.pwinput(prompt='Enter your password: ', mask='*')
  while password != db[currentUser]['facultyPassword']:
    print('The password is incorrect. Try again.')
    password =  pwinput.pwinput(prompt='Enter your password: ', mask='*')
  print('Welcome, ' + facultyFullName(currentUser) + '!')
  return currentUser

def studentPage(currentUser):
  """This function shows the student portal once they are logged in. It asks them what they want to do inside the page."""
  print('Enter 1 to start/edit your housing application\nEnter 2 to view your housing application\nEnter 3 to view the room information\nEnter 4 to log out')
  studentPageInput = input('Your answer: ')
  while not(studentPageInput in ['1', '2', '3', '4']):
    print('Please enter a valid input.')
    studentPageInput = input('Your answer: ')
  if studentPageInput == '1':
    manageHousingApplication(currentUser)
  elif studentPageInput == '2':
    viewHousingApplication(currentUser, currentUser)
  elif studentPageInput == '3':
    print('Available residence halls:\n- Residence Hall A\n- Residence Hall B\nAvailable Rooms:\n- A double room for 2 people\n- A single room for 1 person')
    studentPage(currentUser)
  elif studentPageInput == '4':
    logout()

def addNewFaculty(currentUser):
  """This function allows faculty members to add more faculty members if they are not already in the system."""
  login = input('Choose a login: ')
  indicator = False
  while indicator == False:
    flag = True
    for elem in db.keys():
      if 'Faculty' in elem:
        if db[elem]['facultyLogin'] == login:
          flag = False
          break
    if flag == False:
      print('Such login already exsists.')
      login = input('Choose a login: ')
    else:
      indicator = True
  print ('Your password MUST cobtain at least 8 characters, 1 uppercase letter, 1 number and 1 special character')
  password = pwinput.pwinput(prompt='Enter your password: ', mask='*')
  #print ('here')
  if condPassword(password):
    #print ('got here')
    verification =  pwinput.pwinput(prompt='Repeat your password: ', mask='*')
    while password != verification:
      print('The passwords do not match. Try again.')
      password = pwinput.pwinput(prompt='Enter your password: ', mask='*')
      verification =  pwinput.pwinput(prompt='Repeat your password: ', mask='*')
  else:
    print ('Your password does not fulfill the requirements. Please try again.')
    addNewFaculty(currentUser)
  facultyName = input('Enter new faculty member\'s name: ')
  facultySurname = input('Enter new faculty member\'s surname: ')
  facultyID = 'Faculty' + str(db['NumOfFac'] + 1)
  initializeFaculty(login, password, facultyName, facultySurname, facultyID)
  db['NumOfFac'] += 1
  print('A new faculty member, ' + facultyFullName(facultyID) + ', was successfully added to the system.')
  facultyPage(currentUser)

def facultyPage(currentUser):
  """This function is the faculty portal, and it asks the user what they want to do such as managing students or adding nee facukty members."""
  print('Enter 1 to access student information\nEnter 2 to add a new faculty member\nEnter 3 to get a housing plan\nEnter 4 to log out')
  facultyPageInput = input('Your answer: ')
  while not(facultyPageInput in ['1', '2', '3', '4']):
    print('Please enter a valid input.')
    facultyPageInput = input('Your answer: ')
  if facultyPageInput == '1':
    accessStudentInfo(currentUser)
  elif facultyPageInput == '2':
    addNewFaculty(currentUser)
  elif facultyPageInput == '3':
    generateHousingAssignments()
  elif facultyPageInput == '4':
    logout()

def mainscreen():
  """This function is the main screen, which is the first page that users visualize, which asks them to either log in or sign up."""
  print('Welcome to the Student Housing Management System!')
  print('Enter 1 to create a new account\nEnter 2 to log in as a student\nEnter 3 to log in as a faculty member')
  mainScreenInput = input('Your answer: ')
  while not(mainScreenInput in ['1', '2', '3', '4']):
    print('Please enter a valid input.')
    mainScreenInput = input('Your answer: ')
  if mainScreenInput == '1':
    currentUser = newStudentAccount()
    studentPage(currentUser)
  elif mainScreenInput == '2':
    currentUser = studentLogIn()
    studentPage(currentUser)
  elif mainScreenInput == '3':
    currentUser = facultyLogIn()
    facultyPage(currentUser)

def preparations():
  """This function makes sure that there is at least one faculty member to be able to add more faculty members in the future. It also helps to keep track of the number of students and the number of faculty members."""
  if not('NumOfStud' in db.keys()):
    db['NumOfStud'] = 0
    db['NumOfFac'] = 0
    for elem in db.keys():
      if 'Student' in elem:
        db['NumOfStud'] += 1
      elif 'Faculty' in elem:
        db['NumOfFac'] += 1
  if db['NumOfFac'] == 0:
    initializeFaculty('FirstAdmin', 'Qwerty123', 'First', 'Administrator', 'Faculty1')
    db['NumOfFac'] += 1
    
      
#initializeFaculty('FirstAdmin', 'Qwerty123', 'First', 'Administrator', 'Faculty1')  
#db.clear()

db.clear()
initializeStudent('studentLogin1', 'studentPassword1', 'Simon', 'Rutter', 'Student1')
initializeStudent('studentLogin2', 'studentPassword2', 'Michael', 'Cornell', 'Student2')
initializeStudent('studentLogin3', 'studentPassword3', 'Thomas', 'Boyle', 'Student3')
initializeStudent('studentLogin3', 'studentPassword3', 'Astrid', 'Faustman', 'Student4')
initializeStudent('studentLogin3', 'studentPassword3', 'Tugo', "'The King'", 'Student6')
initializeStudent('studentLogin3', 'studentPassword3', 'Teo', 'Blind', 'Student5')

db['Student1']['studentResidPrefer'] = 'dorm A'
db['Student2']['studentResidPrefer'] = 'dorm A'
db['Student3']['studentResidPrefer'] = 'dorm A'
db['Student4']['studentResidPrefer'] = 'dorm A'

preparations()
mainscreen()