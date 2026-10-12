//code by Arjun
//12-10-26

#include <stdio.h>

#define NUM_STATES 8

// States: A=0, B=1, C=2, D=3, E=4, F=5, G=6, H=7
const char state_names[NUM_STATES] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'};

// FSM Transition Table from problem image
int next_state[NUM_STATES][2] = {
    {5, 1}, // A -> F, B
    {3, 2}, // B -> D, C
    {5, 4}, // C -> F, E
    {6, 0}, // D -> G, A
    {3, 2}, // E -> D, C
    {5, 1}, // F -> F, B
    {6, 7}, // G -> G, H
    {6, 0}  // H -> G, A
};

int output_f[NUM_STATES][2] = {
    {0, 0}, // A
    {0, 0}, // B
    {0, 0}, // C
    {1, 0}, // D
    {0, 0}, // E
    {1, 1}, // F
    {0, 1}, // G
    {1, 0}  // H
};

int main() {
    int group[NUM_STATES];
    int new_group[NUM_STATES];
    
    // Step 1: Initial partitioning based on output f (X=0, X=1)
    for (int i = 0; i < NUM_STATES; i++) {
        group[i] = (output_f[i][0] << 1) | output_f[i][1];
    }

    int changed = 1;
    while (changed) {
        changed = 0;
        int group_counter = 0;
        
        for (int i = 0; i < NUM_STATES; i++) {
            new_group[i] = -1;
        }

        for (int i = 0; i < NUM_STATES; i++) {
            if (new_group[i] != -1) continue;

            new_group[i] = group_counter;
            for (int j = i + 1; j < NUM_STATES; j++) {
                if (group[i] == group[j] &&
                    group[next_state[i][0]] == group[next_state[j][0]] &&
                    group[next_state[i][1]] == group[next_state[j][1]]) {
                    new_group[j] = group_counter;
                }
            }
            group_counter++;
        }

        for (int i = 0; i < NUM_STATES; i++) {
            if (group[i] != new_group[i]) {
                changed = 1;
                group[i] = new_group[i];
            }
        }
    }

    // Count distinct states
    int distinct_states = 0;
    int visited[NUM_STATES] = {0};

    printf("Minimization Results:\n");
    for (int i = 0; i < NUM_STATES; i++) {
        if (!visited[group[i]]) {
            visited[group[i]] = 1;
            distinct_states++;
            printf("Group %d: { ", distinct_states);
            for (int j = 0; j < NUM_STATES; j++) {
                if (group[j] == group[i]) {
                    printf("%c ", state_names[j]);
                }
            }
            printf("}\n");
        }
    }

    printf("--------------------------------------------------\n");
    printf("Required Answer (Minimum number of states): %d\n", distinct_states);

    return 0;
}

