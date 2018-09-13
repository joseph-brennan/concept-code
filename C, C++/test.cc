#include <stdio.h>
using namespace std;

void swap(int a, int b) {
    int temp;
    temp = a;
    a = b;
    b = temp;
}

int main(int arg, char *argv[]) {
    printf("Hello World vim \n");
    int value = 2;
    int list[5] = {1, 3, 5, 7, 9};
    
    swap(value, list[0]);
    printf("value = %d, list = %d %d %d %d %d\n", value, list[0], list[1], list[2], list[3], list[4]);
  
    swap(list[0], list[1]);
    printf("value = %d, list = %d %d %d %d %d\n", value, list[0], list[1], list[2], list[3], list[4]);

    swap(value, list[value]);
    printf("value = %d, list = %d %d %d %d %d\n", value, list[0], list[1], list[2], list[3], list[4]);
}
