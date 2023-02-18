#include <math.h>
#include <stdio.h>
#include <stdint.h>

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

uint64_t reverse(uint64_t number)
{
  int rest = 0;
  uint64_t new_int = 0;
  
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
  uint64_t s,y,z;
  int sum = 0;

  while (cnt<50)
  {
    if (is_prime(x))
    {
      y = x*x;
      z = reverse(y);
      s = sqrt(z);
      if (!ceilf(s))
        x++;
        continue;
      if ((y != z) && (is_prime(y)) && (is_prime(s)))
      {
        cnt++;
        sum = sum + x;
      }
    }
    x++;
  }

  printf("%d\n", sum);
}

