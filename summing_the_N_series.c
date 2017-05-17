#include "stdio.h"
int sum(int n){
    int i;
    int s = 0;
    for (i = 1; i <=n; i++) {
        s+=2*i-1;
    }
    return s;
}

int main(int argc, char const *argv[]) {
  int t,i,n;
  scanf("%d",&t );
  int out[t];
  for (i = 0; i < t; i++) {
      scanf("%d", &n);
      out[i]=sum(n);
  }

  for (i = 0; i < t; i++) {
      printf("%d\n",out[i] );
  }
  return 0;
}
