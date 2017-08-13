#include "stdio.h"

int dynamic_fib(int num){
    int i,table[num+1];

    // Preenche a tabela com 0s
    memset(table,0,sizeof(table));
    // Casos Base
    table[0] = 0;
    table[1] = 1;

    // Fibonnaci!!!
    for (i = 2; i <= num; i++) {
        table[i] += table[i-1]+table[i-2];
    }

    return table[num];
}


int main(int argc, char const *argv[]) {
  int n;
  scanf("%d",&n );
  printf("fib(%d) = %d\n",n,dynamic_fib(n));
  return 0;
}
