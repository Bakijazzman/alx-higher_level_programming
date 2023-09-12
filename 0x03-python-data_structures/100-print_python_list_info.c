#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - Prints info about a Python list obj
 * @p: reference to the Python list object
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	unsigned int i;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));

	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < Py_SIZE(p); i++)
		printf("Element %d: %s\n", idx, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
