package backjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class n17615 {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());
        String input_String = bf.readLine();
        char[] ball_list = new char[N];
        int red_cnt = 0;
        int blue_cnt = 0;
        for(int i=0; i<N; i++) {
            ball_list[i] = input_String.charAt(i);
            if (ball_list[i] == 'R') {
                red_cnt +=1;
            }if (ball_list[i] == 'B') {
                blue_cnt +=1;
            }
        }

        int answer = Integer.MAX_VALUE;

        int left_Red = 0;
        int left_Blue = 0;
        int right_Red = 0;
        int right_Blue = 0;

        // 1. Red 를 왼쪽에 보내는 경우
        for (int i=0; i<N; i++) {
            if (ball_list[i] == 'R') {
                left_Red +=1;
            }
            else{
                break;
            }
        }
        answer = Math.min(answer , red_cnt - left_Red);

        // 2. Blue 를 왼쪽에 보내는 경우
        for (int i=0; i<N; i++) {
            if (ball_list[i] == 'B') {
                left_Blue +=1;
            }
            else{
                break;
            }
        }
        answer = Math.min(answer , blue_cnt - left_Blue);

        // 3. Red 를 오른쪽에 보내는 경우
        for (int i=N-1; i>0; i--) {
            if (ball_list[i] == 'R') {
                right_Red +=1;
            }
            else{
                break;
            }
        }
        answer = Math.min(answer , red_cnt - right_Red);

        // 4. Blue 를 오른쪽에 보내는 경우
        for (int i=N-1; i>0; i--) {
            if (ball_list[i] == 'B') {
                right_Blue +=1;
            }
            else{
                break;
            }
        }
        answer = Math.min(answer , blue_cnt - right_Blue);

        System.out.println(answer);
    }
}
