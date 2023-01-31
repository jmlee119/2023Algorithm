package backjoon;

import java.util.Scanner;

public class n1065 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		System.out.println(hansu(num));
	}
	private static int hansu(int num) {
		// TODO Auto-generated method stub
		int count=0;
		if (num <=99) {
			return num;
		}
		else {
			count =99;
			for (int i = 100; i <= num; i++) {
				int h = i/100;
				int t = (i/10)%10;
				int o = i%10;

				if ((h-t)==(t-o)) {
					count++;
				}
			}
		}
		return count;
	}
}
