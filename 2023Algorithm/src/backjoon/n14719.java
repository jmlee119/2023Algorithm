package backjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class n14719 {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int w = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());
        int[] arr = new int[h];
        st = new StringTokenizer(bf.readLine());
        for (int i=0; i<h; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int answer = 0;
        for (int i=1; i<h-1; i++) {
            int leftMax =0;
            int rightMax = 0;
            for (int j=0; j<i; j++) {
                leftMax = Math.max(leftMax, arr[j]);
            }
            for (int j=i+1; j<h; j++) {
                rightMax = Math.max(rightMax, arr[j]);
            }
            int water = Math.min(leftMax, rightMax) - arr[i];
            if (water > 0) {
                answer += water;
            }
        }
        System.out.println(answer);

    }
}
