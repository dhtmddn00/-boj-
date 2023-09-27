#include <stdio.h>
#include <stdlib.h>
#define swap(a, b) {int* tmp=a; a=b; b=tmp;}
#define _CRT_SECURE_NO_WARNINGS
#pragma warning(disable : 4996)

int main()
{
    int n, m, q;
    scanf("%d %d %d", &n, &m, &q);
    int** arr = (int**)malloc(sizeof(int*) * n); // 수정: int* 형식의 포인터 배열 생성

    for (int i = 0; i < n; i++)
    {
        arr[i] = (int*)malloc(sizeof(int) * m); // 수정: 각 행에 대해 동적 할당
        for (int j = 0; j < m; j++)
        {
            scanf("%d", &arr[i][j]);
        }
    }
    int a, b, c;

    int count = 0;
    while (count < q)
    {
        scanf("%d", &a);
        if (a == 0)
        {
            scanf("%d %d %d", &a, &b, &c);
            arr[a][b] = c;
            count++;
        }
        else {
            scanf("%d %d", &a, &b);
            swap(arr[a], arr[b]);
            count++;
        }
    }

    for (int i = 0;i < n;i++)
    {
        for (int j = 0;j < m;j++)
        {
            printf("%d ", arr[i][j]);

        }
        printf("\n");
    }








}