
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class CharFile {

    public void WriteCharFile(String Filename, String data) throws IOException {
        FileWriter fw = new FileWriter(Filename, true);
        BufferedWriter bw = new BufferedWriter(fw); 
        bw.write("\n" + data);
        bw.close();
    }

    public void ReadCharFile(String Filename) throws IOException {
        FileReader fr = new FileReader(Filename);
        BufferedReader br = new BufferedReader(fr);

        String line;

        while ((line = br.readLine()) != null) {
            System.out.println(line);
        }
        br.close();

    }
}
