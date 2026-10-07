#include <stdio.h>

int main() {
    printf(" b3 | b2 | b1 | b0 |  F \n");
    printf("-----------------------\n");

    for (int i = 0; i < 16; i++) {
        // Extract individual bits from integer i
        int b3 = (i >> 3) && 1;
        int b2 = (i >> 2) && 1;
        int b1 = (i >> 1) && 1;
        int b0 = (i >> 0) && 1;

        // Evaluate the Boolean function F = ∑(0, 2, 4, 8, 10, 11, 12)
        int F = (i == 0  || i == 2  || i == 4  || 
                 i == 8  || i == 10 || i == 11 || i == 12) ? 1 : 0;

        printf("  %d |  %d |  %d |  %d |  %d\n", b3, b2, b1, b0, F);
    }

    return 0;
}

