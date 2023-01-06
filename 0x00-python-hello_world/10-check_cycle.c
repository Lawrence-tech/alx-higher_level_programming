#include "lists.h"

/**
  *check_cycle - checks if a singly linked list has a cycle in it.
  *@list: list to check for loops
  *Return: 0 if there is no cycle, 1 if there is a cycle
  */

int check_cycle(listint_t *list)
{
	listint_t *ptr, *end;

	if (list == NULL)
		return (0);
	ptr = list;
	end = ptr->next;
	if (end == NULL)
		return (0);
	while (1)
	{
		if (end == ptr)
			return (1);
		if (end == NULL)
			return (0);
		end = end->next;
		if (end == NULL)
			return (0);
		ptr = ptr->next;
	}
}
