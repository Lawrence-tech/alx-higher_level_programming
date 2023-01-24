#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for s in range(x):
        print("{:d}".format(my_list[s]), end='')
        count += 1
    except ValueError:
        continue
    except TypeError:
        continue
    print('')
    return count
