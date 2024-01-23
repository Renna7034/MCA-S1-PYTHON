class color:
    def col(self):
        list1 =input("enter color seprated my coma:").split(',')
        list2 = ["green", "white", "black"]
        notinlist2 = [a for a in list1 if a not in list2]
        print("Colors from list1 not in list2: ", notinlist2)
obj = color()
obj.col()