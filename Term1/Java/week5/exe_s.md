# 1-10 addition : 
int c = 0,i;
for (i = 1; i<=10; i++){
    c += i;
    System.out.println(c);
}

# Name input Loop :
String name; 
char stop;
boolean end = true;

do {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter Your Name ");
    name = sc.nextLine();
    System.out.printf("Your Name i%s\n\n", name);
    System.out.print("Press [N/n] tEnd!!! : ");
    stop = sc.next().charAt(0);
    if ( stop == 'N' || stop == 'n'){
        end = false;
    }
} while ( end )


