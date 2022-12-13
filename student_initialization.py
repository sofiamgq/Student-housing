from replit import db
import os
#os.system("pip install pwinput")
import pwinput

def initializeStudent(studentLogin, studentPassword, studentName, studentSurname, studentID):
  """This is the init function, which starts the class. It also contains the main data that the objects in the class will require, such as student email and age."""
  db[studentID] = dict()
  db[studentID]['studentLogin'] = studentLogin
  db[studentID]['studentPassword'] = studentPassword
  db[studentID]['studentName'] = studentName
  db[studentID]['studentSurname'] = studentSurname
  db[studentID]['studentEmail'] = None
  db[studentID]['studentPhoneNum'] = None
  db[studentID]['studentAge'] = None
  db[studentID]['studentYearOfEdu'] = None
  db[studentID]['studentResidPrefer'] = None
  db[studentID]['studentRoomPrefer'] = None
  db[studentID]['studentRoommatePrefer'] = None
  db[studentID]['studentSpecMedCond'] = None

def studentFullName(studentID):
  """This function combines the first name and the surname to get the full name."""
  return db[studentID]['studentName'] + ' ' + db[studentID]['studentSurname']

def getAllStudents():
  """This function allows the faculty member to view the names of all of the students."""
  studentList = []
  for elem in db.keys():
    if 'Student' in elem:
      studentList.append((elem, studentFullName(elem)))
  return studentList

def changeStudentEmail(currentUser):
  """This function allows students to change their email address."""
  email = input('Enter your email: ')
  while not('@' in email) or (' ' in email):
    print('Please input a valid email.')
    email = input('Enter your email: ')
  db[currentUser]['studentEmail'] = email

def changeStudentAge(currentUser):
  """This function allows a student to change their age."""
  age = input('Enter your age: ')
  flag = False
  while flag == False:
    try:
      int_age = int(age)
      flag = True
    except ValueError:
      print('Please input valid age.')
      age = input('Enter your age: ')
  db[currentUser]['studentAge'] = age

def changeStudentPhoneNum(currentUser):
  """This function allows a student to change their phone number."""
  phoneNum = input('Enter your phone number in format +XX...X: ')
  while phoneNum[0] != '+':
    print('Please input your phone number in the right format.')
    phoneNum = input('Enter your phone number: ')
  while not phoneNum[1:].isdigit():
    print('Please input your phone number in the right format.')
    phoneNum = input('Enter your phone number: ')
  db[currentUser]['studentPhoneNum'] = phoneNum

def changeStudentYearOfEdu(currentUser):
  """This function allows a student to change their year of education."""
  yearOfEdu = input('Enter your year of education (1, 2, 3 or 4): ')
  while not(yearOfEdu in ['1', '2', '3', '4']):
    print('Please enter valid year of education.')
    yearOfEdu = input('Enter your year of education (1, 2, 3 or 4): ')
  db[currentUser]['studentYearOfEdu'] = yearOfEdu

def changeStudentResidPrefer(currentUser):
  """This funcyion allows a student to change their residence preference."""
  residPrefer = input('Enter your residence preference (1 for Residence Hall A and 2 for Residence Hall B): ')
  while not(residPrefer in ['1', '2']):
    print('Please input your residence preference in the correct format.')
    residPrefer = input('Enter your residence preference (1 for Residence Hall A and 2 for Residence Hall B): ')
  db[currentUser]['studentResidPrefer'] = residPrefer

def changeStudentRoomPrefer(currentUser):
  """This function allows a student to update/change their room preference."""
  roomPrefer = input('Enter your room preference (1 for a single room and 2 for a double room): ')
  while not(roomPrefer in ['1', '2']):
    print('Please input your room preference in the correct format')
    roomPrefer = input('Enter your room preference (1 for a single room and 2 for a double room): ')
  db[currentUser]['studentRoomPrefer'] = roomPrefer

def changeStudentRoommatePrefer(currentUser):
  """This function allows a student to change their roommate preference."""
  if db[currentUser]['studentYearOfEdu'] == '1':
    print('We do not allow first-year students to choose a roommate, so you cannot set a rommate preference.')
    return
  elif db[currentUser]['studentYearOfEdu'] == None:
    print('You cannot set the rommate preference unless you set your year of education.')
  roommatePrefer = input('Enter your roommate preference (full name of the student you want to live with): ')
  studentList = getAllStudents()
  flag = False
  while flag == False:
    for student in studentList:
      if student[0] == roommatePrefer:
        flag = True
        break
    if flag == False:
      print('There is no such student on our system.')
      roommatePrefer = input('Enter your roommate preference (full name of the student you want to live with): ')
  db[currentUser]['studentRoommatePrefer'] = roommatePrefer

def changeStudentSpecMedCond(currentUser):
  """This function allows students to enter their specific medical conditions."""
  specMedCond = input('Enter your room preference: ')
  db[currentUser]['studentSpecMedCond'] = specMedCond