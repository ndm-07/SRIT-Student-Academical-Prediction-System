while(True):
    print("1.To Calculate Internal Marks of MID Exams")
    print("2.To Calculate Total Internal Marks")
    print("3.To Predict the Grade result of SEM Exams")
    print("4.Exit")
    choice=int(input("Select an option: "))

    if(choice==1):
        m1=float(input("Enter Mid 1 marks: "))
        m2=float(input("Enter Mid 2 marks: "))
        if(m1>30 or m2>30):
            print("--------Mid 30 Marks ke ra. 30 lopala marks type chey")
            continue
        elif(m1>m2 or m1==m2):
                r1=(m1*0.8)+(m2*0.2)
        elif(m1<m2 or m1==m2):
                r1=(m2*0.8)+(m1*0.2)
        print("--------The Internal marks of MID Exams: ",round(r1))          
    elif(choice==2):
        m1=float(input("Enter Mid 1 marks: "))
        m2=float(input("Enter Mid 2 marks: "))
        m3=float(input("Enter CAA1 marks: "))
        m4=float(input("Enter CAA2 marks: "))
        if(m1>30 or m2>30):
           print("--------Mid 30 Marks ke ra. 30 lopala marks type chey")
           continue
        else:
            if(m1>m2 or m1==m2):
                  r1=(m1*0.8)+(m2*0.2)
            elif(m1<m2 or m1==m2):
                  r1=(m2*0.8)+(m1*0.2)
            print("--------The Internal marks of MID Exams: ",round(r1))
            if(m3>10 or m4>10):
                print("--------CAA 10 Marks ke ra jaffa.")
                continue
            else:
                r2=(m3+m4)/2
                r3=r1+r2
            print("--------The Internal marks along with CAA marks: ",round(r3))
            continue

    elif(choice==3):
        x=int(input("Enter your Internal Marks: "))
        y=int(input("Enter your Expected Marks in SEM Exams: "))
        if(x>40 or y>60):
            print("--------Kallu Tirugutannaya? Yenni marks type chesnavo sarigga chusko.")
            continue
        elif(y<21):
            print("--------Bro, no doubt. Fail ey. Supply ki ready ayipo.")
            continue
        else:
            p=round(x)+round(y)
            if(p>=90):
                print("--------You Might get S as your Grade")
            elif(p>=80 and p<=89):
                print("--------You Might get A as your Grade")
            elif(p>=70 and p<=79):
                print("--------You Might get B as your Grade")
            elif(p>=60 and p<=69):
                print("--------You Might get C as your Grade")
            elif(p>=50 and p<=59):
                print("--------You Might get D as your Grade")
            elif(p>=40 and p<=49):
                print("--------You Might get E as your Grade")
            elif(p<40):
                print("--------Sorry bro.Supply ne le inka. F Grade neeku")
                continue
    elif(choice==4):
        print("--------Exiting")
        break
    else:
        print("--------Nee yenkamma Options undi 4 ey. Chusi select chey")
        continue
    

