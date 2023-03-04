package backjoon;

import java.util.Scanner;

public class n10870 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		System.out.println(Fibo(n));
		
	}
	
	private static int Fibo(int n) {
		// TODO Auto-generated method stub
		int N=0;
		
		if(n==0) return N;
		else if (n==1) {
			N=1;
			return N;
		}
		else {
			N = Fibo(n-1)  + Fibo(n-2);
			return N;
		}
	}
}
