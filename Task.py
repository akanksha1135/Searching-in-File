
email = input("Enter email id to search")
###print(email)
file1 = open('file1.txt','r')
file2 = open('File2.txt','r')
val=""
salary=0
for line in file1:
    arr=line.split()
    if arr[0]==email:
        val=arr[1]
for line in file2:
    arr1=line.split()
    if arr1[0]==val:
        salary=arr1[1]
if val!="" and salary!=0:
    print("For Email id : "+email)
    print("Designation : "+val)
    print("salary : "+salary)
else:
    print(email+" NOT FOUND")
file1.close()
file2.close()

