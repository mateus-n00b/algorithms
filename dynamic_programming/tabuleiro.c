// Finds the shortest path in a table
// Mateus-n00b, August 2017
//
#include "stdio.h"

#define min(a,b) (a<b)?a:b
#define N 4

int path[N][N],q[N][N];

void inicializar(int X[N][N],int n){
        int i = n-1;
        for (int j = 0; j < n; j++) {
            path[i][j] = j;
            q[i][j] = X[i][j];
        }
        i = n-2;
        for (i ; i >= 0; i--)
            for (int j = 0; j < n; j++)
                  q[i][j] = 99999;
}

void tabuleiro(int X[N][N],int n){
    inicializar(X,n);
    for (int i = n-1; i > 0; i--){
      for (int j = 0; j < n; j++)
          for (int k = j-1; k <= j+1; k++)
                if (k>=0 && k<=n)
                    if (q[i-1][k] > q[i][j]+X[i-1][k]){
                        q[i-1][k] = q[i][j]+X[i-1][k];
                        path[i-1][k] = j;
                    }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            printf("%d  ", q[i][j]);
        printf("\n");
    }

    printf("The best path is=> " );
    int j = 0;
    for (int i = 0; i < n; i++)
        for (j; j < n; j++) {
            j = path[i][j];
            printf("%d ",path[i][j]);
            break;
        }
    printf("\n");
}

int main(int argc, char const *argv[]) {
  int matrix[N][N] = {
    {2,6,8,7},
    {3,4,6,9},
    {8,7,2,4},
    {3,5,2,1}
  };
  int n = sizeof(matrix)/sizeof(matrix[0]);
  tabuleiro(matrix,n);
  return 0;
}
