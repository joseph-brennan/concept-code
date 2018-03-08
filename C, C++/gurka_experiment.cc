// Cool idea to test the effeccts of using the octal with descimal
#include  <stdio.h>
//#include <iostream>

//using namespace std;


void test_adding(int octal, int dec, int hex)
{
    
    printf("lets try adding base 10 and 8 together %d\n", dec + octal);
    
    printf("lets try adding base 8 and 16 together %d\n", octal + hex);

    printf("lets try adding base 10 and 16 together %d\n", dec + hex);

    printf("another test using numbers base 8 and 10 should as always %d\n", 012 + 10);

}

void test_subtraction(int octal, int dec, int hex)
{
    printf("lets try subtracting base 10 and 8 together %d\n", dec - octal);
    
    printf("lets try subtracting base 8 and 16 together %d\n", octal - hex);

    printf("lets try subtracting base 10 and 16 together %d\n", dec - hex);

    printf("another test using numbers base 8 and 10 should as always %d\n", 012 - 10);


}

int main (int argc, char *argv[])
{
    char answer;
    const char *value[3] = {"decimal", "hex (repsented by 0x#)", "octal (represented by 0#)"};

    int math[3] = {0, 0x0, 00};
    int test1 = 0;
    int test2 = 2;


    printf("Would you like to define you own values?\n");
    scanf(" %c", &answer);
    

    if ((answer == 'Y') || (answer == 'y'))
    {
        for(int i = 0; i < 3; i++)
        {
            printf("Enter %s value\n", value[i]);

            scanf("%d", &math[i]);

        }   

    }

    else
    {
        math[2] = 012;
        math[0] = 10;
        math[1] = 0xA;

    }


    printf("the decimal = %d the octal = %d the hex = %d\n", math[0], math[2], math[1]);
    
    printf("addition\n");

    test_adding(math[2], math[0], math[1]);
    
    printf("subtraction\n");

    test_subtraction(math[2], math[0], math[1]);


}
