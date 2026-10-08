#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "listgen.h"
#include "listfun.h"

int find(double query, sadish *list)
{
    while (list != NULL)
    {
        if (list->data == query)
            return 1;
        list = list->next;
    }
    return 0;
}

int countNodes(sadish *head)
{
    int count = 0;
    while (head != NULL)
    {
        count++;
        head = head->next;
    }
    return count;
}

int main()
{
    FILE *fp1 = fopen("vec1.dat", "r");
    FILE *fp2 = fopen("vec2.dat", "r");

    if (!fp1 || !fp2) return 1;

    // Load linked lists L1 and L2
    sadish *L1 = loadVec(fp1, 9);
    sadish *L2 = loadVec(fp2, 7);

    fclose(fp1);
    fclose(fp2);

    // Save starting head node of L1 so we don't lose the list
    sadish *head = L1;

    // Traverse and modify directly using L1
    while (L1->next != NULL)
    {
        if (find(L1->next->data, L2))
        {
            L1->next = L1->next->next; // Delete matching node
        }
        else
        {
            L1 = L1->next;             // Move L1 forward
        }
    }

    // Print resulting list starting
    printf("Modified L1: ");
    printVec(head);

    printf("Number of nodes remaining in L1 = %d\n", countNodes(head));

    return 0;
}

