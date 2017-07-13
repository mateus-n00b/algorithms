/*
At the annual meeting of Board of Directors of Acme Inc, every one
starts shaking hands with everyone else in the room.
Given the fact that any two persons shake hand exactly once, Can you tell the total count of handshakes?

Input Format:
The first line contains the number of test cases T, T lines follow.
Each line then contains an integer N, the total number of Board of Directors of Acme.

Output Format
Print the number of handshakes for each test-case in a new line.


Problema do handshake - no site www.hackerhank.com

Mateus Sousa, Maio 2017
Entrada um: numero de testes a serem realizados. Ex:
1 // somente um teste
2 // teste com 2 pessoas

*/

#include "iostream"
using namespace std;


int main(){
    int T,val=0;
    cin >> T;
    int array[T];
    for(int a0 = 0; a0 < T; a0++){
        int N;
        cin >> N;
        switch(N){
            case 1:
                    array[a0] = 0;
                    break;
            case 2:
                    array[a0] = 1;
                    break;
            default:
                    for (int shake = N; shake >1; shake--){
                        val+=shake-1;
                    }
                    array[a0] = val;
                    val = 0;
                    break;
        }
    }
    for (int i = 0; i < T; i++) {
        std::cout << array[i] << std::endl;
    }
    return 0;
}
