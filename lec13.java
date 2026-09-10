import java.util.*;

public class lec13 {
    public static Scanner scn = new Scanner(System.in);

    public static int[] inputArr(int n, int val) {
        if (n == 0) {
            return new int[val];
        }

        int[] arr = inputArr(n - 1, val);
        arr[n - 1] = scn.nextInt();

        return arr;
    }

    public static void printArr(int[] arr, int idx) {
        if (idx == arr.length) {
            return;
        }
        System.out.print(arr[idx] + "\t");
        printArr(arr, idx + 1);
    }

    public static int maximum(int[] arr, int idx) {
        if (idx == arr.length) {
            return -(int) 1e9;
        }

        int max = maximum(arr, idx + 1);
        return Math.max(max, arr[idx]);
    }

    public static int minimum(int[] arr, int idx) {
        if (idx == arr.length) {
            return (int) 1e9;
        }

        int min = minimum(arr, idx + 1);
        return Math.min(min, arr[idx]);
    }

    public static boolean find(int[] arr, int idx, int data) {
        if (idx == arr.length) {
            return false;
        }

        if (arr[idx] == data) {
            return true;
        }
        return find(arr, idx + 1, data);
    }

    // arr = [ 1, 1, 2, 4, 6, 2, 7, 7, 0, 6, 2, 5, 3, 2, 5, 2, 2, 2]; // 2

    public static int firstIdx(int[] arr, int i, int data) {
        if (i == arr.length) {
            return -1;
        }

        if (arr[i] == data) {
            return i;
        }

        return firstIdx(arr, i + 1, data);
    }

    public static int lastIdx(int[] arr, int i, int data) {
        if (i == arr.length) {
            return -1;
        }

        int recAns = lastIdx(arr, i + 1, data);

        if (recAns != -1) {
            return i;
        }

        return (arr[i] == data)? i : -1;
    }

    public static int countOfElem(int[] arr, int i, int data) {
        if (i == arr.length) {
            return -1;
        }
        int count = countOfElem(arr, i + 1, data);
        if (arr[i] == data) {
            count++;
        }
        return count;
    }

    public static int[] allIdx(int[] arr, int i, int data, int count) {
        if (i == arr.length) {
            return new int[count];
        }

        if (arr[i] == data) {
            count++;
        }

        int[] ans = allIdx(arr, i + 1, data, count);

        if (arr[i] == data) {
            ans[count - 1] = i;
        }

        return ans;
    }

    public static boolean firstAndLastIdx(int[] arr, int i, int data, int[] ans) {
        if (i == arr.length) return false;
        if (arr[i] == data) ans[0] = i;
        boolean res = firstAndLastIdx(arr, i + 1, data, ans);
        if (res) {
            return true;
        }
        if(arr[i] == data) {
            ans[1] = i;
            return true;
        }
        return false;
    }

    public static ArrayList<String> subSeq(String str) {

    }

    // Get KPC number against characters.
    // "0" -> ".;"
    // "1" -> "abc" 
    // "2" -> "def" 
    // "3" -> "ghi" 
    // "4" -> "jkl" 
    // "5" -> "mno" 
    // "6" -> "pqrs" 
    // "7" -> "tu" 
    // "8" -> "vwx"
    // "9" -> "yz"
    public static ArrayList<String> getKPC(String str) {

    }

    public static void main(String[] args) {
        printArr(inputArr(scn.nextInt(), scn.nextInt()), 0);
    }
}