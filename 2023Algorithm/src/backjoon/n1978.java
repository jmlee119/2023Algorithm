package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Iterator;
import java.util.StringTokenizer;

public class n1978 {

	public static void main(String[] args) throws  IOException {
		// TODO Auto-generated method stub
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int num = Integer.parseInt(bf.readLine());
		StringTokenizer st = new StringTokenizer(bf.readLine());
		int[] arr = new int[num];
		int n = 1000;
		for (int i = 0; i < num; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		boolean primeNumberarr[] =  new boolean[n+1];
		primeNumberarr = isprime(primeNumberarr, n+1);
		int count=0;
		for (int i = 0; i < arr.length; i++) {
			if(!primeNumberarr[arr[i]]) count++;
		}
		System.out.println(count);
		
	}
	static boolean[] isprime(boolean[] b, int n) {
		b[0]=true;
		b[1]=true;
		for (int i = 2; i < Math.sqrt(n); i++) {
			if (!b[i]) {
				for (int j = i*i; j < n; j+=i) {
					b[j]=true;
				}
			}
		}
		
		return b;
	}

}
