
while(True):
    print("1.General Calculation of attandance")
    print("2.Prediction to a number of days present")
    print("3.Prediction to a number of days absent")
    print("4.Exit")
    choice=int(input("Select an option: "))

    if(choice==1):
        np=int(input("Enter number of periods present: "))
        tp=int(input("Enter number of total periods: "))
        att=float((np/tp)*100)
        print("-----------------------------Your attandance will be :",att)
        continue
    elif(choice==2):
        np=int(input("Enter number of periods present: "))
        tp=int(input("Enter number of total periods: "))
        x=int(input("Enter number of days to be predicted: "))
        a = np + (x*7)
        b = tp + (x*7)
        att=float((a/b)*100)
        print("-----------------------------Your attandance will be :",att)
        continue
    elif(choice==3):
        np=int(input("Enter number of periods present: "))
        tp=int(input("Enter number of total periods: "))
        x=int(input("Enter number of days to be predicted: "))
        a=np
        b= tp + (x*7)
        att=float((a/b)*100)
        print("-----------------------------Your attandance will be :",att)
        continue
    elif(choice==4):
        print("-----------------------------Exiting")
        break
    else:
        print("Choice Unavailable!!")
        continue
        
