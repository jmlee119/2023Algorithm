package backjoon;

import java.util.Scanner;

public class n10872 {
	public static int Fact(int n) {
		if (n==0) return 1;
		else {
			int N = n * Fact(n-1);
			return N;
		}
	
	}

	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		System.out.println(Fact(n));
		
	}
	
}
