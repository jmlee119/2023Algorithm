package backjoon;

import java.util.Iterator;
import java.util.Scanner;

public class n2798 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int M = sc.nextInt();
		
		int[] arr= new int[N];
		for (int i = 0; i < arr.length; i++) {
			arr[i] = sc.nextInt();
		}
		int max =0,sum=0;
		for (int i = 0; i < arr.length; i++) {
			for (int j = i+1; j < arr.length; j++) {
				for (int k = j+1; k < arr.length; k++) {
					sum = arr[i] + arr[j] + arr[k];
					if (max <sum && sum  <= M) {
							max = sum;
						
					}
				}
			}
		}
		System.out.println(max);
	}
	
	
}
