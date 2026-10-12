//code by Arjun
//Date:12-10-26

#include <stdio.h>

int main(void) {
    // Initial state
    int Q3 = 0, Q2 = 0, Q1 = 0, Q0 = 0;
    
    //To have track of initial states
    int initial_Q3 = Q3, initial_Q2 = Q2, initial_Q1 = Q1, initial_Q0 = Q0;
    int count = 0;

    printf("Initial State (Q3 Q2 Q1 Q0): %d%d%d%d\n\n", Q3, Q2, Q1, Q0);
    //Main logic

    do {
        printf("State %d: %d%d%d%d\n", count, Q3, Q2, Q1, Q0);
        
        //Next state logic based on flip-flop D inputs:
        int next_Q0 = !Q3;
        int next_Q1 = Q0;
        int next_Q2 = Q1;
        int next_Q3 = Q2;

        //Update states
        Q0 = next_Q0;
        Q1 = next_Q1;
        Q2 = next_Q2;
        Q3 = next_Q3;

        count++;
    } while (!(Q3 == initial_Q3 && Q2 == initial_Q2 && Q1 == initial_Q1 && Q0 == initial_Q0)); //condition

    printf("\nReturned back to initial state %d%d%d%d after %d transitions.\n", Q3, Q2, Q1, Q0, count);
    printf("Initial State: %d%d%d%d\n", initial_Q3, initial_Q2, initial_Q1, initial_Q0);
    printf("Number of distinct states): %d\n", count);

    return 0;
}

