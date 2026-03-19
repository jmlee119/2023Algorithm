package backjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;

public class n26069 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int Testcase = Integer.parseInt(br.readLine());
        HashSet<String> set = new HashSet<>();

        set.add("ChongChong");
        for (int i=0; i<Testcase; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            String a = st.nextToken();
            String b = st.nextToken();

            if(set.contains(a) || set.contains(b)) {
                set.add(a);
                set.add(b);
            }

        }
        System.out.println(set.size());
    }
}
