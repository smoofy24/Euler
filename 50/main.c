#include <math.h>
#include <stdio.h>

int is_prime(int number) 
{
  int i;
  int flag = 1;

  for (i = 2; i <= sqrt(number); i++) {
    if (number % i == 0) {
      flag = 0;
      break;
   }
  }

  if ( number <= 1 )
    flag = 0;

  if (flag == 1 )
    return 1;
  else
    return 0;
}

int main() 
{
  char str[1000] = "2";
  int sum = 2, count = 2;

  while (sum<1000000)
  {
    count=count+1;
    if (is_prime(count))
    {
      sum=sum+count;
      snprintf(str, 1000, "%s+%d", str, count);
      printf("%s=%d\n",str,sum);
      if (is_prime(sum))
      {
        printf("Sum %d is prime.\n",sum);
      }
    }
  }
  printf("Result is %d.\n",sum);
}
