#include <stdio.h>
#include <stdlib.h>

#define BUFFERSIZE 50

int
main (int argc, char *argv[])
{
    long long int n;

    fscanf(fopen(argv[1],"r"), "%lld", &n);

    for (int i = 1; i <= n; i++) {
        if (i % 15 == 0) {
            printf("Hop\n");
        } else if (i % 5 == 0) {
            printf("Hophop\n");
        } else if (i % 3 == 0) {
            printf("Hoppity\n");
        }
    }

    return EXIT_SUCCESS;
}
