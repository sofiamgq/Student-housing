from replit import db

def initializeStudent(studentLogin, studentPassword, studentName, studentSurname, studentID):
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
  return db[studentID]['studentName'] + ' ' + db[studentID]['studentSurname']

def getAllStudents():
  studentList = []
  for elem in db.keys():
    if 'Student' in elem:
      studentList.append((elem, studentFullName(elem)))
  return studentList

def changeStudentEmail(currentUser):
  email = input('Enter your email: ')
  while not('@' in email) or (' ' in email):
    print('Please input valid email.')
    email = input('Enter your email: ')
  db[currentUser]['studentEmail'] = email

def changeStudentAge(currentUser):
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
  phoneNum = input('Enter your phone number in format +XX...X: ')
  while phoneNum[0] != '+':
    print('Please input your phone number in the right format.')
    phoneNum = input('Enter your phone number: ')
  flag = False
  while flag == False:
    try:
      int_phoneNum = int(phoneNum[1:])
    except ValueError:
      print('Please input your phone number in the right format.')
      phoneNum = input('Enter your phone number: ')
  db[currentUser]['studentPhoneNum'] = phoneNum

def changeStudentYearOfEdu(currentUser):
  yearOfEdu = input('Enter your year of education (1, 2, 3 or 4): ')
  while not(yearOfEdu in ['1', '2', '3', '4']):
    print('Please enter valid year of education.')
    yearOfEdu = input('Enter your year of education (1, 2, 3 or 4): ')
  db[currentUser]['studentYearOfEdu'] = yearOfEdu

def changeStudentResidPrefer(currentUser):
  residPrefer = input('Enter your residence preference (1 for Residence Hall A and 2 for Residence Hall B): ')
  while not(residPrefer in ['1', '2']):
    print('Please input your residence preference in the correct format.')
    residPrefer = input('Enter your residence preference (1 for Residence Hall A and 2 for Residence Hall B): ')
  db[currentUser]['studentResidPrefer'] = residPrefer

def changeStudentRoomPrefer(currentUser):
  roomPrefer = input('Enter your room preference (1 for a single room and 2 for a double room): ')
  while not(roomPrefer in ['1', '2']):
    print('Please input your room preference in the correct format')
    roomPrefer = input('Enter your room preference (1 for a single room and 2 for a double room): ')
  db[currentUser]['studentRoomPrefer'] = roomPrefer

def changeStudentRoommatePrefer(currentUser):
  if db[currentUser]['studentYearOfEdu'] == 1:
    print('We do not allow first-year students to choose a roommate, so you cannot set a rommate preference.')
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
  specMedCond = input('Enter your room preference: ')
  db[currentUser]['studentSpecMedCond'] = specMedCond

def initializeFaculty(facultyLogin, facultyPassword, facultyName, facultySurname, facultyID):
  db[facultyID] = dict()
  db[facultyID]['facultyLogin'] = facultyLogin
  db[facultyID]['facultyPassword'] = facultyPassword
  db[facultyID]['facultyName'] = facultyName
  db[facultyID]['facultySurname'] = facultySurname

def facultyFullName(facultyID):
  return db[facultyID]['facultyName'] + ' ' + db[facultyID]['facultySurname']

def logout():
  print('You have successfully logged out.')

def newStudentAccount():
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
  password = input('Choose your password: ')
  verification = input('Repeat your password: ')
  while password != verification:
    print('The passwords do not match. Try again.')
    password = input('Choose your password: ')
    verification = input('Repeat your password: ')
  studentName = input('Enter your name: ')
  studentSurname = input('Enter your surname: ')
  studentID = 'Student' + str(db['NumOfStud'] + 1)
  initializeStudent(login, password, studentName, studentSurname, studentID)
  db['NumOfStud'] += 1
  print('Welcome to the system, ' + studentFullName(studentID) + '!')
  print('Your student ID:', studentID)
  return studentID

def studentLogIn():
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
  password = input('Enter your password: ')
  while password != db[currentUser]['studentPassword']:
    print('The password is incorrect. Try again.')
    password = input('Enter your password: ')
  print('Welcome, ' + studentFullName(currentUser) + '!')
  return currentUser

def facultyLogIn():
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
  password = input('Enter your password: ')
  while password != db[currentUser]['facultyPassword']:
    print('The password is incorrect. Try again.')
    password = input('Enter your password: ')
  print('Welcome, ' + facultyFullName(currentUser) + '!')
  return currentUser

def manageOneAspect(currentUser, aspect):
  if aspect == '1':
    changeStudentEmail(currentUser)
  elif aspect == '2':
    changeStudentPhoneNum(currentUser)
  elif aspect == '3':
    changeStudentAge(currentUser)
  elif aspect == '4':
    changeStudentYearOfEdu(currentUser)
  elif aspect == '5':
    changeStudentResidPrefer(currentUser)
  elif aspect == '6':
    changeStudentRoomPrefer(currentUser)
  elif aspect == '7':
    changeStudentRoommatePrefer(currentUser)
  elif aspect == '8':
    changeStudentSpecMedCond(currentUser)
  print('You have successfully updated your application.')
  studentPage(currentUser)

def manageHousingApplication(currentUser):
  print('Enter 1 if you want to change a specific answer on your housing application\nEnter 2 if you want to start the housing application from the beginning')
  ans = input('Your answer: ')
  while not(ans in ['1', '2']):
    print('Please enter a valid input.')
    ans = input('Your answer: ')
  if ans == '1':
    print('Which aspect of the application do you want to change?\n1 - Email\n2 - Phone number\n 3 - Age\n4 - Year of education\n5 - Residence preference\n6 - Room preference\n7 - Roommate preference\n8 - Special medical conditions')
    aspect = input('Your answer: ')
    while not(aspect in ['1', '2', '3', '4', '5', '6', '7', '8']):
      print('Please enter a valid input.')
      aspect = input('Your answer: ')
    manageOneAspect(currentUser, aspect)
  elif ans == '2':
    changeStudentEmail(currentUser)
    changeStudentPhoneNum(currentUser)
    changeStudentAge(currentUser)
    changeStudentYearOfEdu(currentUser)
    changeStudentResidPrefer(currentUser)
    changeStudentRoomPrefer(currentUser)
    print('Do you want to specify a rommate preference?\nEnter 1 if yes\nEnter 2 if no')
    ans = input('Your answer: ')
    while not (ans in ['1', '2']):
      print('Please input valid answer.')
      ans = input('Your answer: ')
    if ans == '1':
      changeStudentRoommatePrefer(currentUser)
    changeStudentSpecMedCond(currentUser)
    print('You have successfully completed your application!')
    studentPage(currentUser)
    
def viewHousingApplication(currentUser):
  print('Housing Application', currentUser)
  print('Full Name:', studentFullName(currentUser))
  print('Email:', db[currentUser]['studentEmail'])
  print('Phone Number:', db[currentUser]['studentPhoneNum'])
  print('Age:', db[currentUser]['studentAge'])
  print('Year of education:', db[currentUser]['studentYearOfEdu'])
  print('Residence preference:', db[currentUser]['studentResidPrefer'])
  print('Room preference:', db[currentUser]['studentRoomPrefer'])
  if 'studentRoommatePrefer' in db[currentUser].keys():
    print('Roommate preference:', db[currentUser]['studentRoommatePrefer'])
  print('Enter 1 if you want to change anything on your application\nEnter 2 if you want to go back to home page')
  ans = input('Your answer: ')
  while not(ans in ['1', '2']):
    print('Please enter a valid input.')
    ans = input('Your answer: ')
  if ans == '1':
    manageHousingApplication(currentUser)
  elif ans == '2':
    studentPage(currentUser)

def studentPage(currentUser):
  print('Enter 1 to start/edit your housing application\nEnter 2 to view your housing application\nEnter 3 to view the room information\nEnter 4 to log out')
  studentPageInput = input('Your answer: ')
  while not(studentPageInput in ['1', '2', '3', '4']):
    print('Please enter a valid input.')
    studentPageInput = input('Your answer: ')
  if studentPageInput == '1':
    manageHousingApplication(currentUser)
  elif studentPageInput == '2':
    viewHousingApplication(currentUser)
  elif studentPageInput == '3':
    print('Available residence halls:\n- Residence Hall A\n- Residence Hall B\nAvailable Rooms:\n- A double room for 2 people\n- A single room for 1 person')
  elif studentPageInput == '4':
    logout()

def accesStudentInfo(currentUser):
  print('Enter 1 if you want to access the list of all the students and their student IDs\nEnter 2 if you want to access information about a specific student')
  ans = input('Your answer: ')
  while not(ans in ['1', '2']):
    print('Please input a valid answer.')
    ans = input('Your answer: ')
  if ans == '1':
    studentList = getAllStudents()
    for elem in studentList:
      print(elem[0], '-', elem[1])
  elif ans == '2':
    studentList = getAllStudents()
    student = input('Enter student\'s ID: ')
    flag = False
    while flag == False:
      for elem in studentList:
        if elem[0] == student:
          flag == True
          print(viewHousingApplication(student))
          break
      if flag == False:
        print('Please input a valid student ID.')
        student = input('Enter student\'s ID: ')
  facultyPage(currentUser)

def addNewFaculty(currentUser):
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
  password = input('Choose a password: ')
  verification = input('Repeat a password: ')
  while password != verification:
    print('The passwords do not match. Try again.')
    password = input('Choose a password: ')
    verification = input('Repeat a password: ')
  facultyName = input('Enter new faculty member\'s name: ')
  facultySurname = input('Enter new faculty member\'s surname: ')
  facultyID = 'Faculty' + str(db['NumOfFac'] + 1)
  initializeFaculty(login, password, facultyName, facultySurname, facultyID)
  db['NumOfFac'] += 1
  print('A new faculty member, ' + facultyFullName(facultyID) + ', was successfully added to the system.')
facultyPage(currentUser)

def facultyPage(currentUser):
  print('Enter 1 to access student information\nEnter 2 to add a new faculty member\nEnter 3 to get a housing plan\nEnter 4 to log out')
  facultyPageInput = input('Your answer: ')
  while not(facultyPageInput in ['1', '2', '3', '4']):
    print('Please enter a valid input.')
    facultyPageInput = input('Your answer: ')
  if facultyPageInput == '1':
    accessStudentInfo()
  elif facultyPageInput == '2':
    addNewFaculty()
  elif facultyPageInput == '3':
    pass
  elif facultyPageInput == '4':
    logout()

def mainscreen():
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

db.clear()
preparations()
mainscreen()