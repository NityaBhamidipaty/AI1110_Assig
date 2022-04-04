#ICSE 2017 2(c)
#Name: Nitya Seshagiri Bhamidipaty
#Roll no.: cs21btech11041

#computes the debt due at the end of 2nd year 
def computedue(p,r1,r2,q1):
    return (p*(1+r1/100)*(1+r2/100) - q1*(1+r2/100))
    
p = 50000 #The principle
r1 = 12 #rates of interest r1
r2 = 15 #rates of interest r2
q1 = 33000 #amount paid at the end of 1st year
print("Amount due at the end of second year = ",computedue(p,r1,r2,q1));  
