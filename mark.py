dict={}
for i in range(0,5):
     reg=input("Enter the register number")
     mark=[]
     for j in range(5):
          m=int(input("Enter the mark"))
          mark.append(m)
          dict[reg]=mark
          print(dict)
                      
