package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Iterator;
import java.util.Scanner;
import java.util.StringTokenizer;

public class n8958 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		String[] arr= new String[num];
		
		for (int i = 0; i < arr.length; i++) {
			arr[i] = sc.next();
		}
		
		for (int i = 0; i < arr.length; i++) {
			int cnt =0;
			int sum=0;
			for (int j = 0; j < arr[i].length(); j++) {
				if (arr[i].charAt(j)=='O') {
					cnt++;
				}
				else {
					cnt =0;
				}
				sum += cnt;
			}
			System.out.println(sum);
		} 
		
	
	}

}
