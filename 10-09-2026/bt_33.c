//code by Arjun
//date: 10-09-2026
#include<stdio.h>
#include<math.h>
#define e 2.718

//Main program begins
int main(void){
double x=1; // Initial guess
double y=pow(e, x)-2; //Initial y

//Logic to find root
while(y!=0){
x=x-(pow(e, x)-2)/(pow(e, x));
y=pow(e, x)-2;
}
//Printing the root
printf("The root is %.2lf", x);
 }
