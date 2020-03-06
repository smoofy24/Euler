#include <stdio.h>

int print_number(int num) {
	int un = num%10;
	int te = num - un;
	int sub_sum = 0;
	switch(num)
	{
		case 1:
			printf("one");
			sub_sum = 3;
			break;
		case 2:
			printf("two");
			sub_sum = 3;
			break;
		case 3:
			printf("three");
			sub_sum = 5;
			break;
		case 4:
			printf("four");
			sub_sum = 4;
			break;
		case 5:
			printf("five");
			sub_sum = 4;
			break;
		case 6:
			printf("six");
			sub_sum = 3;
			break;
		case 7:
			printf("seven");
			sub_sum = 5;
			break;
		case 8:
			printf("eight");
			sub_sum = 5;
			break;
		case 9:
			printf("nine");
			sub_sum = 4;
			break;
		case 10:
			printf("ten");
			sub_sum = 3;
			break;
		case 11:
			printf("eleven");
			sub_sum = 6;
			break;
		case 12:
			printf("twelve");
			sub_sum = 6;
			break;
		case 13:
			printf("thirteen");
			sub_sum = 8;
			break;
		case 14:
			printf("fourteen");
			sub_sum = 8;
			break;
		case 15:
			printf("fifteen");
			sub_sum = 7;
			break;
		case 16:
			printf("sixteen");
			sub_sum = 7;
			break;
		case 17:
			printf("seventeen");
			sub_sum = 9;
			break;
		case 18:
			printf("eighteen");
			sub_sum = 8;
			break;	
		case 19:
			printf("nineteen");
			sub_sum = 8;
			break;
		case 20:
			printf("twenty");
			sub_sum = 6;
			break;	
		case 30:
			printf("thirty");
			sub_sum = 6;
			break;
		case 40:
			printf("forty");
			sub_sum = 5;
			break;
		case 50:
			printf("fifty");
			sub_sum = 5;
			break;
		case 60:
			printf("sixty");
			sub_sum = 5;
			break;
		case 70:
			printf("seventy");
			sub_sum = 7;
			break;
		case 80:
			printf("eighty");
			sub_sum = 6;
			break;
		case 90:
			printf("ninety");
			sub_sum = 6;
			break;
		default:
			sub_sum = sub_sum + print_number(te);
			printf(" ");
			sub_sum = sub_sum + print_number(un);
			break;
	}
	return sub_sum;
}

int main() {
	int th, hu, re;

	int sum = 0;
	int i; 
	for (i=0; i<=1000; i++)
	{
		th = (i/1000)%10;
		hu = (i/100)%10;
		re = i%100;
		
		if (th!=0) {
			sum = sum + print_number(th);
			printf(" thousand");
			sum=sum+8;
		}
		if (hu!=0) {
			sum = sum + print_number(hu);
			printf(" hundred");
			sum=sum+7;
		}
		if (re!=0) {
			if ((th!=0) || (hu!=0)) {
				printf(" and ");
				sum=sum+3;
			}
			sum = sum + print_number(re);
		}
		printf(" %d\n",sum);
	}	
}