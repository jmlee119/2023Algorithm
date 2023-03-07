package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class n2231 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int num = Integer.parseInt(br.readLine());
		
		int sum=0, min=0;
		int n = 0;
		for (int i = 1; i < num; i++) {
			sum =0;
			n = i;
			while (n!=0) {
				sum = sum + n%10;
				n = n/10;
			}
			if(sum + i == num) {
				min = i;
				break;
			}
		}
		System.out.println(min);
		
		
	}
}
