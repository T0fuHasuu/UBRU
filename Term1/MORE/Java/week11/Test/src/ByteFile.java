import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class ByteFile {
    public void WriteByteFile () throws IOException   {
        FileOutputStream myFile = new FileOutputStream("data2.txt");
        DataOutputStream fos = new DataOutputStream(myFile);
        
        // Declare Variables
        String name = "Chamber";
        int age = 24;
        float height = 180.4f;

        fos.writeUTF(name);
        fos.writeInt(age);
        fos.writeFloat(height);
        fos.close();
    }
    public void ReadByteFile () throws IOException   {
        FileInputStream myFile = new FileInputStream("data2.txt");
        DataInputStream fos = new DataInputStream(myFile);
        
        String name = fos.readUTF();
        int age = fos.readInt();
        float height = fos.readFloat();
        System.out.printf("Name : %s\nAge : %d Years Old\nHeight : %.2f Cm",name,age,height);
        fos.close();
    }
}
