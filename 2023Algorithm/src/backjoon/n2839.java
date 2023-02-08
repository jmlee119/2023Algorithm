package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class n2839 {

	public static void main(String[] args) throws  IOException {
		// TODO Auto-generated method stub
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int num = Integer.parseInt(bf.readLine());
		if(num==4 || num==7) {
			System.out.println(-1);
		}
		else if (num%5==0) {
			System.out.println(num/5);
		}
		else if (num%5==1) {
			System.out.println((num-6)/5 +2);
		}
		else if (num%5==2) {
			System.out.println((num-12)/5 +4);
		}
		else if (num%5==3) {
			System.out.println((num-3)/5+1);
		}
		else if (num%5==4) {
			System.out.println((num-9)/5 +3);
		}
		
	}

}
