#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *slug, *hare;

	if (!list || list->next == NULL)
		return (0);

	slug = list->next;
	hare = list->next->next;

	for (; slug && hare && hare->next; )
	{
		if (slug == hare)
			return (1);

		slug = slug->next;
		hare = hare->next->next;
	}

	return (0);
}
