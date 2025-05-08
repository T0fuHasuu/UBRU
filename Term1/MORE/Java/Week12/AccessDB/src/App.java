// Import 
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;

public class App {

    // Declare connection
    static Connection conn;

    public static void main(String[] args) {
        try {
            // Get connection from the Connect class
            conn = Connect.getConnection();

            // Update Student name
            StudentDAO.updateStudentName(conn, "66122420109", "นายJose Marlin");
            
            // Delete Student from the database
            StudentDAO.deleteStudent(conn, "66122420126");

            // Add a new student
            int result = StudentDAO.addStudent(conn, "66122420126", "นายDAYUTH THY");
            System.out.println("Added new student: " + (result > 0 ? "Success" : "Failed"));
            

            // Retrieve all student data
            ResultSet data = StudentDAO.getAllStudents(conn);

            // Display student data
            while (data.next()) {
                System.out.println("ID: " + data.getString("id") + ", Name: " + data.getString("name"));
            }
        } catch (SQLException e) {
            System.err.println("An error occurred while accessing the database: " + e.getMessage());
        } finally {
            try {
                if (conn != null) {
                    conn.close();
                }
            } catch (SQLException e) {
                System.err.println("Error while closing the connection: " + e.getMessage());
            }
        }
    }
}
