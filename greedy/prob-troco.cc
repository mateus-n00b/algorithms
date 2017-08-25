// Exchange problem -
// Input: a float value representing an amount of money
// Output: the Total of 'coins' necessary to exchange the value
//
// Coded by Mateus Sousa (n00b)
// License GPLv3+
#include "iostream"

using namespace std;

int solver_troco(int num,int coins[]){
    int k = 0,
    cont = 0;
    int n = 6; // Lentgh of coins
    while (k < n) {
          if (num/coins[k] > 0) {
              cont+= num/coins[k];
              num%=coins[k];
          }
          k++;
    }
    return cont;
}

main(){
      // Usual coins in Brazil
      int coins[] = {100,50,25,10,5,1};
      float value;
      std::cout << "Value: ";
      std::cin >> value;
      value *= 100;
      std::cout << "Total >> "<< solver_troco(value,coins) << std::endl;
}
