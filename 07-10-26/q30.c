//Code by Arjun, 07-10-26

#include <stdio.h>

int main() {
    char alphabet[3] = {'a', 'b', 'c'};
    int count = 0;

    // Iterate through all possible ternary strings of length 5
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            for (int k = 0; k < 3; k++) {
                for (int l = 0; l < 3; l++) {
                    for (int m = 0; m < 3; m++) {
                        
                        // Check if at least one consecutive pair is identical
                        if (i == j || j == k || k == l || l == m) {
                            count++;
                        }

                    }
                }
            }
        }
    }

    printf("The number of such strings of length 5 is: %d\n", count);

    return 0;
}

