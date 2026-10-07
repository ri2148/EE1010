//code by arjun, 07-10-26

#include <stdio.h>

int main(void) {
    int a = 12; // Binary: 1100
    int b = 10; // Binary: 1010
    printf("The numbers taken are a=%d and b=%d\n", a, b);
    // 1. Difference in output values
    printf("a & b  = %d\n", a & b);   // Output: 8 (bitwise: 1100 & 1010 = 1000)
    printf("a && b = %d\n\n", a && b); // Output: 1 (logical: true AND true)

