public class pistol {
    int ammo;
    boolean burstMode = false;

    public pistol(int ammo, boolean burstMode) {
        this.ammo = ammo;
        this.burstMode = burstMode;
    }

    public void fire() {
        if (ammo > 0) {
            if (burstMode) {
                if (ammo >= 3) {
                    ammo -= 3;
                    System.out.print("Bang-Bang-Bang!!!");
                } else {
                    ammo = 0;
                    System.out.print("click*");
                }
            } else {
                ammo--;
                System.out.print("bang!!");
            }
        } else {
            System.out.print("click*");
        }
    }

    public void toggleBurstMode() {
        burstMode = !burstMode;
        System.out.println("Burst mode: " + (burstMode ? "On" : "Off"));
    }
}
