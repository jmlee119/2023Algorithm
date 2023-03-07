package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Iterator;
import java.util.StringTokenizer;

public class n10815 {
	public static void main(String[] args) throws  IOException {
		HashSet<Integer> s1 = new HashSet<>();
		HashSet<Integer> s2 = new HashSet<>();
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i <N ; i++) {
			s1.add(Integer.parseInt(st.nextToken()));
		}
		int M = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < M; i++) {
			if(s1.contains(Integer.parseInt(st.nextToken()))) {
				sb.append('1').append(" ");
			} else {
				sb.append('0').append(" ");
			}
			
		}
		System.out.print(sb);
		
	}
}
