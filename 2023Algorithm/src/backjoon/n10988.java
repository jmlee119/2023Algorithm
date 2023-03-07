package backjoon;

import java.util.Scanner;

public class n10988 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.next();
		int a =0;
		for (int i = 0; i < s.length()/2+1; i++) {
			char c= s.charAt(i);
			char c1 = s.charAt(s.length()-i-1);
			if(c!=c1) {
				a=0;
				break;
			}else {
				a=1;
			}			
		}
		System.out.println(a);
	}
}
