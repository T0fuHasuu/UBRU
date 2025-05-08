#include <stdio.h>
#include <stdbool.h>

void displayFunnyCat() {
    printf("      /\\_/\\  \n");
    printf("     ( o.o ) \n");
    printf("      > ^ <  \n");
    printf("     Meow!  \n");
}

void HelloWorld(){
    printf("Hello World");
}

void PNewLine(){
    printf("Name : DAYUTH\nAge : 20");
}

void Variable(){
    char name[] = "Dayuth";
    int age = 20;
    char Lastname = 'T';
    float height = 1.75;
    bool single = true;

    printf("Name : %s\n"
    "Age : %d\n years old"
    "LastName : %c\n."
    "Height : %.2f\n m."
    "Single : %s",
    name,age,Lastname,height, single ? "Yes" : "No");
}

int Plus(){
    int num1;
    int num2;
    int overall;

    overall = num1 + num2 ;
    printf("%d", overall);
}



void CheckLegalAge(){
    int age = 0;
    if (age >= 18){
        printf("You are legal");
    }  
    else if (age == 0) {
        printf("._.");
    }    
    else {
        printf("Nahh Not yet");
    }
}

void SwitchMe(){
    int input = 2;

    switch (input)
    {
    case 1:
        printf("Number 1");
        break;

    case 2:
        printf("Number 2");
        break;
    
    default:
        printf("Nothing");
        break;
    }
}

void forLoop() {
    for (int i = 0; i<=2;i++){
        printf("*");
    }
}

void whileLoop(){
    int i = 10;
    while ( i > 1 ){
        printf("%d\n", i);
        i--;
    }  
}

void DoWhileLoop(){
    int i = 0;
    do {
        printf("hello %d\n", i);
        i++;
    } while (i < 5);
}

int main() {
    return 0;
}