#include <stdio.h>

int fun (int *k) 
{
	*k += 4;
	return 3 * (*k) - 1;
}

int main() 
{
	int i = 10, j = 10, sum1, sum2;
	sum1 = fun(&i) + (i / 2);
	sum2 = (j / 2) + fun(&j);
    printf("this is sum 1 %d\n", sum1);
    printf("this is sum 2 %d\n", sum2);
}
