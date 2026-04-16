package backjoon;

import java.io.*;
import java.util.*;
public class n1283 {
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());
        boolean[] visitedAlpabet = new boolean[26];

        for (int i = 0; i < N; i++) {
            String st = bf.readLine();
            String[] ch2 = st.split(" ");


            int index = -1;
            int pos = 0;
            for(String s : ch2) {
                char c = Character.toLowerCase(s.charAt(0));
                if (!visitedAlpabet[c - 'a']) {
                    visitedAlpabet[c - 'a'] = true;
                    index = pos;
                    break;
                }
                pos += s.length() + 1;
            }

            if (index == -1){
                for(int j=0; j<st.length(); j++) {
                    char c  = Character.toLowerCase(st.charAt(j));
                    if (c != ' ' && !visitedAlpabet[c - 'a']) {
                        visitedAlpabet[c - 'a'] = true;
                        index = j;
                        break;
                    }
                    pos += 1;
                }
            }
            print(index, st);
        }
        System.out.println(sb);
    }
    static void print(int index, String st) {
        if (index ==-1) {
            sb.append(st).append("\n");
        }
        else{
            sb.append(st.substring(0,index))
                    .append("[")
                    .append(st.charAt(index))
                    .append("]")
                    .append(st.substring(index+1, st.length()))
                    .append("\n");
        }
    }

}

