import calendar as cal
print("-----calender program in python----\n");
print("Enter'x' for exit")
y = input("enter year:");
if y=='x':
    exit()
else:
    m=input("enter month:");
    yy=int(y);
    mm=int(m);
    print("\n",cal.month(yy,mm))
    