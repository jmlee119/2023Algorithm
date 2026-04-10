package backjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class n20310 {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String[] str = bf.readLine().split("");
        int zero_cnt = 0;
        int one_cnt = 0;
        for (int i =0; i<str.length; i++) {
            if (str[i].equals("0")) {
                zero_cnt += 1;
            }
            else if (str[i].equals("1")) {
                one_cnt += 1;
            }
        }
        zero_cnt = zero_cnt/2;
        one_cnt = one_cnt/2;

        StringBuilder sb = new StringBuilder();

        for (int i=0; i<str.length; i++) {
            if (str[i].equals("1")) {
                str[i] = "X";
                one_cnt --;
            }
            if (one_cnt == 0) {
                break;
            }
        }
        for (int i=str.length-1; i>=0; i--) {
            if (str[i].equals("0")) {
                str[i] = "X";
                zero_cnt --;
            }
            if (zero_cnt == 0) {
                break;
            }
        }
        for(String c : str) {
            if (!c.equals("X")) {
                sb.append(c);
            }
        }
        System.out.println(sb);
    }
}
