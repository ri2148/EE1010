#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include "listgen.h"
#include "listfun.h"

// Include your header file containing the 'avyuh' struct, Listnorm, Listscale, and Listunit
#include "listfun.h" 

void print_vector(avyuh *v) {
    // Modify this loop/print logic according to your 'avyuh' / vector struct definition
    printf("[ ");
    // Example assuming v->vector is a linked list or array:
    // ... print vector elements here ...
    printf(" ]\n");
}

int main() {
    // 1. Initialize/Create a test vector 'a'
    // Replace this initialization with your actual helper function to create/populate a vector
    avyuh *a = NULL; 
    
    /* 
       Example setup: create a 3D vector [3, 4, 0]
       Norm should be sqrt(3^2 + 4^2) = 5
       Unit vector should be [0.6, 0.8, 0.0]
    */

    printf("Original Vector Norm: %f\n", Listnorm(a));

    // 2. Call your unit vector function
    avyuh *u = Listunit(a);

    // 3. Display the resulting unit vector
    printf("Unit Vector: ");
    print_vector(u);

    // 4. Verify that the norm of the unit vector equals 1.0
    double u_norm = Listnorm(u);
    printf("Norm of Unit Vector: %f\n", u_norm);

    if (fabs(u_norm - 1.0) < 1e-6) {
        printf("TEST PASSED: Norm is 1.0!\n");
    } else {
        printf("TEST FAILED: Norm is not 1.0.\n");
    }

    // Clean up allocated memory if necessary
    // free(a);
    // free(u);

    return 0;
}

