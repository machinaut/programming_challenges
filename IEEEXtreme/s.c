#include<stdlib.h>
#include<unistd.h>
#include<stdio.h>
#include<math.h>
int main() {
  double first,last,current,area=0;
  scanf("%lf",&first);
  last = first;
  while ( 0 < scanf("%lf",&current)) {
    area += 0.5*sin((current-last)*M_PI);
    last = current;
  }
  area += 0.5*sin((2.-last+first)*M_PI);
  printf("%.2f",area);
  return(0);
}
