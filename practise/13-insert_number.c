#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *temp;
	if (*head == NULL)
		return (NULL);

	temp = *head;
	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	if (temp->n > number)
	{
		node->next= temp;
		temp = node;
		return (node);
	}
	
	while (temp->n < number)
	{
		temp = temp->next;
		if (temp->next->n > number)
			break;
	}
	node->next = temp->next;
	temp->next = node;
	return (node);

}
