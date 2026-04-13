package backjoon;

import java.util.*;
import java.io.*;

public class n1406 {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String input = bf.readLine();
        Stack<Character> leftStack = new Stack<>();
        Stack<Character> rightStack = new Stack<>();

        int M = Integer.parseInt(bf.readLine());
        for (int i=0; i<input.length(); i++) {
            leftStack.add(input.charAt(i));
        }
        int index = leftStack.size();

        for(int i=0; i<M; i++) {
            String command = bf.readLine();
            char com = command.charAt(0);

            switch (com){
                case 'L':
                    if (!leftStack.isEmpty()) {
                        rightStack.push(leftStack.pop());
                    }
                    break;
                case 'D':
                    if (!rightStack.isEmpty()) {
                        leftStack.push(rightStack.pop());
                    }
                    break;
                case 'B':
                    if (!leftStack.isEmpty()) {
                        leftStack.pop();
                    }
                    break;
                case 'P':
                    char c = command.charAt(2);
                    leftStack.push(c);
                    break;
            }
        }

        StringBuilder sb = new StringBuilder();
        while (!rightStack.isEmpty()){
            leftStack.push(rightStack.pop());
        }
        for(char x: leftStack){
            sb.append(x);
        }
        System.out.println(sb);
    }
}
