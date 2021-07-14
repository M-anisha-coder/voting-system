#  step-1 first we declare two team and provide the name of candidates
teamA =input("Enter the name of first member :")
teamB =input("Enter the name of second member:")
# step-2 declare their no. of votes initially zero
voteA=0
voteB=0
# step-3 declare the id for registered or valid  voters
ids = [1,2,3,4,5,6,7,8,9,10]
# step-4 define total number of voter 
numofvotes =len(ids)
# step-5 start a while loop for voting it execute till all valid voter give their vote
while True:
 
    if ids ==[]:
         print("voting session is over")
         if voteA>voteB:
             per1 =( voteA/numofvotes)*100
             print(teamA,"has won with",per1 ,"% votes")
             break
         elif voteA<voteB:
             per2 =( voteB/numofvotes)*100
             print(teamB,"has won with",per2 ,"% votes")
             break
         else:
             print(" all member are winners")
             break
    else:
        voter =int(input("enter your voter id:"))
        if voter  in ids:
          print("you are a voter")
          ids.remove(voter)
          vote =int(input("enter your vote:\n1)teamA\n2)teamB :\n "))
          if vote==1:
             voteA+=1
             print("thank you for your vote") 

          elif vote==2:
            voteB+=1
            print("thank you for your vote")  
        else:
         print("you are not a voter or you have already voted")
            
        
#hello guys this a voting system where two candidates are fighting and 10 peoples are voting for a great leader
        
    
