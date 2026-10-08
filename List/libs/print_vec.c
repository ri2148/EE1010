#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "listgen.h"
#include "listfun.h"

int main()
{
    // Load both vectors directly into an avyuh matrix structure
    avyuh *matrix = (avyuh *)malloc(sizeof(avyuh));

    FILE *fp1 = fopen("vec1.dat", "r");
    FILE *fp2 = fopen("vec2.dat", "r");

    if (!fp1 || !fp2) return 1;

    matrix->vector = loadVec(fp1, 9);         // Row 1 (9 elements)
    matrix->next = (avyuh *)malloc(sizeof(avyuh));
    matrix->next->vector = loadVec(fp2, 7);   // Row 2 (7 elements)
    matrix->next->next = NULL;

    fclose(fp1);
    fclose(fp2);

    // Print matrix directly using library function
    printf("Combined Avyuh Matrix:\n");
    printList(matrix);

    return 0;
}

