L1 = ["John", 102, "USA"]
L2 = [1, 2, 3, 4, 5, 6]
L3 = [1, "Ryan"]

emp = ["John", 102, "USA"]
Dep1 = ["CS", 10]
Dep2 = ["IT", 11]
HOD_CS = [10, "Mr. Holding"]
HOD_IT = [11, "Mr. Bewon"]
print("printing employee data...")
print("Name : %s, ID: %d, Country: %s" % (emp[0], emp[1], emp[2]))
print("printing departments...")
print("Department 1:\nName: %s, ID: %d\nDepartment 2:\nName: %s, ID: %s" % (Dep1[0], Dep2[1], Dep2[0], Dep2[1]))
print("HOD Details ....")
print("CS HOD Name: %s, Id: %d" % (HOD_CS[1], HOD_CS[0]))
print("IT HOD Name: %s, Id: %d" % (HOD_IT[1], HOD_IT[0]))
print(type(emp), type(Dep1), type(Dep2), type(HOD_CS), type(HOD_IT))


# Updating list values

List = [1, 2, 3, 4, 5, 6]
print(List)
List[2] = 10
print(List)
List[1:3] = [89, 78]
print(List)


