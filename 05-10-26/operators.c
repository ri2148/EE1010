//code by arjun, 07-10-26

#include <stdio.h>

int main(void) {
    int a = 12; // Binary: 1100
    int b = 10; // Binary: 1010
    printf("The numbers taken are a=%d and b=%d\n", a, b);
    // 1. Difference in output values
    printf("a & b  = %d\n", a & b);   // Output: 8 (bitwise: 1100 & 1010 = 1000)
    printf("a && b = %d\n\n", a && b); // Output: 1 (logical: true AND true)

    // 2. Short-circuit demonstration
    int x = 0;
printf("Demonstration with x=0 and 0\n");
    // && skips the right side if left is 0
    if (0 && ++x) {}
    printf("x after &&: %d\n", x); // x is still 0

    // & always evaluates both sides
    if (0 & ++x) {}
    printf("x after & : %d\n", x); // x becomes 1

    return 0;
}

