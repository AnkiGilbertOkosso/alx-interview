#!/usr/bin/python3
'''The minimum operations.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.

    :param n: The target number of H characters.
    :type n: int
    :return: The fewest number of operations needed.
    :rtype: int
    '''
    if not isinstance(n, int):
        return 0
    operations_count = 0
    clipboard = 0
    done = 1
    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            operations_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            operations_count += 2
        elif clipboard > 0:
            done += clipboard
            operations_count += 1
    return operations_count
