#include "lists.h"
/**
 * check_cycle - checks the cycle
 * @list: the linked list.
 *
 * Return: 1 on succes and 0 on failure.
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	listint_t *after_temp = list;

	if (!list || !list->next)
		return (0);

	while (temp && after_temp && after_temp->next)
	{
		temp = temp->next;
		after_temp = after_temp->next->next;

		if (temp == after_temp)
			return (1);
	}
	return (0);
}
