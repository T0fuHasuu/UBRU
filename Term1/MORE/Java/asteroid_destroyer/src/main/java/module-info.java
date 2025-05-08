module com.megaton {
    requires javafx.controls;
    requires javafx.fxml;

    opens com.megaton to javafx.fxml;
    exports com.megaton;
}
