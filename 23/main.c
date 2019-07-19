#include <stdio.h>

#define LIMIT 28123

int is_abundant(int x);

int main() {
	int array[7000];
	int count = 0;
	int tot_sum = 0;
	int check = 0;

    // Get the array of abundant numbers up to the LIMIT
	int i;
	for (i=0; i<=LIMIT; i++) { 
		if (is_abundant(i)==0) array[count++] = i;
	}

	int j,k;
	for (i=0; i<=LIMIT; i++) {
		check = 0;
		for (j=0; j<count; j++) {
			if (array[j]+array[0]>i) break;
			for (k=0; k<count; k++) {
				if (array[j]+array[k]==i) {
					//printf("%d\n",i);
					//printf("%d+%d==%d\n",array[j],array[k],array[j]+array[k]);
					check = 1;
				}
				if (array[j]+array[k]>i) break;
			}

		}
		if(check!=1) tot_sum+=i;
		//printf("%d %d\n",i, check);
	}
	printf("%d\n",tot_sum);
}

int is_abundant(int x) {
	int sum = 0;
	int i;
	for (i=1; i<=x/2; i++) {
		if (x%i==0) sum+=i;
	//	printf("%d\n",sum);
	}
	if (sum>x) 
		return 0;
	else
		return 1;
}
