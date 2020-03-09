#include <stdio.h>
#include <stdlib.h>

struct node 
{
	int exp;
	int base;
	struct node *next;
};


/*
 * Create array and feed it with all the possible values
 */
struct node *init_array(int num_range, int exp_range)
{
	int i,j;

	// Define and alocate the memory for the header
	struct node *head = malloc(sizeof(struct node));
	struct node *last = head;

	for (i=2; i<=num_range; i++)
	{
		for (j=2; j<=exp_range; j++)
		{
			last->base = i;
			last->exp = j;
			if ((i==num_range) && (j==exp_range)) 
				last->next = NULL;
			else
				last->next = malloc(sizeof(struct node));
		}
	}

	return head;
}

int destroy_array(struct node *array)
{
	struct node *next;
	do
	{
		next = array->next;
		free(array);
		array = next;
	}
	while (next != NULL);

	return 0;
}

int main ()
{
	int test;
	
	struct node *list = init_array(100,100);

	destroy_array(list);
	
	return 0;
}