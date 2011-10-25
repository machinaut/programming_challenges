#include<stdlib.h>
#include<unistd.h>
#include<stdio.h>
#include<math.h>
#define MAXINT 0x7fffffff
int main() {
  int rides,paths,j,k,a,b,c,current,min,max,alt,found;
  int *distances,*dist,*checked;
  int park = 1;
  scanf("%d",&rides);
  while(rides > 0) { // iterate until get '0' rides
    printf("Park %d:\n",park); // === INITIALIZATION ===
    distances = (int*)malloc(rides*rides*sizeof(int));
    dist = (int*)malloc(rides*sizeof(int));
    checked = (int*)malloc(rides*sizeof(int));
    for (j=0;j<rides;j++) {
      for (k=0;k<rides;k++) { distances[j*rides+k] = MAXINT; }
      distances[j*rides+j] = 0;
    }
    scanf("%d",&paths);
    for (j=0;j<paths;j++) { // === READ INPUT ===
      scanf("%d",&a); scanf("%d",&b); scanf("%d",&c);
      distances[(a-1)*rides+(b-1)]=c; distances[(b-1)*rides+(a-1)]=c;
    }
    for (j=0;j<rides;j++) { // === ITERATE OVER RIDES ===
      for (k=0;k<rides;k++) { // initialize arrays
        dist[k] = MAXINT; checked[k] = 0;
      }
      printf("%d:",j); current = j; dist[j] = 0; checked[j] = 1; // Current ride
      while (1) { // Dijkstra's algorithm
        for (k=0;k<rides;k++) { // update dist
          alt = dist[current] + distances[current*rides+k];
          if (alt < dist[k] && distances[current*rides+k] < MAXINT) {
            dist[k] = alt; // update dist if better path
          }
        }
        found = -1; min = MAXINT;
        for (k=0;k<rides;k++) { // find next ride (closest)
          if (checked[k] == 0 && dist[k] < MAXINT && dist[k] < min) {
            found = k; min = dist[k];
          }
        }
        if (found == -1) { // all remaining rides unreachable
          break; 
        }
        current = found; checked[found] = 1; // 'step' to next ride
      }
      max = 0;
      for (k=0;k<rides;k++) { // find longest distance
        if (dist[k] > max) { max = dist[k]; }
      }
      for (k=0;k<rides;k++) { // print all rides with longest distance
        if (dist[k] == max) { printf(" %d",k+1); }
      } printf("\n");
    }
    free(distances); free(dist); free(checked);
    park += 1; scanf("%d",&rides); // Next park, read in rides again
  }
  return(0);
}
