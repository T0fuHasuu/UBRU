
public class dog {
    String name;
    String color;
    String gender;
    int stamina;

    public dog(String name, String color, String gender, int stamina){
        this.name = name;
        this.color = color;
        this.gender = gender;
        this.stamina = stamina;
    }

    public void walk(){
        if (stamina > 0){
            System.out.println("Walking ..");
            stamina -= 1 ;
        } else {
            System.out.println("It's tired");
        }
    }

    public void run(){
        if (stamina > 1){
            System.out.println("Running . . . ");
            stamina -= 2;
        } else {
            System.out.println("Nahh No Way !!!");
        }
    }
    public void sleep(){
        System.out.println("sleeping . . . 5 Stamina Added");
        stamina = 5;
    }
    public void eat(){
        System.out.println("Eating . . . Gain 3 stamina");
        stamina = 3;
    }
    void info(){
        // System.out.print("name : " + name);
        // System.out.print("\t|\tgender : " + gender);
        // System.out.println("\t|\tcolor : " + color);

        System.err.print(name + " with the " + color + " color and " + gender + " is " );

    }

}
