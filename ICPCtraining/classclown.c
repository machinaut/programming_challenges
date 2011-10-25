#include<stdlib.h>
#include<unistd.h>
#include<stdio.h>
#include<math.h>
typedef struct {
  double x,y,dir,dist,wid;
} info;
int main() {
  int n,m,i,j,visible;
  double x,y,dx,dy,theta,len,dir,dist,wid;
  scanf("%d",&n); // num informers
  info *t = (info*)malloc(n*sizeof(info));
  for (i=0;i<n;i++) { // read informats
    scanf("%lf",&(t[i].x));
    scanf("%lf",&(t[i].y));
    scanf("%lf",&(t[i].dir));
    scanf("%lf",&(t[i].dist));
    scanf("%lf",&(t[i].wid));
  }
  scanf("%d",&m);
  for (j=0;j<m;j++) { // read and parse desks
    scanf("%lf",&x);
    scanf("%lf",&y);
    visible = 1;
    for (i=0;i<n;i++) { // check informants
      dy = y-t[i].y;
      dx = x-t[i].x;
      theta = atan2(dy,dx);
      len = sqrt(dy*dy+dx*dx);
      dir = t[i].dir;
      dist = t[i].dist;
      wid = t[i].wid;
      if (dir-wid/2 <= theta && theta <= dir+wid/2 && len <= dist) {
        visible = 0;
        break;
      }
    }
    if (visible == 1) {
      printf("%g %g\n",x,y);
    }
  }
  return(0);
}
