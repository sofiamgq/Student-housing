from replit import db
import os
#os.system("pip install pwinput")
import pwinput
from student_initialization import *
from faculty_initialization import *
from housing_application import *

def generateHousingAssignments():
  dormAAvailable = 50
  dormAList = []
  dormBAvailable = 50
  dormBList = []
  Overflow = []
  # Assigns students to dorm A if they indicated this as their first choice. Otherwise, assigns to dorm B until dorm B is full. Then, assigns to overflow after both dorms are full.
  for elem in db.keys():
    if 'Student' in elem:
      if dormAAvailable > 0:
        if db[elem]['studentResidPrefer'] == 'dorm A':
          dormAAvailable -= 1
          dormAList.append(elem)
        elif dormBAvailable > 0:
          dormBAvailable -= 1
          dormBList.append(elem)
      else:
        print('All dorms full')
        Overflow.append(elem)
  
  print('Dorm A Roommate Assignments:')
  RoommateAssignmentsDormA = returnRoommateList(dormAList)
  if len(RoommateAssignmentsDormA) == 0:
    print('No Students requested to be assigned to dorm A. Dorm A is empty!')
  for tuple in RoommateAssignmentsDormA:
    print(studentFullName(tuple[0]) + ' : ' + studentFullName(tuple[1]))
  print()
  print('Dorm B Roommate Assignments:')
  RoommateAssignmentsDormB = returnRoommateList(dormBList)
  for tuple in RoommateAssignmentsDormB:
    print(studentFullName(tuple[0]) + ' : ' + studentFullName(tuple[1]))
    print()


def returnRoommateList(listOfStudents):
  RoommmateAssignmentsList = []
  # Generate roommate assignments within the dorm by creating sets of tupples based on roommate specifications
  # pair roommates who have requested each other by name. Ignores if students have 'None' in this category
  for student1 in listOfStudents:
    for student2 in listOfStudents:
      if student2 == student1:
        continue
      else:
        if db[student1]['studentRoommatePrefer'] == db[student2]['studentRoommatePrefer'] and db[student1]['studentRoommatePrefer'] != None:
          listOfStudents.remove(student1)
          listOfStudents.remove(student2)
          roommateTuple = (student1, student2)
          RoommmateAssignmentsList.append(roommateTuple)
    break
  # pair  students of the same grade level. Ignores if students have 'None' in this category
  for student1 in listOfStudents:
    for student2 in listOfStudents:
      if student2 == student1:
        continue
      else:
        if db[student1]['studentYearOfEdu'] == db[student2]['studentYearOfEdu'] and db[student1]['studentRoommatePrefer'] != None:
          listOfStudents.remove(student1)
          listOfStudents.remove(student2)
          roommateTuple = (student1, student2)
          RoommmateAssignmentsList.append(roommateTuple)
    break
  while len(listOfStudents) >= 2:
    for student1 in listOfStudents:
      for student2 in listOfStudents:
        if student2 == student1:
          continue
        else:
          try:
            listOfStudents.remove(student1)
            listOfStudents.remove(student2)
            roommateTuple = (student1, student2)
            RoommmateAssignmentsList.append(roommateTuple)
          except:
            pass
      break
  print('Unassigned students: ' + str(listOfStudents))
  return RoommmateAssignmentsList