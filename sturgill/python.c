#include <unistd.h>
#include <sys/wait.h>
#include <iostream>
using namespace std;
int main(){
  pid_t pid;
  int status, died;
     switch(pid=fork()){
     case -1: cout << "can't fork\n";
              exit(-1);
     case 0 : sleep(2); // this is the code the child runs
              exit(3); 
     default: died= wait(&status); // this is the code the parent runs 
     }
}
