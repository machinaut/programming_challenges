#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int main(){
  int s,n;
  int *l;
  int *m;
  int i,j,k;
  scanf("%d",&s);
  while (0 != s) {
    scanf("%d", &n);
    //printf("s %d n %d\n",s, n);
    l = (int*)malloc(sizeof(int)*n);
    for (i = 0; i < n; i++) {
      scanf("%d", &(l[i]));
    }

    m = (int*)malloc(sizeof(int)*(l[n-1]*s+1));
    for (i=0;i<=l[n-1]*s;i++) {
      m[i] = -1;
    }

    m[0] = 0;
    for (i=0;i<n;i++) { // for i in coins
      for (j = 0 ; j <= l[n-1]*s ; j++) { // for value
        if (j >= l[i] && m[j-l[i]] >=0 && m[j-l[i]] < s) {
          if (m[j] < 0 || m[j-l[i]] + 1 < m[j]) {
            m[j] = m[j-l[i]] + 1;
          }
          //printf("found at i %d j %d l[i] %d m[j-l[i]] %d m[j] %d\n",
              //i,j,l[i],m[j-l[i]],m[j]);
        }
      }
    }
    for (i=0; i<= l[n-1]*s; i++) {
      if (m[i] < 0) { break; }
    }
    printf("%d\n",i>0?i-1:0);

    scanf("%d", &s);
  }
  return 0;
}
