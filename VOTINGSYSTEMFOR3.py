#  step-1 first we declare three team and provide the name of candidates
P1 =input("enter the name of first member :\n")
P2 =input("enter the name of second member:\n")
P3 =input("enter the name of third  member:\n")
# step-2 declare their no. of votes initially zero
V1 =0
V2 =0
V3 =0
# step-3 declare the id for registered or valid  voters
ID= [1,2,3,4]
# step-4 define total number of voter 
TOTALVOTES =len(ID)
# step-5 start a while loop for voting it execute till all valid voter give their vote
while True:

    if ID ==[]:
        print("voting session is over")
        if V1>V2 and V1>V3:
            percentage1 =( V1/TOTALVOTES)*100
            print(P1 , "has won with", percentage1, " % votes" )
            break
        elif V2>V1 and V2>V3: 
            percentage2 =( V2/TOTALVOTES)*100
            print(P2 , "has won with", percentage2, " % votes" )
            break 
        elif V3>V1 and V3>V2:
            percentage3 =(V3/TOTALVOTES)*100
            print(P3 , "has won with", percentage3, " %votes")
            break
        elif V1 ==V2 and V2>V3:
            print("Both", P1, "and", P2, "are winner")
            break
        elif V3 ==V2 and V2>V1:
            print("Both", P3, "and", P2, "are winner")
            break
        elif V3 ==V2 and V1>V2:
            print("Both", P3, "and" ,P2, "are winner")
            break
        elif V1==V2 and V2==V3:
            print("all are winners")
            break
                  
              
    else:
        VOTER =int(input("enter your voter id:"))
        if VOTER in ID:
         print("you are a voter")
         ID.remove(VOTER)
         vote =int(input("enter your vote:\n1)P1\n2)P2\n3)P3\n "))
         if vote ==1:
            V1+=1
            print("thank you for your vote") 
            
         elif vote == 2:
            V2+=1
            print("thank you for your vote") 
            
         elif vote == 3:
            V3+=1
            print("thank you for your vote") 
            
        else:
         print("you are not a voter or you have already voted")
            
        

        
    
