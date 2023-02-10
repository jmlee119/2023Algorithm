package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class n2581 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int M = Integer.parseInt(bf.readLine());
		int N = Integer.parseInt(bf.readLine());
		int max = 10000;
		boolean[] arr = new boolean[max+1];
		arr = isPrime(arr, max+1);
		int sum =0;
		int count=0;
		int min=0;
		for (int i = M; i <= N; i++) {
			if(!arr[i]) {
				sum += i;
				count++;
				if(count==1) {
					min = i;
				}
			}
		}
		if (count==0) {
			System.out.println(-1);
		} else {
			System.out.println(sum);
			System.out.println(min);
		}
		
		
	}
	
	
	static boolean[] isPrime(boolean[] b, int m) {
		b[0] = true;
		b[1] = true;
		for (int i = 2; i < Math.sqrt(m); i++) {
			if(!b[i]) {
				for (int j = i*i; j < m; j+=i) {
					b[j] = true;
				}
			}
		}
		return b;
	}

}
