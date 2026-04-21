package backjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class n2493 {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int[] arr = new int[N];

        for(int i =0; i<N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Stack<Integer> stack = new Stack<>();

        StringBuilder sb = new StringBuilder();
        for(int i =0; i<N; i++) {
            while (!stack.isEmpty() && arr[stack.peek()] < arr[i]) {
                stack.pop();
            }
            if (stack.isEmpty()) {
                sb.append(0).append(" ");
            }
            else {
                sb.append(stack.peek()+1).append(" ");
            }
            stack.push(i);
        }
        System.out.println(sb);

    }
}
