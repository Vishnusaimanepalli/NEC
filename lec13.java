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

    public static int firstIdx(int[] arr, int idx, int data) {

    }

    public static int lastIdx(int[] arr, int idx, int data) {
        
    }

    public static int[] firstAndLastIdx(int[] arr, int idx, int data) {
        
    }

    public static int countOfIdx(int[] arr, int idx, int data) {
        
    }

    public static int[] allIdx(int[] arr, int idx, int data) {  // you can take 1 more formal parameter but not an array.
        
    }
    public static void main(String[] args) {
        printArr(inputArr(scn.nextInt(), scn.nextInt()), 0);
    }
}