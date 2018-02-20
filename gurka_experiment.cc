// Cool idea to test the effeccts of using the octal with descimal
#include  <stdio.h>

using namespace std;


void test_adding(int octal, int dec, int hex)
{
    
    printf("lets try adding base 10 and 8 together %d\n", dec + octal);
    
    printf("lets try adding base 8 and 16 together %d\n", octal + hex);

    printf("lets try adding base 10 and 16 together %d\n", dec + hex);

}

void test_subtraction(int octal, int dec, int hex)
{
    

}

int main (int argc, char *argv[])
{
    int octal = 0;  // octal number to play with
    int hex = 0x0;  // hex number because why not
    int dec = 0;    // decimal number can't tell the differince

    octal = 012;
    dec = 10;
    hex = 0xA;

    printf("the decimal = %d the octal = %d the hex = %d\n", dec, octal, hex);

    test_adding(octal, dec, hex);


}
