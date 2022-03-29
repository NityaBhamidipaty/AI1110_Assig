#include <stdio.h>

int main(){
    double p; /*The principle*/
    double r; /*rate of interest*/
    /*for first year*/
    p = 50000.0;
    r = 12.0;
    double due;
    /*at the end of first year*/
    due  = p*(1.0 + r/100.0 );

    p = due - 33000.0;   /*33000 paid*/
    r = 15.0;
    /*at the end of second year*/
    due = p*(1.0 + r/100.0);
    printf("Amount due at the end of second year %f\n",due);
    return 0;
}