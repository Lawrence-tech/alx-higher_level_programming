#include "lists.h"
#include <stdlib.h>

/**
  *is_pal_recur - function pointer to add nodes
  *@left: to left of node
  *@right: to right of node
  *Return: address of the new element or NULL if it fails
  */
listint_t *is_pal_recur(listint_t *left, listint_t *right)
{
	if (right->next == NULL)
		return (left->next);
	right = right->next;
	if (right->next == NULL)
	{
		if (left->n != left->next->n)
			return (NULL);
		if (left->next->next == NULL)
			return (left);
		return (left->next->next);
	}
	right = is_pal_recur(left->next, right->next);
	if (right == NULL)
		return (NULL);
	if (right->n == left->n)
	{
		if (right->next == NULL)
			return (left);
		return (right->next);
	}
	return (NULL);
}

/**
  *is_palindrome - checks if a singly linked list is a palindrome.
  *@head: pointer to head
  *Return: 0 if it is not a palindrome, 1 if it is a palindrome.
  */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	if (is_pal_recur(*head, *head) != NULL)
		return (1);
	return (0);
}
