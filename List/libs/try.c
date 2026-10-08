//Code by Mudit
//Date: 08/10/2026
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "listgen.h"
#include "listfun.h"

void printVector(sadish *a)
{
    while (a != NULL)
    {
        printf("%.2lf ", a->data);
        a = a->next;
    }
    printf("\n");
}

void printMatrix(avyuh *a)
{
    while (a != NULL)
    {
        printVector(a->vector);
        a = a->next;
    }
    printf("\n");
}

int main()
{
    // Quadratic equation: x^2 - 5x + 6 = 0
    avyuh *q = Listquad(1, -5, 6);
    printf("Roots: ");
    printVector(q->vector);

    // Standard basis vector
    avyuh *basis = Listbasis(4);
    printf("Basis vector: ");
    printVector(basis->vector);

    // Identity matrix
    avyuh *I = Listeye(3);
    printf("Identity matrix:\n");
    printMatrix(I);

    // Matrix A
    avyuh *A = createList(2, 2);

    A->vector->data = 1;
    A->vector->next->data = 2;
    A->next->vector->data = 3;
    A->next->vector->next->data = 4;

    printf("Matrix A:\n");
    printMatrix(A);

    // Trace and determinant
    printf("Trace = %.2lf\n", Listrace(A));
    printf("Determinant = %.2lf\n", Listdet(A));

    // Eigenvalues of A
    avyuh *eig = Listeigval(A);
    printf("Eigenvalues: ");
    printVector(eig->vector);

    // Section formula for vectors
    sadish *v1 = createVec(2);
    sadish *v2 = createVec(2);

    v1->data = 1;
    v1->next->data = 2;

    v2->data = 5;
    v2->next->data = 6;

    sadish *sectionVector = ListVecSec(v1, v2, 2);

    printf("Section vector: ");
    printVector(sectionVector);

    // Matrix B
    avyuh *B = createList(2, 2);

    B->vector->data = 5;
    B->vector->next->data = 6;
    B->next->vector->data = 7;
    B->next->vector->next->data = 8;

    // Section formula for matrices
    avyuh *sectionMatrix = Listsec(A, B, 2);

    printf("Section matrix:\n");
    printMatrix(sectionMatrix);

    // Circulant matrix
    avyuh *v = Listbasis(3);

    v->vector->data = 1;
    v->vector->next->data = 2;
    v->vector->next->next->data = 3;

    avyuh *C = circulantList(v);

    printf("Circulant matrix:\n");
    printMatrix(C);

    return 0;
}
