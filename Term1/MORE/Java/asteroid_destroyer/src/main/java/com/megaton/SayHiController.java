package com.megaton;

import java.io.IOException;

import javafx.fxml.FXML;
import javafx.scene.control.TextField;

public class SayHiController {
    
    @FXML
    private TextField txtName;


    public void goMainMenu() throws IOException{
        App.setRoot("MainMenu");
    }


    public void SayHi() throws IOException{
        System.out.println("Hi " + txtName.getText());
    }
}
