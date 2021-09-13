#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * palindrome - check palindrome in sigly linked list
 * @left: init singly linked list
 * @right: end singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 **/
int palindrome(listint_t **left, listint_t *right)
{
	int isPalindrome;
	if (right == NULL)
	{
		return (1);
	}
	isPalindrome = (palindrome(left, right->next) && (*left)->n == right->n);
	*left = (*left)->next;
	return (isPalindrome);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (!(*head) || !head)
	{
		return (1);
	}
	return (palindrome(head, *head));
}
