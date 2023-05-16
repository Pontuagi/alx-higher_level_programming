#include "lists.h"

/**
* is_palindrome - checks whether a singly linked list is a palindrome
* @head: pointer to the head of the linked list
*
* Return: 1 if a palindrome or 0 if not
*/
int is_palindrome(listint_t **head)
{
	listint_t *fast_ptr = *head;
	listint_t *slow_ptr = *head;
	listint_t *prev, *curr, *next, *first_part, *second_part;

	if (*head == NULL)
		return (1);

	while(fast_ptr != NULL && slow_ptr != NULL)
	{
		fast_ptr = fast_ptr->next->next;
		slow_ptr = slow_ptr->next;
	}
	prev = NULL;
	curr = slow_ptr;
	next = NULL;
	while(curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	first_part = *head;
	second_part = prev;
	while(second_part != NULL)
	{
		if (first_part->n != second_part->n)
			return (0);
		first_part = first_part->next;
		second_part = second_part->next;
	}

	return (1);
}
