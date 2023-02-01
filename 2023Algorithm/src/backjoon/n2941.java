package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class n2941 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
		String str[]= {"c=","c-","dz=","d-","lj","nj","s=","z="};
		for (int i = 0; i < str.length; i++) {
			if (s.contains(str[i])) {
				s=s.replace(str[i],"0");
			}
		}
		System.out.println(s.length());
	}
}