from replit import db
import os
#os.system("pip install pwinput")
import pwinput

def manageOneAspect(currentUser, aspect):
  """This function allows the users to update their housing application and redirects them to the part of the application that they want to update."""
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
  """This is the function that asks students what part of their application they want to change, and then it redirects them to that section."""
  print('Enter 1 if you want to change a specific answer on your housing application\nEnter 2 if you want to start the housing application from the beginning')
  ans = input('Your answer: ')
  while not(ans in ['1', '2']):
    print('Please enter a valid input.')
    ans = input('Your answer: ')
  if ans == '1':
    print('Which aspect of the application do you want to change?\n1 - Email\n2 - Phone number\n3 - Age\n4 - Year of education\n5 - Residence preference\n6 - Room preference\n7 - Roommate preference\n8 - Special medical conditions')
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
    
def viewHousingApplication(studentID, currentUser):
  """This function allows students to visualize the information they entered for the housing application."""
  print('Housing Application', studentID)
  print('Full Name:', studentFullName(studentID))
  print('Email:', db[studentID]['studentEmail'])
  print('Phone Number:', db[studentID]['studentPhoneNum'])
  print('Age:', db[studentID]['studentAge'])
  print('Year of education:', db[studentID]['studentYearOfEdu'])
  if db[studentID]['studentResidPrefer'] == '1':
    print('Residence preference:', 'Residence Hall A')
  elif db[studentID]['studentResidPrefer'] == '2':
    print('Residence preference:', 'Residence Hall B')
  elif db[studentID]['studentResidPrefer'] == None:
    print('Residence preference:', None)
  if db[studentID]['studentRoomPrefer'] == '1':
    print('Room preference:', 'single room')
  elif db[studentID]['studentRoomPrefer'] == '2':
    print('Room preference:', 'double room')
  elif db[studentID]['studentRoomPrefer'] == None:
    print('Room preference:', None)
  print('Roommate preference:', db[studentID]['studentRoommatePrefer'])
  if 'Student' in currentUser:
    print('Enter 1 if you want to change anything on your application\nEnter 2 if you want to go back to home page')
    ans = input('Your answer: ')
    while not(ans in ['1', '2']):
      print('Please enter a valid input.')
      ans = input('Your answer: ')
    if ans == '1':
      manageHousingApplication(currentUser)
    elif ans == '2':
      studentPage(currentUser)
  else:
    facultyPage(currentUser)

def accessStudentInfo(currentUser):
  """This function allows faculty members to see a list of all the students. It also allows them to view specific information about a student if they enter their student ID."""
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
          print(viewHousingApplication(student, currentUser))
          break
      if flag == False:
        print('Please input a valid student ID.')
        student = input('Enter student\'s ID: ')
  facultyPage(currentUser)
  
def returnStudentFullName(elem):
  return db[elem]['studentName'] + ' ' + db[elem]['studentSurname']