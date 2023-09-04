#include "lists.h"

/**
 * check_cycle - find a loop in a list
 * @list: points to the start of the list
 * Return: 0 if no cycle, 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slug, *hare;
	
	slug = list;
	hare = list;
	while (slug && hare && hare->next)
	{
		hare = hare->next->next;
		slug = slug->next;
		if (slug == hare)
			return (1);
	}
	return (0);
}
