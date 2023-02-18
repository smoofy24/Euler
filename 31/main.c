#include <stdio.h>
#include <stdlib.h>
/*
 * Define possible coin values
 */
const int values[] = {200,100,50,20,10,5,2,1};

/*
 * Get size of the array
 */
size_t val_size = sizeof(values)/sizeof(*values);

int count  = 0;
int max;


/*
 * Define recursive function to count the value
 */
void adder(int sum, int index);

int main(int argc, char *argv[]) {
/*
 * Get argument
 */
	max = strtol(argv[1], NULL, 10);

/*
 * Use each value in array as a root for the recursion
 */
	adder(0, 0);

/*
 * Print the result
 */
	printf("%d\n", count);
}

void adder(int sum, int index) {
	int i;
	int tmp_sum;
	for (i=index; i<val_size; i++) {
		tmp_sum = sum + values[i];
		printf("%d + %d = %d\n", sum, values[i], tmp_sum);
		if (tmp_sum == max) {
		printf("%d = %d => increasing counter...\n", tmp_sum, max);
			count++;
		}
		else if (tmp_sum > max) {
			continue;
		}
		else {
			adder(tmp_sum, i);
		}
	}
}