package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class n3009 {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		
		int x1 = Integer.parseInt(st.nextToken());
		int y1 = Integer.parseInt(st.nextToken());
		
		st= new StringTokenizer(bf.readLine());
		int x2 = Integer.parseInt(st.nextToken());
		int y2 = Integer.parseInt(st.nextToken());
		
		st= new StringTokenizer(bf.readLine());
		int x3 = Integer.parseInt(st.nextToken());
		int y3 = Integer.parseInt(st.nextToken());
		
		System.out.println(coordinate(x1, x2, x3)+" "+coordinate(y1, y2, y3));
		
		
	}
	private static int coordinate(int a,int b,int c) {
		if (a==b) {
			return c;
		}
		else if (b==c) {
			return a;
		}
		else {
			return b;
		}
	}
}
