#include <math.h>
#include <stdio.h>

int is_prime(int number) 
{
  int i;
  int flag = 1;

  for (i = 2; i <= sqrt(number); i++) 
  {
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

int reverse(int number)
{
  int rest = 0;
  int new_int = 0;
  
  while (number != 0) 
  {
    rest = number % 10;
    new_int = new_int*10 + rest;
    number = number / 10;
  }
  return new_int;
}

int main() 
{
  int cnt = 0;
  int x = 3;
  int y;
  int sum = 0;

  while (cnt<50)
  {
    y=reverse(x);
    if (is_prime(x) && (is_prime(y)) && (x != y))
    {
      printf("%d\n",x);
//     printf("%d is prime and its reverse %d also\n",x, y);
//     printf("%d + %d = %d\n",sum, x, sum+x);
      sum = sum + x;
      cnt++;
    }
    x++;
  }

//  printf("%d\n", sum);
}

