#include "lists.h"

/**
 * is_palindrome- to check if a linked list
 * reads the same backward as forward(palirome)
 *
 * @head: pointer to the head of list
 *
 * Return: 1 if list is a palidrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *man, *kc, *mario;
	int count = 1;

	if (*head == NULL)
		return (1);
	mario = kc = *head;
	temp = man = NULL;

	while (kc != NULL)
	{
		temp = kc->next;
		kc->next = man;
		man = kc;
		kc = temp;
	}
	while (mario != NULL)
	{
		if (mario->n == man->n)
		{
			if (mario->next == NULL)
				break;
			mario = mario->next;
			man = man->next;
			continue;
		}
		else
		{
			count -= 1;
			break;
		}
	}
	if (mario->n == man->n)
		return (count);
	else
		return (0);
}
