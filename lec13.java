import java.util.*;
public class lec13{
    public static Scanner scn = new Scanner(System.in);

    public static int[] inputArr(int n, int val){
        if (n == 0) {
            return new int[val];
        }

        int[] arr = inputArr(n-1, val);
        arr[n-1] = scn.nextInt();

        return arr;
    }

    public static void printArr(int[] arr, int idx){
        if (idx == arr.length) {
            return;
        }
        System.out.print(arr[idx] + "\t");
        printArr(arr, idx + 1);
    }

    public static int maximum(int[] arr, int idx){

    }

    public static int minimum(int[] arr, int idx){

    }

    public static void main(String[] args){
        printArr(inputArr(scn.nextInt(), scn.nextInt()), 0);
    }
}