#include<stdlib.h>
#include<unistd.h>
#include<stdio.h>
#include<math.h>

int main() {
  double sumx = 0;
  double sumy = 0;
  double sumxy = 0;
  double sumx2 = 0; 
  double sumy2 = 0;
  double p;
  int c= 0;
  int a,b;
  while ( 0 < scanf("%d,",&a)) {
    scanf("%d",&b);
    sumx += (double)a;
    sumy += (double)b;
    sumxy += (double)(a*b);
    sumx2 += (double)(a*a);
    sumy2 += (double)(b*b);
    c += 1;
  }
  sumx /= (double)c;
  sumy /= (double)c;
  sumxy /= (double)c;
  sumx2 /= (double)c;
  sumy2 /= (double)c;
  p = (sumxy-sumx*sumy)/(sqrt(sumx2-sumx*sumx)*sqrt(sumy2-sumy*sumy));
  if (isnan(p)){
    printf("invalid input");
  } else {
    printf("%0.4f",p);
  }
  return(0);
}
