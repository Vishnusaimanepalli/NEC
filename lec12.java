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

    public static ArrayList<Integer> arrToMap(int n) {
        ArrayList<Integer> arr = new ArrayList<>();
        for (Integer i = 0; i < n; i++) {
            arr.add(scn.nextInt());
        }
        return arr;
    }

    public static HashMap<Integer, Integer> countFreq(ArrayList<Integer> arr) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (Integer i = 0; i < arr.size(); i++) {
            map.put(arr.get(i), map.getOrDefault(arr.get(i), 0) + 1);
        }
        return map;
    }

    public static HashMap<Character, Integer> charFreq(String str) {
        HashMap<Character, Integer> map = new HashMap<>();
        for (Integer i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }
        return map;
    }
    
    public static void nonRepeating387(ArrayList<Integer> arrLst) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (Integer i = 0; i < arrLst.size(); i++) {
            map.put(arrLst.get(i), map.getOrDefault(arrLst.get(i), 0) + 1);
        }
        for (Map.Entry<Integer, Integer> entries : map.entrySet()) {
            // System.out.println(entries.getKey() + ": " + entries.getValue());
            if (entries.getValue() > 1) {
                continue;
            } else {
                System.out.println(entries.getKey());
                break;
            }
        }
    }

    public static int findDuplicate442(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int duplicateElem = -1;
        for (Integer elem : nums) {
            map.put(elem, map.getOrDefault(elem, 0) + 1);
        }
        for (Integer i = 0; i < nums.length; i++) {
            if (map.get(nums[i]) > 1) {
                duplicateElem = nums[i];
            }
        }
        return duplicateElem;
    }

    
    
    public static void main(String[] args){
        // displayGen(countFreq(arrToMap(scn.nextInt())));
        displayGen(charFreq("abaacbacc cabc abc"));
    }
}