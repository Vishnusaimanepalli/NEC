import java.util.*;

public class lec9 {
    public static Scanner scn = new Scanner(System.in);

    public static void stringCompression(String str) {
        int n = str.length(), i = 1;
        String ans = str.charAt(0) + "";
        while (i < n) {
            while (i < n && ans.charAt(ans.length() - 1) == str.charAt(i)) {
                i++;
            }
            if (i < n) {
                ans += str.charAt(i);
                i++;
            }
        }
        System.out.print(ans);
    }

    public static void stringCompressionCounts(String str) {
        int n = str.length(), i = 1, count = 0;
        String ans = str.charAt(0) + "";
        while (i < n) {
            count = 1;
            while (i < n && ans.charAt(ans.length() - 1) == str.charAt(i)) {
                i++;
                count++;
            }

            if (count >= 1) {
                ans = ans + ":" + count + "\n";
            }
            if (i < n) {
                ans += str.charAt(i);
            }
            i++;
        }
        System.out.print(ans);
    }

    public static void countOfHi(String str) {
        int len = str.length(), i = 0, count = 0;
        str = str.toLowerCase();

        while (i < len - 1) {
            if (str.charAt(i) == 'h' && str.charAt(i + 1) == 'i') {
                count++;
                i += 2;
            } else {
                i++;
            }
        }
        System.out.println(count);
    }

    public static int countOfHiInHit(String str) {
        int len = str.length(), i = 0, count = 0;

        while (i < len) {
            if (str.charAt(i) == 'i' && str.charAt(i - 1) == 'h') {
                if (i + 1 < len && str.charAt(i + 1) == 't') {
                    i += 2;
                } else {
                    i++;
                    count++;
                }
            } else {
                i++;
            }
        }
        return count;
    }

    public static void removeHi(String str) {
        String str1 = "";
        int len = str.length(), i = 0;

        while (i < len) {
            if (str.charAt(i) == 'h' && str.charAt(i + 1) == 'i') {
                if (i + 1 < len && str.charAt(i + 2) != 't') {
                    i += 2;
                } else {
                    str1 += str.charAt(i);
                    i++;
                }
            } else {
                str1 += str.charAt(i);
                i++;
            }
        }
        System.out.println(str1);
    }

    public static void removeHit(String str) {
        String str1 = "";
        int len = str.length(), i = 0;

        while (i < len) {
            if (i + 2 < len && str.charAt(i) == 'h' && str.charAt(i + 1) == 'i' && str.charAt(i + 2) == 't') {
                i += 3;
            } else {
                str1 += str.charAt(i);
                i++;
            }
        }
        System.out.println(str1);
    }

    public static void main(String[] args) {
        stringCompressionCounts(scn.nextLine());
    }
}