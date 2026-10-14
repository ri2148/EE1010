//code by Arjun
//14-10-26

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "libs/listgen.h"
#include "libs/listfun.h"

//Function to calculate higher powers
double power_rec(double x, int exp) {
if (exp == 0) return 1.0;
double half = power_rec(x, exp / 2);
if (exp % 2 == 0) return half * half;
return x * half * half;
}

int main(void) {
double val, x, result = 0.0;
int degree = 0;

printf("Enter coefficients (a0, a1, a2, ...) separated by space (enter 'q' to stop): ");

sadish *head = NULL, *tail = NULL;

while (scanf("%lf", &val) == 1) {
sadish *new_node = (sadish *)malloc(sizeof(sadish));
new_node->data = val;
new_node->next = NULL;

if (head == NULL) {
head = new_node;
} else {
tail->next = new_node;
}
tail = new_node;
}

while (getchar() != '\n');

printf("Enter x: ");
scanf("%lf", &x);

//Evaluate Polynomial
sadish *curr = head;
while (curr != NULL) {
result += curr->data * power_rec(x, degree);
degree++;
curr = curr->next;
}

printf("P(%.2f) = %.4f\n", x, result);
//Free memory
while (head != NULL) {
sadish *temp = head;
head = head->next;
free(temp);
}

return 0;
}

