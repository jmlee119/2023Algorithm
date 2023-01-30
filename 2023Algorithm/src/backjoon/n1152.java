package backjoon;

import java.util.Scanner;
import java.util.StringTokenizer;

public class n1152 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		String S = sc.nextLine();
		sc.close();
		
		StringTokenizer st = new StringTokenizer(S," ");
		System.out.println(st.countTokens());
	}

}
