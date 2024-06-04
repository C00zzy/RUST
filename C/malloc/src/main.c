#include <stdlib.h>
#include <stdio.h>

int main ()
{
    (malloc(1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024));
    while (1);
    return 0;
}