package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class n2908 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine()); 
		int num1 = Integer.parseInt(st.nextToken());
		int num2 = Integer.parseInt(st.nextToken());

		int renum1= (num1%10) *100 + ((num1/10)%10)*10 + (num1/100);
		int renum2= (num2%10) *100 + ((num2/10)%10)*10 + (num2/100);
		
		if (renum1 > renum2) {
			System.out.println(renum1);
		} else {
			System.out.println(renum2);
		}
	}	
}
