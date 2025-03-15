public class Horse {
    protected String name;
    private String color;

    public Horse(String name, String color) {
        this.name = name;
        this.color = color;
    }

    public void walk() {
        System.out.printf("%s[horse] Walking\n", name);
    }

    public void run() {
        System.out.printf("%s[horse] Running\n", name);
    }
}


class Pegasus extends Horse {
    
    public Pegasus(String name, String color) {
        super(name, color);
    }
    public void fly(){
        System.out.printf("%s[Pegasus] Flying\n", name);
    }
    
}