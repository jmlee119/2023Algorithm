package backjoon;

import java.util.Scanner;

public class n13241 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long a = sc.nextInt();
		long b = sc.nextInt();
		System.out.println(a*b/gcd(a,b));
	}
	
	private static long gcd(long a,long b) {
		if (b==0) return a;
		return gcd(b,a%b);
	}
}