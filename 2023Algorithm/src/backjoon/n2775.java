package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class n2775 {

	public static void main(String[] args) throws  IOException {
		// TODO Auto-generated method stub
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(bf.readLine());
		int[][] arr = new int[15][15];
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < 15; i++) {
			arr[0][i] = i;
			arr[i][1] = 1;
		}
		for (int i = 1; i < 15; i++) {
			for (int j = 2; j < 15; j++) {
				arr[i][j] = arr[i-1][j] +arr[i][j-1];
			}
		}
		for (int i = 0; i < T; i++) {
			int k = Integer.parseInt(bf.readLine());
			int n = Integer.parseInt(bf.readLine());
			sb.append(arr[k][n]+"\n");
		}
		System.out.println(sb);
	}

}
