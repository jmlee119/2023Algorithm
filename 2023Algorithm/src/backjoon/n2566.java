package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class n2566 {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int[][] arr = new int[9][9];
		int max=Integer.MIN_VALUE , x=0, y=0;
		for (int i = 0; i < 9; i++) {
			StringTokenizer st = new StringTokenizer(bf.readLine()," ");
			for (int j = 0; j < 9; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
				if (max <arr[i][j]) {
					max = arr[i][j];
					x= i+1;
					y= j+1;
				}
			}
		}
		System.out.println(max);
		System.out.println(x+" "+y);
	}
}
