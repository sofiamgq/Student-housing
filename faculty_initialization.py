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

def logout():
  """This function logs out the user of their account."""
  print('You have successfully logged out.')