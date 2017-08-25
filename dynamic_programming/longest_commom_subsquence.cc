#include <bits/stdc++.h>

#define max(a,b) (a>b) ? a : b

int lcs(char *X, char *Y, int m,int n){
    int c[m+1][n+1];

    for (int i = 0; i <= m ; i++) {
        for (int j = 0; j <= n; j++) {
            if (i==0|| j == 0)
                c[i][j] = 0;
            else if (X[i] == Y[j])
                  c[i][j] = c[i-1][j-1]+1;
            else
                  c[i][j] = max(c[i][j-1],c[i-1][j]);
        }
    }
    return c[m][n];
}

int main(int argc, char const *argv[]) {
  char X[] = "AGGTAB",
  Y[] = "GXTXAYB";

  int m = strlen(X),
  n = strlen(Y);

  printf("Length of LCS is %d\n", lcs(X,Y,m,n));

  return 0;
}
