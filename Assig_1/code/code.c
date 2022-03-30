#include <stdio.h>

double computedue(double p,double r1,double r2,double q1){
    return (p*(1.0+r1/100.0)*(1.0+r2/100.0) - q1*(1.0+r2/100));
}

int main(){
    
    double p = 50000.0; /*The principle*/
    double r1 = 12.0,r2 = 15.0; /*rates of interest*/
    double q1 = 33000.0; /*amount paid at the end of 1st year*/
    printf("Amount due at the end of second year =  %g \n",computedue(p,r1,r2,q1));  
    return 0;
}
