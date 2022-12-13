from replit import db
import os
#os.system("pip install pwinput")
import pwinput

def initializeFaculty(facultyLogin, facultyPassword, facultyName, facultySurname, facultyID):
  """This is the init function, which starts the class. It also contains the main data that the objects in the class will require, such as faculty name and surname."""
  db[facultyID] = dict()
  db[facultyID]['facultyLogin'] = facultyLogin
  db[facultyID]['facultyPassword'] = facultyPassword
  db[facultyID]['facultyName'] = facultyName
  db[facultyID]['facultySurname'] = facultySurname

def facultyFullName(facultyID):
  """This function combines the first name and the surname to get the full name."""
  return db[facultyID]['facultyName'] + ' ' + db[facultyID]['facultySurname']

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