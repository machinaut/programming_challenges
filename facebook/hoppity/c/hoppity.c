#include <stdio.h>
#include <stdlib.h>

int
main (int argc, char *argv[])
{
    long long int n;

    fscanf(fopen(argv[1],"r"), "%lld", &n);

    for (int i = 0; i < n/15; i++)
        puts("Hoppity\nHophop\nHoppity\n"
            "Hoppity\nHophop\nHoppity\nHop\n");
    for (int i = 0; i < n%15; i++) {
        if (i %  5 == 0) puts("Hophop\n");
        else if (i %  3 == 0) puts("Hoppity\n");
    }

    return EXIT_SUCCESS;
}
