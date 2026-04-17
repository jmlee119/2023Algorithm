package backjoon;

import java.util.*;
        import java.io.*;

public class n2531 {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int[] arr = new int[N];

        for (int i=0; i<N; i++) {
            arr[i] = Integer.parseInt(bf.readLine());
        }
        int[] count = new int[d+1];
        int kind = 0;

        // 초기 세팅
        for (int i =0; i<k; i++) {
            if (count[arr[i]] == 0) kind++;
            count[arr[i]]++;
        }
        // answer : 최종 값 kind : 배열안 길이

        int answer = kind;
        if (count[c] == 0) answer++;

        for (int i = 1; i< N; i++){
            int remove = arr[i-1];
            count[remove]--;
            if (count[remove] == 0) kind--;

            int add = arr[(i+k-1) % N];
            if (count[add] == 0) kind++;
            count[add]++;

            if (count[c] == 0) {
                answer = Math.max(answer, kind+1);
            }
            else {
                answer =Math.max(answer, kind);
            }


        }
        System.out.println(answer);
    }
}
