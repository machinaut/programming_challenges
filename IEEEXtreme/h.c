#include<stdlib.h>
#include<unistd.h>
#include<stdio.h>
typedef struct {
  int i;
  int x;
  int v;
  int final;
} ball;
static int cmpinit(const void *a, const void *b) {
  int i = ((ball*)a)->x;
  int j = ((ball*)b)->x;
  return i>j?1:(i<j?-1:0);
}
static int cmpball(const void *a, const void *b) {
  int i = ((ball*)a)->final;
  int j = ((ball*)b)->final;
  return i>j?1:(i<j?-1:0);
}
int main() {
int simulations,sim;
int n,i,x,v,target,time,end;
ball tab[250];
scanf("%d", &simulations);
for (sim=0;sim<simulations;sim++) {
  scanf("%d",&n);
  for (i=0;i<n;i++) {
    scanf("%d",&x);
    scanf("%d",&v);
    tab[i].i = i+1; tab[i].x = x; tab[i].v = v;
  }
  scanf("%d", &target);
  scanf("%d", &time);
  qsort(tab,n,sizeof(ball),cmpinit);
  for (i=0;i<n;i++) {
    if (tab[i].i == target) {
      target = i;
      break;
    }
  }
  for (i=0;i<n;i++) {
    end = tab[i].v*time+tab[i].x;
    tab[i].final = end > 0 ? (end < 100 ? end : 100) : 0;
  }
  qsort(tab,n,sizeof(ball),cmpball);
  printf("%d",tab[target].final);
  if(sim+1<simulations) {
    printf("\n");
  }
}
printf("\n");
return(0);
}
