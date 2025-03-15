
public class App {

    public static void main(String[] args) throws Exception {
        // CharFile cf = new CharFile();
        // CharFile rf = new CharFile();
        ByteFile wbf = new ByteFile();

        // // Use
        // cf.WriteCharFile("data.txt", "");
        // rf.ReadCharFile("data.txt");
        wbf.WriteByteFile();
        wbf.ReadByteFile();
    }

    public static float divide(int a, int b) {
        return a / b;
    }

    public static void CheckAge(int age) {
        if (age < 18) {
            throw new IllegalArgumentException("Brhhh");
        } else {

            System.out.println("Can use it");
        }
    }
}
