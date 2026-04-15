package backjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class n2304 {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());
        int max = Integer.MIN_VALUE;
        int main = -1;
        int[][] factory = new int[N][2];
        int sum = 0;

        for (int i =0; i <N; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            factory[i][0] = Integer.parseInt(st.nextToken());
            factory[i][1] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(factory, (a,b) -> a[0]-b[0]);


        for (int i =0; i <N; i++) {
            if (max < factory[i][1]) {
                max = factory[i][1];
                main = i;
            }
        }

        int leftIndex = factory[0][0];
        int leftHeight = factory[0][1];
        //왼쪽부터 높이가 가장 높은 max 까지
        for(int i=1; i<=main; i++) {
            if (leftHeight <= factory[i][1]) {
                sum = sum + (factory[i][0] - leftIndex) * leftHeight;
                leftIndex = factory[i][0];
                leftHeight = factory[i][1];
            }
        }

        int rightIndex = factory[N-1][0];
        int rightHeight = factory[N-1][1];
        for (int j = N-1; j>=main; j--) {
            if (rightHeight <= factory[j][1]) {
                sum = sum + (rightIndex - factory[j][0]) * rightHeight;
                rightIndex = factory[j][0];
                rightHeight = factory[j][1];
            }
        }
        sum += max;
        System.out.println(sum);
        //System.out.println(Arrays.deepToString(factory));
    }
}
