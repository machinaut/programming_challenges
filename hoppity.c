#include <stdio.h>
#include <stdlib.h>

#define BUFFERSIZE 50

int
main (int argc, char *argv[])
{
    FILE *input = fopen(argv[1],"r"); /* input file */

    /* Input buffer */
    char *buf = malloc(sizeof(char) * BUFFERSIZE); 
    size_t n = BUFFERSIZE;  /* size of the buffer */

    ssize_t ret = getline(&buf, &n, input);


    return EXIT_SUCCESS;
}
