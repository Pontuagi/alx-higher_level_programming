#include <stdio.h>
#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - A function that inserts a number into a sorted singly linked
 * list
 * @head: the head of the linked list
 * @number: the number to add to the list
 *
 * Return: the address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *prev;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	current = *head;
	prev = NULL;

	while (current != NULL && number > current->n)
	{
		prev = current;
		current = current->next;
	}

	new_node->next = current;
	if (prev != NULL)
		prev->next = new_node;
	else
		*head = new_node;

	return (new_node);
}
