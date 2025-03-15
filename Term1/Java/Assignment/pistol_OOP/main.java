
public class main {

    public static void main(String[] args) {
        pistol myPistol = new pistol(21, false);

        while (myPistol.ammo > 0) {
            System.out.print("Ammo : " + myPistol.ammo + "\t");
            myPistol.fire();
            System.out.println("\tAmmo : " + myPistol.ammo + "\t");
            myPistol.toggleBurstMode();
        }
        System.out.println("click**");
    }
}
