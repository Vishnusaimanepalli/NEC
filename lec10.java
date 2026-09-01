import java.util.*;

public class lec10 {
    public static Scanner scn = new Scanner(System.in);

    public static void newfunc() {
        String str = "";
        long start = System.currentTimeMillis();
        for (int i = 0; i < (int) 1e5; i++) {
            str += i;
        }
        long end = System.currentTimeMillis();
        System.out.println(end - start);
    }

    public static void stringBuilderTimeMeasure() {
        StringBuilder sb = new StringBuilder();

        long start = System.currentTimeMillis();
        for (int i = 0; i < (int) 1e6; i++) {
            sb.append(i);
        }
        long end = System.currentTimeMillis();
        System.out.println(end - start);
    }

    public static void stringBuilderOps() {
        StringBuilder sb = new StringBuilder();
        sb.append('a');
        sb.append('b').append("cdefgh ijk"); // O(m) m is the length of the existing string.
        
        System.out.println(sb);
        System.out.println(sb.toString()); // O(n) of .toString();

        sb.setCharAt(4, '7'); // O(1).
        System.out.println(sb.toString());

        sb.deleteCharAt(4); // O(n) if it is any character in the string except last character. complexity of last character is -> O(1);
        System.out.println(sb.toString());

    }

    public int scoreOfStringLeetCode3110(String s) {
        StringBuilder sb = new StringBuilder(s);
        int score = 0;

        for (int i = 0; i < sb.length() - 1; i++) {
            int diff = Math.abs(sb.charAt(i) - sb.charAt(i + 1));
            score += diff;
        }

        return score;
    }


    public boolean hasAdjacentDigitDifferenceLeetCode3931(int n) {
        StringBuilder sb = new StringBuilder(String.valueOf(Math.abs(n)));

        for (int i = 0; i < sb.length() - 1; i++) {
            int digit1 = sb.charAt(i) - '0';
            int digit2 = sb.charAt(i + 1) - '0';

            if (Math.abs(digit1 - digit2) != 1) {
                return false;
            }
        }

        return true;
    }

public static String funnyStringHackerRank(String s) {
    StringBuilder sb = new StringBuilder(s);
    StringBuilder rev = new StringBuilder(s).reverse();

    for (int i = 0; i < sb.length() - 1; i++) {
        int forward = Math.abs(sb.charAt(i) - sb.charAt(i + 1));
        int reverse = Math.abs(rev.charAt(i) - rev.charAt(i + 1));

        if (forward != reverse) {
            return "Not Funny";
        }
    }

    return "Funny";
}

public static String superReducedStringHackerRank(String s) {
    StringBuilder sb = new StringBuilder();

    for (int i = 0; i < s.length(); i++) {
        char ch = s.charAt(i);

        if (sb.length() > 0 && sb.charAt(sb.length() - 1) == ch) {
            sb.deleteCharAt(sb.length() - 1);
        } else {
            sb.append(ch);
        }
    }

    return sb.length() == 0 ? "Empty String" : sb.toString();
}

    public static void main(String[] args) {
        stringBuilderOps();
    }
}