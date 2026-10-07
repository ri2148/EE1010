// Code by Arjun
// Date: 05/10/2026
#include <stdio.h>

// Function converting number to specific bit using division and modulo
int get_bit(int num, int position) {
    if (position == 2) num = num / 4; // Shift left bit down (2^2)
    if (position == 1) num = num / 2; // Shift middle bit down (2^1)
    
    return num % 2; // Returns remainder: 0 or 1
}

int main(void)
{
    int i, X;
    printf("--------\n");

    for (i = 0; i < 8; i++)
    {
        // Majority function computed directly: AB + AC + BC
        X = (get_bit(i, 2) & get_bit(i, 1)) | 
            (get_bit(i, 2) & get_bit(i, 0)) | 
            (get_bit(i, 1) & get_bit(i, 0));

        // Print A, B, C directly without separate variables
        printf("%d %d %d | %d\n", get_bit(i, 2), get_bit(i, 1), get_bit(i, 0), X);
    }

    return 0;
}

