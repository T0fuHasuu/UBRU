public class main {

    public static void main(String[] args) {
        String[][] days = {
            {"Monday","MON"},
            {"Tuesday","TUE"},
            {"Wednesday","WED"},
            {"Thursday","THU"},
            {"Friday","FRI"},
            {"Saturday","SAT"},
            {"Sunday","SUN"}
        };

        for (int i = 0; i < days.length; i++){
            System.out.println("Day: " + days[i][0] + ", Abbreviation: " + days[i][1]);
        } 
    }
}