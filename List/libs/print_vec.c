#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "listgen.h"
#include "listfun.h"

int main()
{
    int n1 = 9, n2 = 7;

    FILE *fp1 = fopen("vec1.dat", "r");
    FILE *fp2 = fopen("vec2.dat", "r");

    if (!fp1 || !fp2) return 1;

    // 1. Read directly into an avyuh matrix structure
    avyuh *matrix = (avyuh *)malloc(sizeof(avyuh));
    matrix->vector = loadVec(fp1, n1); // Row 1[span_2](start_span)[span_2](end_span)

    matrix->next = (avyuh *)malloc(sizeof(avyuh));
    matrix->next->vector = loadVec(fp2, n2); // Row 2[span_3](start_span)[span_3](end_span)
    matrix->next->next = NULL;

    fclose(fp1);
    fclose(fp2);

    // 2. Pad row 2 with zeros manually in a simple loop
    sadish *curr = matrix->next->vector;
    while (curr->next != NULL) curr = curr->next; // Find tail

    for (int i = n2; i < n1; i++)
    {
        curr->next = (sadish *)malloc(sizeof(sadish));
        curr = curr->next;
        curr->data = 0.0;
        curr->next = NULL;
    }

    // 3. Use the built-in printList function from listgen.h
    printf("Combined Avyuh:\n");
    printList(matrix);

    return 0;
}

