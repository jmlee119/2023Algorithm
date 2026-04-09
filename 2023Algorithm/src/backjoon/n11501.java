package backjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class n11501 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int testCase = Integer.parseInt(br.readLine());
        for (int t=0; t<testCase; t++) {
            int N = Integer.parseInt(br.readLine());
            int[] arr = new int[N];

            StringTokenizer st = new StringTokenizer(br.readLine());

            for (int i=0; i<N; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }
            int MAX = arr[N-1];
            long answer = 0;

            for (int j = N-2; j >= 0; j--) {
                if (MAX > arr[j]) {
                    answer += MAX - arr[j];
                }
                else {
                    MAX = arr[j];
                }
            }
            System.out.println(answer);
        }

    }
}
