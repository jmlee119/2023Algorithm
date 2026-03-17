package backjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Stack;

public class n25192 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashSet<String> set = new HashSet<String>();

        int testCase = Integer.parseInt(br.readLine());
        int count =0;

        for(int i=0; i<testCase; i++) {
            String name = br.readLine();

            if (name.equals("ENTER")) {
                count += set.size();
                set.clear();
            }
            else {
                set.add(name);
            }
        }
        count += set.size();
        System.out.println(count);
    }
}
