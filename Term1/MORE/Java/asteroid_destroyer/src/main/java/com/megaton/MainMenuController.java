package com.megaton;

import java.io.IOException;

public class MainMenuController {

    public void goFirst() throws IOException {
        App.setRoot("SayHi");
    }

    public void goSecondary() throws IOException{
        App.setRoot("secondary");
    }
    
    public void goExit(){
        System.out.println("Exit");
    }
}
