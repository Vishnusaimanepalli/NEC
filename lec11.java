import java.util.Scanner;
import java.util.ArrayList;

public class lec11 {

    public static Scanner scn = new Scanner(System.in);

    public static ArrayList<Integer> arrayListInput(int n) {
        ArrayList<Integer> arrLst = new ArrayList<>();

        for (Integer i = 0; i < n; i++) {
            arrLst.add(scn.nextInt());
        }

        return arrLst;
    }

    public static void arrayLstOps() {
        ArrayList<Integer> arrLst = new ArrayList<>();
        // set or adding elements in the arrayList
        arrLst.add(10);
        arrLst.add(scn.nextInt());
        arrLst.add(scn.nextInt());
        arrLst.add(40);
        System.out.println(arrLst);

        // to know the length of arrayList, default size is 15 of arrayList and it will
        // vary
        arrLst.size();

        // get or render on particular element
        arrLst.get(2); // index we have to provide in the parenthesis to get an element.

        // looping on arrayLst
        for (Integer i = 0; i < arrLst.size(); i++) {
            System.out.println(arrLst.get(i));
        }
        // or
        for (Integer elem : arrLst) {
            System.out.print(elem + "\t");
        }

        // to remove or delete element from array list
        arrLst.remove(2);
    }

    public static void swap(ArrayList<Integer> arrLst, int i, int j) {
        int temp = arrLst.get(i);
        arrLst.set(i, arrLst.get(j));
        arrLst.set(j, temp);
    }

    public static Boolean isPrime(int n) {
        if (n < 2)
            return false;

        for (int i = 2; i <= n / 2; i++) {
            if (n % i == 0)
                return false;
        }
        return true;
    }

    public static void removePrimeNumbers(int n) {
        ArrayList<Integer> arrLst = arrayListInput(n);
        ArrayList<Integer> arrLst1 = new ArrayList<>();
        int i = arrLst.size() - 1;
        while (i >= 0) {
            if (isPrime(arrLst.get(i))) {
                swap(arrLst, i, arrLst.size() - 1);
                int removedElem = arrLst.remove(arrLst.size() - 1);
                arrLst1.add(removedElem);
            }
            i--;
        }
        System.out.print(arrLst);
        System.out.print(arrLst1);
        System.out.println("\nFncn DONE");

    }

    public static void removePrime1(ArrayList<Integer> arrLst) {
        ArrayList<Integer> ans = new ArrayList<>();
        for (int elem : arrLst) {
            if (!isPrime(elem)) {
                ans.add(elem);
            }
        }
        // arrLst.clear();
        while (arrLst.size() - 1 != 0) {
            arrLst.remove(arrLst.size() - 1);
        }
        for (int elem : ans) {
            arrLst.add(elem);
        }
        System.out.print(arrLst);
    }

    public static void main(String[] args) {

    }
}
