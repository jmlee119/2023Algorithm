package backjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;

public class n25757 {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        char GAME = st.nextToken().charAt(0);

        HashSet<String> set = new HashSet<>();
        for (int i=0; i<N; i++) {
            set.add(bf.readLine());
        }
        // System.out.println(set);
        int num = set.size();
        if (GAME == 'Y') {
            System.out.println(num);
        } else if (GAME == 'F') {
            System.out.println(num/2);
        }
        else {
            System.out.println(num/3);
        }
    }

}
