/*
Sometimes when you are a Computer Science student, you’ll see an exercise or a problem involving the Fibonacci sequence.
This sequence has the first two values 0 (zero) and 1 (one) and each next value will always be the sum of the two preceding numbers.
By definition, the formula to find any Fibonacci number is:
fib(0) = 0
fib(1) = 1
fib(n) = fib(n-1) + fib(n-2);

One way of finding Fibonacci numbers is by recursive calls.
This is illustrated below, presenting the tree of derivation when we calculate fib(4), i.e. the fifth value of this sequence:

Fibonacci, How Many Calls? - URI ONLINE
*/
#include "iostream"
using namespace std;

int cont;
int fibonacci(int num){
    cont++;
    if (num == 0)
        return 0;
    if (num == 1)
      return 1;

    return fibonacci(num-1)+fibonacci(num-2);
}


main(){
  int n;
  std::cin >> n;
  int a[n];
  for (int i = 0; i < n; i++) {
      std::cin >> a[i];

  }
  for (int i = 0; i < n; i++) {
      int k = fibonacci(a[i]);
      std::cout << "fib("<< a[i] <<") = "<< cont-1 ;
      std::cout << " calls = " << k << std::endl;
      cont = 0;
  }
}
