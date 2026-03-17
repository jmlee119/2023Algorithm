package backjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class n4134{
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int TestCase = Integer.parseInt(br.readLine());
        for (int i=0; i<TestCase; i++) {
            long num = Long.parseLong(br.readLine());
            System.out.println(calc(num));
        }
    }
    private static long calc(long num) {
        if (num <=2) {
            return 2;
        }

        long ans= 0;
        for(long i=num; ; i++){
            boolean prime = false;
            for (long j=2; j<=Math.sqrt(i); j++){
                if(i%j ==0) {
                    prime = true;
                    break;
                }
            }
            if (!prime) {
                return i;
            }
        }
    }
}
