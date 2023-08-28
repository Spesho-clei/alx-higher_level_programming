#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - Prints basic info about a Python list object.
 * @p: A pointer to the Python list object.
 */
void print_python_list(PyObject *p)
{
    setbuf(stdout, NULL);  // Unbuffered output
    Py_ssize_t size, i;

    printf("[*] Python list info\n");
    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);

    for (i = 0; i < size; i++)
    {
        PyObject *element = PyList_GetItem(p, i);
        printf("Element %ld: ", i);

        if (PyFloat_Check(element))
        {
            printf("float\n");
        }
        else
        {
            printf("%s\n", Py_TYPE(element)->tp_name);
        }
    }
}

/**
 * print_python_bytes - Prints basic info about a Python bytes object.
 * @p: A pointer to the Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
    setbuf(stdout, NULL);  // Unbuffered output
    Py_ssize_t size, i;
    char *data;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_GET_SIZE(p);
    printf("  size: %ld\n", size);

    data = PyBytes_AsString(p);
    printf("  trying string: %s\n", data);

    printf("  first %ld bytes: ", (size > 10) ? 10 : size);
    for (i = 0; i < size && i < 10; i++)
        printf("%02x%c", (unsigned char)data[i], (i + 1 < size && i + 1 < 10) ? ' ' : '\n');
}

/**
 * print_python_float - Prints basic info about a Python float object.
 * @p: A pointer to the Python float object.
 */
void print_python_float(PyObject *p)
{
    setbuf(stdout, NULL);  // Unbuffered output
    double value;

    printf("[.] float object info\n");
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    value = PyFloat_AsDouble(p);
    printf("  value: %g\n", value);
}
