#EX4
array = [['Number ID','Name','Count','Status'],[]]
print("Find length of array",len(array))
print("Insert value 1,Rubber,0,Out of stock")
print("Insert value 2,Ruler,5,In stock")
print("Insert value 3,Pencil,1,In stock")
array.insert(1,[1,"Rubber",0,"Out of stock"])
array.insert(2,[2,"Ruler",5,"In stock"])
array.insert(3,[3,"Pencil",1,"In stock"])
print(array)