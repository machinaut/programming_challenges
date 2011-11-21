#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int main(){
  int n,k;
  int *s;
  int *m;
  int i,j;
  scanf("%d",&n);
  while (0 != n) {
    s = (int*)malloc(sizeof(int)*n);
    for (i = 0; i < n; i++) {
      scanf("%d", &(s[i]));
    }
    scanf("%d", &k);
    //printf("k%d\n", k);

    m = (int*)malloc(sizeof(int)*(k+1));
    for (i=0;i<=k;i++) {
      m[i] = 0;
    }

    m[0] = 1;
    for (i=0;i<n;i++) {
      for (j = k - s[i]; j>=0; j--) {
        if (m[j]) {
          m[j+s[i]] = 1;
          //printf("true at i %d, j %d, si %d\n",i,j,s[i]);
        }
      }
    }
    printf("%s\n",m[k] ? "yes" : "no" );

    scanf("%d", &n);
  }
  return 0;
}
