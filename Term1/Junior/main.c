#include <stdio.h>
int main(){
int numbers[3];

    for (int i=0; i<3; i++){
        printf("Enter number %d:",i+1);
        scanf("%d" ,&numbers[i]);
    }
    for (int i=0; i<3; i++){
        printf("Numbers is %d: %d\n",i+1,numbers[i]);
    }
    return 0;
}

