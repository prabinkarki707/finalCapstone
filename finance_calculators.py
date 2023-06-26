#lets gooooooo
import math
#lets use print statement to print some conditions
print("investment - to calculate the amount you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

#using select_one variable to select one option
select_one = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

#making the string of select_one variable lowercase 
verification = select_one.lower()

#condition 1st using if statement
if verification == "investment":
   P = float(input("Enter the deposit amount: "))
   r = float(input("Enter the interest rate: "))
   t = float(input("Enter the number of years to invest: "))
   interest=input("Do you want 'simple' or 'compound' interest: ")
   I= interest.lower()
   r= float(r/100)
   
   #well let's say this as condition 1.1 that is performed if user goes with condition 1st
   if I == 'simple':
      A = float(P*(1+(r*t)))
      print("Your simple interest will be " + str(A))

   #and similarly condition 1.2
   elif I == 'compound':
      A = P * (1+r) ** t   
      print("Your compound interest will be " + str(A))  

# this is gonna be condition 2nd if user inputs "bond"      
elif verification == "bond":
   P= float(input("Enter the present value of house: "))
   i = float(input("Enter the interest rate: "))  
   n = float(input("Enter the bond replayments plan in months: "))
   i= float((i/100)/12)
   x = float((1 +i)**(-n)) 
   y = float(1-x)
   repayment = float((i * P)/y)    
   print("You'll have to pay " + str(repayment) +"each month")