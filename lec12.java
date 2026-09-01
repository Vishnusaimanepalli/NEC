import java.util.*;
public class lec12{
    public static Scanner scn = new Scanner(System.in);

    public static HashMap<Integer,Integer> input(int n){
        HashMap<Integer, Integer> map = new HashMap<>();
        for (Integer i = 0; i < n; i++) {
            map.put(i, scn.nextInt());
        }
        return map;
    }

    public static void display(HashMap<Integer, Integer> map){
        for (Map.Entry<Integer, Integer> entries : map.entrySet()) {
            System.out.println(entries.getKey() + ": " + entries.getValue());
        }
    }

    public static <K, V> void displayGen(HashMap<K, V> map) {
        for (Map.Entry<K, V> entries : map.entrySet()) {
            System.out.println(entries.getKey() + ": " + entries.getValue());
        }
    }


    public static void main(String[] args){
        // newFunc(scn.nextInt());
    }
}