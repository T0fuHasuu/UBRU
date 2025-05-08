import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class StudentDAO {

    // Retrieve Student Data
    public static ResultSet getAllStudents(Connection conn) throws SQLException {
        String sql = "SELECT * FROM students";
        Statement stmt = conn.createStatement();
        return stmt.executeQuery(sql);
    }

    // Get student by their ID
    public static ResultSet getStudentById(Connection conn, String id) throws SQLException {
        String sql = "SELECT * FROM students WHERE id = '" + id + "'";
        Statement stmt = conn.createStatement();
        return stmt.executeQuery(sql);
    }

    // Add student into the database
    public static int addStudent(Connection conn, String id, String name) throws SQLException {
        String sql = String.format("INSERT INTO students (id, name) VALUES ('%s', '%s')", id, name);
        Statement stmt = conn.createStatement();
        return stmt.executeUpdate(sql);
    }

    // Update student name
    public static int updateStudentName(Connection conn, String id, String newName) throws SQLException {
        String sql = String.format("UPDATE students SET name = '%s' WHERE id = '%s'", newName, id);
        Statement stmt = conn.createStatement();
        return stmt.executeUpdate(sql);
    }

    // Delete student name
    public static int deleteStudent(Connection conn, String id) throws SQLException {
        String sql = String.format("DELETE FROM students WHERE id = '%s'", id);
        Statement stmt = conn.createStatement();
        return stmt.executeUpdate(sql);
    }   
}


