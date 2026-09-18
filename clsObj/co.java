public class co {

    public static class phone {
        String brand;
        String model;
        String color;
        int ram;
        int rom;
        int btry;

        {
            System.out.println(this);
        }

        // -----------------------------------Example of constructor
        // overloading---------------------
        phone(String brand, String model, String color, int ram, int rom, int btry) { // parameterized constructor it
                                                                                      // helps to create objects
            this.brand = brand;
            this.model = model; // this refers to current object; left model is the variable of the class which
                                // we have created upside, and right model is the parameter which catching the
                                // real value from main();
            this.color = color;
            this.ram = ram;
            this.rom = rom;
            btry = btry;// here both btry refer as same which is parameter of phone constructor. hover
                        // on btry and check it shows - btry has no effect; i.e. 10 = 10; thatswhy we
                        // use this keyword;
        }

        phone(int btry, String model, String color, int ram, int rom, String brand) {
            this.btry = btry;
            this.model = model;
            this.color = color;
            this.ram = ram;
            this.rom = rom;
            this.brand = brand;
        }

        phone(String brand, String model, String color, int rom, int btry) {
            this.btry = btry;
            this.model = model;
            this.color = color;
            this.rom = rom;
            this.brand = brand;
        }

        // ----------------------------------------------------------------------------------------------
        phone() {
        } // non parameterized cunstructor

        // for printing the object, create a method or function :
        public String displayObj() { // dont make display function as static function, because the class is already
                                     // been static and moreover the function inside the class can not be a static
                                     // function.
            StringBuilder sb = new StringBuilder();
            sb.append("inside class display() \n");
            sb.append("Brand: " + this.brand + "\n");
            sb.append("Model: " + this.model + "\n");
            sb.append("Color: " + this.color + "\n");
            sb.append("RAM: " + this.ram + "GB\n");
            sb.append("ROM: " + this.rom + "GB\n");
            sb.append("Battery: " + this.btry + "mAh\n");
            sb.append("\n");
            return sb.toString();
        }

        // but instead of display function we need to use toString() afteroverriding for
        // a good practice.
        @Override
        public String toString() { // here if by mistake spelling of toString() method is incorrect then an error will be thrown.
            StringBuilder sb = new StringBuilder();
            sb.append("With toString() \n"); // with toString() class phone become bit smarter now we do not need to print the object seperately
            sb.append("Brand: " + this.brand + "\n");
            sb.append("Model: " + this.model + "\n");
            sb.append("Color: " + this.color + "\n");
            sb.append("RAM: " + this.ram + "GB\n");
            sb.append("ROM: " + this.rom + "GB\n");
            sb.append("Battery: " + this.btry + "mAh\n");
            sb.append("\n");
            return sb.toString();
        }

    }

    // if want to print or display outside the class then :
    public static String displayOut(phone ph) {
        StringBuilder sb = new StringBuilder();
        sb.append("outside class display() \n");
        sb.append("Brand: " + ph.brand + "\n");
        sb.append("Model: " + ph.model + "\n");
        sb.append("Color: " + ph.color + "\n");
        sb.append("RAM: " + ph.ram + "\n");
        sb.append("ROM: " + ph.rom + "\n");
        sb.append("Battery: " + ph.btry + "\n\n");
        return sb.toString();
    }

    public static void main(String[] args) {
        phone p1 = new phone("Google Pixel", "10 pro xl", "gray", 256, 6000);
        // p1.brand = "Google pixel"; // p1 is an obj and same as this keyword.
        // p1.ram = 12;
        System.out.println(p1.displayObj());
        System.out.println(displayOut(p1));
        // System.out.println(p1);
    }
}
