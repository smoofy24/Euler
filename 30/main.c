#include <math.h>
#include <stdio.h>

#define LIMIT 1000000;

int get_pow5sum(int num)
{
	int sum = 0;
	do
	{
		sum = sum + pow(num%10,5);
		num = num/10;
	}
	while (num!=0);
	return sum;
}

int main()
{
	int i;
	int total = 0;
	for (i=2; i<=1000000; i++)
	{

		if(get_pow5sum(i)==i) 
		{
			total = total + i;
			printf("%d\n",i);
		}
	}

	printf("%d\n",total);
	return 0;
}