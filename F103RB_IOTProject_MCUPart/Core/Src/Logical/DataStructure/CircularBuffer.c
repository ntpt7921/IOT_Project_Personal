/*
 * circular_buffer.c
 *
 *  Created on: Nov 13, 2022
 *      Author: ntpt
 */

#include <Logical/DataStructure/CircularBuffer.h>
#include <Logical/Error/Error.h>
#include <string.h>

static inline
size_t get_last_index(size_t max_count, size_t index, size_t count)
{
    return (index + count) % max_count;
}

static inline
void *get_element_address(void *arr, size_t esize, size_t index)
{
    return (void*) ((uint8_t*) arr + esize * index);
}


void CircularBuffer_Insert(void *arr, size_t asize, size_t esize,
        size_t *head, size_t *count, void *elem)
{
    if (*count == asize) // full
    {
        Error_SetStatus(ERR_CIRBUFF_FULLINSERT);
        return;
    }

    size_t insert_index = get_last_index(asize, *head, *count);
    void * insert_address = get_element_address(arr, esize, insert_index);

    memcpy(insert_address, elem, esize);;
    (*count)++;
}

void CircularBuffer_Delete(size_t asize, size_t *head, size_t *count)
{
    if (*count == 0) // nothing left to delete
    {
        Error_SetStatus(ERR_CIRBUFF_EMPTYDELETE);
        return;
    }

    *head = (*head + 1) % asize;
    (*count)--;
}
