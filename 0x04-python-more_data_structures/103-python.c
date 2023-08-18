#include <python.h>

void print_python_list(PyObject *p)
{
    int size, allocated;
    int i;
    PyObject *item;
    PyListObject *list = (PyListObject *)p;
    
    size = PyList_Size(p);
    allocated = list->allocated;
    
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", allocated);
    
    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
    }
}


#include <python.h>

void print_python_bytes(PyObject *p) {
    PyBytesObject *bytes = (PyBytesObject *)p;
    ssize_t size;
    char *byte_string;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    byte_string = PyBytes_AsString(p);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", byte_string);
    printf("  first %zd bytes: ", size + 1);

    if (size + 1 > 10) {
        size = 10;
    }

    for (ssize_t i = 0; i < size; i++) {
        printf("%02x", byte_string[i] & 0xff);
        if (i < size - 1) {
            printf(" ");
        }
    }

    printf("\n");
}
