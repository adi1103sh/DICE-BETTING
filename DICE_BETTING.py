import random
print("Welcome 2 world of DICE")
print("RULES ARE:")
print("1. IF U BETTED ON CORRECT NO. THEN YOUR INVESTMENT IS DOUBLED")
print("2. IF U BETTED ON WRONG NO. THEN YOUR INVESTMENT IS HALVED")
print("3. AT EACH TURN RESULT IS ADDED")
print("4. IF DICE SHOWS 6 THEN 100 IS ADDED TO YOUR RESULT NO MATTER ON WHICH NUMBER YOU BETTED")
rate_list={2:100,3:200,4:250,5:300}
print("THE RATE LIST IS AS FOLLOWS:")
print(rate_list)
n=int(input("ENTER NO. OF TRIALS:"))
invest=int(input("ENTER RUPEES AS PER NO. OF TRIALS:"))
value=invest
while(n!=0):
    # STARTING BET
    r=int(input("ROLL THE DICE!!! by typing digit on which u bet :"))
    if(r==1 or r==2 or r==3 or r==4 or r==5 or r==6):
        print("YOU BETTED ON:", r)
        dice=random.randint(1,6)
        print("DICE SHOWS:",dice)
        # TRANSACTION BASED ON RESULT OF BETTING
        if(dice==6):
            value=value+100
            print("result:",value)
        elif (dice == r):
            value = value + (value * 2)
            print("result:", value)
        else:
            value = value + (value / 2)
            print("result:", value)
    else:
        print("****NO CHEATING****")
    n=n-1
# RESULT
if(value>invest):
    print("KUDOS!!! YOU NAILED IT")
else:
    print("BETTER LUCK NEXT TIME")
print("YOUR FINAL CREDENTIALS ARE:",value)

