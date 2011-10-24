#include<stdlib.h>
#include<unistd.h>
#include<stdio.h>
#include<string.h>
#define EXTENT 26
// TODO: can cut half iterations by only doing i=0, j=i
int main () {
int circuits,ckt;
char *line = (char*)malloc(1026*sizeof(char));
char *resistor= NULL;
size_t size=1026;
int count,a,b,i,j;
double tab[EXTENT][EXTENT]; // resistance table
int con[EXTENT]; // connectivity table
double sol,aa,bb;
getline(&line,&size,stdin);
sscanf(line,"%d\n",&circuits);
for (ckt=0;ckt<circuits;ckt++) {
  for (i=0;i<EXTENT;i++) {
    for(j=0;j<EXTENT;j++) {
      tab[i][j] = 0.;
    }
  }
  getline(&line,&size,stdin);
  resistor = strtok(line," \n");
  while (resistor != NULL) {
    a = (int)resistor[0]-97;
    b = (int)resistor[1]-97;
    if (tab[a][b] > 0.) {
      sol = 1./(1./tab[a][b] + 1.);
    } else {
      sol = 1.;
    }
    tab[a][b] = sol;
    tab[b][a] = sol;
    resistor = strtok(NULL," \n");
  }
  count = 1;
  while (count > 0) { 
    for (i=0;i<EXTENT;i++) { 
      con[i] = 0;
    }
    for (i=0;i<EXTENT;i++) {
      for (j=i;j<EXTENT;j++) { 
        if (tab[i][j] > 0.) {
          con[i] += 1;
          con[j] += 1;
        }
      }
    }
    count = 0;
    for (i=1;i<EXTENT-1;i++) { 
      if (con[i] == 2) {
        count += 1;
        // find other ends
        aa = 0.; bb = 0.;
        a = 0; b = 0;
        for (j=0;j<EXTENT;j++) {
          if (tab[i][j] > 0.) {
            a = j; aa = tab[i][j]; break;
          }
        }
        for (j=0;j<EXTENT;j++) {
          if (tab[j][i] > 0. && j != a) {
            b = j; bb = tab[j][i]; break;
          }
        }
        if (tab[a][b] > 0.) {
          sol = 1./(1./tab[a][b] + 1./(aa+bb));
        } else {
          sol = aa+bb;
        }
        tab[a][b] = sol;
        tab[b][a] = sol;
        tab[i][a] = 0.;
        tab[i][b] = 0.;
        tab[a][i] = 0.;
        tab[b][i] = 0.;
      }
    }
  /*for (i=0;i<EXTENT;i++) { 
    for(j=0;j<EXTENT;j++) {
      printf("%g ",tab[i][j]);
    } printf("\n");
  } */
  }
  printf("%0.4f\n",tab[0][EXTENT-1]);
}
return(0);
}
