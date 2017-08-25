// Cormen's resolution (16.2-6)
//
// Mateus-n00b, August 2017
//
// License GPLv3+
//
// Version 1.0
#include "stdio.h"

int mochila_fracionaria(int val[], int p[], int n, int W){
    int total =0;
    int sol[n];
    for (int i = 0; i < n; i++)
        sol[i] = val[i]/p[i];

    for (int i = 0; i < n; i++)
        if (p[i] <= W){
            total+=val[i];
            W-=p[i];
        }
        else{
            total+= W*sol[i];
            W-=(W/p[i]);
        }
    return total;
}

int main(int argc, char const *argv[]) {
  int val[] = {60,100,120},
  peso[] = {10,20,30},
  W = 50;
  int n = sizeof(val)/sizeof(val[0]);

  printf("Total: %d\n",mochila_fracionaria(val,peso,n,W) );
  return 0;
}
