#include "stdio.h"

int max(int a, int b) { return (a > b)? a : b; }

int knapsack(int W, int v[],int wt[],int n){
    int i,w,table[n+1][W+1];

    for (i = 0; i <= n; i++)
        for (w= 0; w<= W;w++) {
          if (i == 0 || w == 0)
              table[i][w] = 0;
          else if (wt[i-1] <= w)
                  table[i][w] = max(v[i-1]+table[i-1][w-wt[i-1]],table[i-1][w]);
          else
              table[i][w] = table[i-1][w];
        }

        return table[n][W];
}


int main(int argc, char const *argv[]) {
  int n,i,W;
  printf("n = " );
  scanf("%d",&n );

  printf("W = " );
  scanf("%d",&W );

  int values[n];
  int weight[n];

  printf("Values = ");
  for (i= 0; i< n;i++)
      scanf("%d",&values[i]);
  printf("Weights = ");
  for (i= 0; i< n;i++)
      scanf("%d",&weight[i]);

  printf("%d\n",knapsack(W,values,weight, n));

  return 0;
}
