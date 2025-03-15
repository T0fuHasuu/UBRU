import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Connect {

    // Declare Host
    private static final String url = "jdbc:mariadb://localhost:3306/comsci";
    private static final String username = "root";
    private static final String password = "";

    // Hosting
    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(url, username, password);
    }
}
