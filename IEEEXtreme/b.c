#include<stdlib.h>
#include<unistd.h>
#include<stdio.h>
#include<math.h>
#include<string.h>
int main() {
int bloom[26] = {0};
char diff = 0x20;
char c = '\0';
char n;
char s[1500];
int i;
while('\n' != (c = getc(stdin))) {
  n = (c|diff)-'a';
  if (n >= 0 && n < 26) {
    bloom[(int)(n)] = 1;
  }
}
int sum = 0;
while (1 == scanf("%s",s)) {
  int counted = 1;
  for (i=0;'\0'!=s[i];i++) {
    n = (s[i]|diff)-'a';
    if (n >= 0 && n < 26) {
      if (!bloom[(int)(n)]) {
        counted = 0;
        break;
      }
    }
  }
  sum += counted;
}
printf("%d\n",sum);
return(0);
}
