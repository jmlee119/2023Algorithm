package backjoon;

import java.util.*;
import java.io.*;

public class n1446 {
     static List<Range> list = new ArrayList<>();
     public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        int D = Integer.parseInt(st.nextToken());


        for (int i=0; i<N; i++) {
            st = new StringTokenizer(bf.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int distinct = Integer.parseInt(st.nextToken());
            list.add(new Range(start, end, distinct));
        }
        int[] dp = new int[D+1];

        dp[0] = 0;
        dp[1] = 1;
        for (int i=2; i<=D; i++) {
            dp[i] = dp[i-1] + 1;
            for (Range r : list) {
                if (i == r.end) {
                    dp[i] = Math.min(dp[i], dp[r.start] + r.distinct);
                }
            }
        }
         //System.out.println(Arrays.toString(dp));
         System.out.println(dp[D]);
    }

    static class Range {
        int start;
        int end;
        int distinct;

        public Range(int start, int end, int distinct) {
            this.start = start;
            this.end = end;
            this.distinct = distinct;
        }
    }
}
