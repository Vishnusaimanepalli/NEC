import java.util.*;

public class pract {
    public static Scanner scn = new Scanner(System.in);

    public static void conditionals(int marks) {
        if (marks < 0 || marks >= 100) {
            System.out.println("Invalid input");
        } else if (marks > 90) {
            System.out.println("Grade: A");
        } else if (marks >= 80) {
            System.out.println("Grade: B");
        }

        else if (marks >= 60) {
            System.out.println("Grade: C");
        }

        else if (marks >= 30) {
            System.out.println("Grade: D");
        }

        else if (marks < 30) {
            System.out.println("Grade: E");
        }
    }

    public static void looping(int n) {
        // for(initialization; evaluation; increment) {
        // execution;
        // }
        for (int i = 0; i < n; i++) {
            System.out.println(i);
        }
    }

    public static void findAllEvens(int n) {
        for (int i = 0; i <= n; i++) {
            if(i % 2 == 0) {
                System.out.println(i);
            }
        }
    }

    public static void sqPatt(int n) { // n = 5
        int nst = n;
        for (int row = 1; row <= n; row++) {
            for (int cst = 1; cst <= nst; cst++) {
                System.out.print("*" + "\t");
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {
        // newFunc(scn.nextInt());
        sqPatt(scn.nextInt());

    }
}