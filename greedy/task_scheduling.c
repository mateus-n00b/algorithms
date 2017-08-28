#include "stdio.h"

void task_scheduler(int s[], int f[], int n){
      int A[n];
      A[0] = 1; // Primeira tarefa
      int k = 0;
      for (int i = 1; i < n; i++)
            if (s[k] >= f[i]){
                A[i] = i+1;
                k = i;
                printf("%d\n", i);
            }
}

int main(int argc, char const *argv[]) {
  int s[] = {12,2,8,8,6,5,3,5,0,3,1};
  int f[] = {16,14,12,11,10,9,9,7,6,5,4};
  int n = sizeof(s)/sizeof(s[0]);

  task_scheduler(s,f,n);
  // int *A = task_scheduler(s,f,n);
  // for (int i = 0; i < n; i++)
  //       printf("%d ", A[i]);
  // printf("\n" );
  return 0;
}
