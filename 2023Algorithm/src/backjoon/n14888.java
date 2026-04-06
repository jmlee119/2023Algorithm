package backjoon;

import java.util.*;
import java.io.*;

public class n14888 {
    public static int MAX  = Integer.MIN_VALUE;
    public static int MIN  = Integer.MAX_VALUE;
    public static int N;
    public static int[] num_arr;
    public static int[] operator = new int[4];

    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());
        num_arr = new int[N];
        StringTokenizer st = new StringTokenizer(bf.readLine());
        for (int i = 0; i<N; i++) {
            num_arr[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(bf.readLine());
        for (int i=0; i<4; i++) {
            operator[i] = Integer.parseInt(st.nextToken());
        }

        dfs(num_arr[0], 1);
        System.out.println(MAX);
        System.out.println(MIN);
    }


    private static void dfs(int num, int idx) {
        if (idx == N) {
            MAX = Math.max(MAX, num);
            MIN = Math.min(MIN, num);
            return;
        }

        for (int i = 0; i < 4; i++) {
            if (operator[i] > 0) {
                operator[i]--;
                if (i == 0) dfs(num + num_arr[idx], idx+1);
                if (i == 1) dfs(num - num_arr[idx], idx+1);
                if (i == 2) dfs(num * num_arr[idx], idx+1);
                if (i == 3) dfs(num / num_arr[idx], idx+1);
                operator[i]++;
            }

        }
    }
}
