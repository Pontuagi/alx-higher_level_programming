#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - A function that checks if a singly linked list has a cycle
 * @list: the singly linked list to check
 *
 * Return: 0 it there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list;
	fast = list;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
