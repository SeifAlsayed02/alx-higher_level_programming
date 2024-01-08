#include <stdio.h>
#include "lists.h"
/**
 * is_palindrome - Check if a singly linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 *
 *
 * Return: 0 if not a palindrome, 1 if a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		listint_t *next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}

	if (fast != NULL)
		slow = slow->next;

	while (prev != NULL && slow != NULL)
	{
		if (prev->n != slow->n)
			return (0);
		prev = prev->next;
		slow = slow->next;
	}

	return (1);
}
