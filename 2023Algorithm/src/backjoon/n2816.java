package backjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class n2816 {
    public static String[] channel;

    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());
        channel = new String[N];
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<N; i++ ){
            channel[i] = bf.readLine();
        }

        int idx = 0;
        while (!channel[idx].equals("KBS1")) {
            idx++;
            sb.append('1');
        }
        while (idx > 0) {
            swap(idx, idx-1);
            idx--;
            sb.append('4');
        }

        while (!channel[idx].equals("KBS2")) {
            idx++;
            sb.append('1');
        }
        while (idx > 1) {
            idx--;
            sb.append('4');
        }

        System.out.println(sb);
    }
    public static void swap(int a, int b){
        String temp = channel[a];
        channel[a] = channel[b];
        channel[b] = temp;
    }
}
