#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev_of_slow = *head;
    listint_t *second_half;
    int is_palindrome = 1;

    if (*head != NULL && (*head)->next != NULL)
    {
        while (fast != NULL && fast->next != NULL)
        {
            fast = fast->next->next;
            prev_of_slow = slow;
            slow = slow->next;
        }

        if (fast != NULL)
        {
            slow = slow->next;
        }

        second_half = slow;
        prev_of_slow->next = NULL;
        listint_t *prev = NULL;
        listint_t *current = second_half;
        listint_t *next;
        while (current != NULL)
        {
            next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }

        listint_t *first = *head;
        second_half = prev;
        while (second_half != NULL)
        {
            if (first->n != second_half->n)
            {
                is_palindrome = 0;
                break;
            }
            first = first->next;
            second_half = second_half->next;
        }

        prev = NULL;
        current = prev_of_slow;
        next = NULL;
        while (current != NULL)
        {
            next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }
        prev_of_slow->next = prev;
    }

    return (is_palindrome);
}