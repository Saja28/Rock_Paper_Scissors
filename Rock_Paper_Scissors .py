import random
#a=["Rock","Paper" , "Scissors" ]
#random.choice(a))
b=["r","p" , "s" ]

def rock_paper_scissors() :
   
    if m == 'r' and n== 'p' :
        result= 0
        return result
      #score_n += 1
      #score_m += 0
      # print=(" Paper is winner.  ")
            
    elif m == 'p'and n== 'r' :
        result= 1
        return result
        #score_m += 1
        #score_n += 0
       # print( " Paper is winner.  ")
    elif m == 'r' and n== 's' :
        result= 1
        return result
       
        #print( " Rock is winner.  ")   
    elif m == 's'and n== 'r' :
        result= 0
        return result
      
       # print( " Rock is winner.  ")
    elif m == 'p' and n== 's' :
        result= 0
        return result  
     
       # print( " Scissors is winner.  ")
    elif m == 's' and n== 'p' :
        result= 1
        return result
   
        #print( f" Scissors is winner. ")

    elif m == 's' and n== 's' :
        result= 0
        return result

        #print( " try agin!  ")   
    elif m == 'p' and n== 'p' :
        result= 0
        return result
    
       # print( " try agin!  ")
    elif m == 'r'and n== 'r' :
        result= 0
        return result 
       #print( " try agin!  ")
result=0
count = 0
while count <= 3 :
    count +=1
    n = random.choice(b)
    m = input(" you select one item:\n")
    k=  rock_paper_scissors()
    result= result + k
    print(f"score_m = {k }")
if result <= 2 :
    print("you are winner")
else:
    print("pc is wninner")






