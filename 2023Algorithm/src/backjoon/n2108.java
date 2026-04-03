package backjoon;

import java.io.*;
import java.util.*;


public class n2108 {
    public static void main(String[] args) throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());
        int[] arr = new int[N];
        for (int i =0; i<N; i++) {
            arr[i] = Integer.parseInt(bf.readLine());
        }

        Arrays.sort(arr);

        System.out.println(Avg(arr, N));
        System.out.println(Middle(arr,N));
        System.out.println(Bin(arr, N));
        System.out.println(Range(arr));
    }

    private static int Avg(int[] arr, int N) {
        double sum =0;

        for (int n : arr) {
            sum += n;
        }
        return (int) Math.round(sum / N);
    }

    private static int Middle(int[] arr, int N) {
        return arr[N/2];
    }

    private static int Bin(int[] arr, int N) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int key : arr) {
            if (map.containsKey(key)) {
                map.put(key, map.get(key) + 1);
            } else {
                map.put(key, 1);
            }
        }
        int max = -4001;
        for (int num : map.values()) {
            if (num > max) {
                max = num;
            }
        }
        List<Integer> list = new ArrayList<>();
        for (int key : map.keySet()){
            if (map.get(key) == max) {
                list.add(key);
            }
        }
        Collections.sort(list);
        if (list.size() == 1) {
            return list.get(0);
        }
        else{
            return list.get(1);
        }

    }


    private static int Range(int[] arr) {
        if (arr.length == 1) return 0;
        int max_value = arr[arr.length-1];
        int min_value = arr[0];
        if (max_value >= 0 && min_value >= 0){
            return max_value - min_value;
        }
        else if (max_value >=0 && min_value <= 0) {
            return max_value + Math.abs(min_value);
        }
        else {
            return Math.abs(min_value) + max_value;
        }
    }
}
