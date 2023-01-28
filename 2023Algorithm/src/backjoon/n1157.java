package backjoon;

import java.util.Scanner;

public class n1157 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		String s= sc.next().toUpperCase();
		int[] num = new int[26];
		
		for (int i = 0; i < s.length(); i++) {
			int a = s.charAt(i)-'A';
			num[a]++;
		}
		int max =0;
		char ans = '?';
		for (int i = 0; i < num.length; i++) {
			if(max < num[i]) {
				max = num[i];
				ans = (char)(i+'A');
			} else if (max == num[i]) {
				ans ='?';
			}
		}
		System.out.println(ans);
		
	}

}
