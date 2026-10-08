#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "listgen.h"
#include "listfun.h"

// Helper function to print a vector formatted to 2 decimal places
void printVector(sadish *a)
{
    while (a != NULL)
    {
        printf("%.2lf ", a->data);
        a = a->next;
    }
    printf("\n");
}

int main()
{
    // Define vector lengths
    int n1 = 9; // Number of elements in vec1.dat
    int n2 = 7; // Number of elements in vec2.dat

    // Open file pointers
    FILE *fp1 = fopen("vec1.dat", "r");
    FILE *fp2 = fopen("vec2.dat", "r");

    if (fp1 == NULL || fp2 == NULL)
    {
        printf("Error: Could not open vector data files.\n");
        return 1;
    }

    // Load vectors from files using loadVec from listgen.h
    sadish *v1 = loadVec(fp1, n1);
    sadish *v2 = loadVec(fp2, n2);

    // Close files
    fclose(fp1);
    fclose(fp2);

    // Print vectors
    printf("Vector 1: ");
    printVector(v1);

    printf("Vector 2: ");
    printVector(v2);

    return 0;
}

