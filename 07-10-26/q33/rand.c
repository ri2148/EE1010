#include<stdio.h>

void foo(int p*, intx){
p*=x;
}
int main(void){
int *z;
int a=20, b=25;
z=&a;
foo(z,b);
printf("%d", a);

}
