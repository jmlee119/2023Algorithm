package backjoon;
import java.util.*;
import java.io.*;
public class n20922 {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(bf.readLine());

        int[] arr = new int[N];
        int[] cnt = new int[100001];
        for (int i = 0; i<N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int answer = 0;
        int start= 0, end = 0;
        while (start <= end) {
            if (end < N && cnt[arr[end]] < K) {
                cnt[arr[end]]++;
                end ++;
            }
            else if(cnt[arr[end]] == K) {
                cnt[arr[start]]--;
                start++;
            }
            answer = Math.max(answer, end-start);

            if(end == N) break;
        }
        System.out.println(answer);
    }
}
