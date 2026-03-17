package backjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class n4948 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true){
            // long num = Long.parseLong(br.readLine());
            int num = Integer.parseInt(br.readLine());
            if (num == 0) break;
            System.out.println(calc(num));

        }
    }
    private static int calc(int num) {
        int cnt = 0;
        if (num<=1) return 1;

        for(int i=num+1; i<=num*2; i++) {
            boolean prime = false;
            for(int j=2; j<=Math.sqrt(i); j++) {
                if (i%j ==0) {
                    prime = true;
                    break;
                }
            }

            if (!prime) {
                cnt ++;
            }
        }
        return cnt;
    }
}
