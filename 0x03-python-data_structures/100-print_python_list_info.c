#include "Python.h"
#include "lists.h"
#include <stdio.h>

/**
  *print_python_list_info - prints some basic info about Python lists
  *@p: pointer
  */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *) p;
	long long count = -1, size;

	size = (long long) Py_SIZE(p);
	printf("[*] Size of the Python List = %lld\n", size);
	printf("[*] Allocated = %lld\n", (long long) list->allocated);
	while (++count < size)
		printf("Element %lld: %s\n", count, Py_TYPE(list->ob_item[count])->tp_name);
}
