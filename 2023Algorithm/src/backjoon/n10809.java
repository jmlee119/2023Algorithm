package backjoon;

import java.util.Scanner;

public class n10809 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int[] arr= new int[26];
		for (int i = 0; i < arr.length; i++) {
			arr[i]=-1;
		}
		String s = sc.nextLine();
		
		for (int i = 0; i < s.length(); i++) {
			char ch= s.charAt(i);
			if(arr[ch-'a']==-1) {
				arr[ch-'a']=i;
			}
		}
		for (int i = 0; i < arr.length; i++) {
			System.out.println(arr[i]);
		}
	}

}
