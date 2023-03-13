package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class n1735 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int firsta  = Integer.parseInt(st.nextToken());
		int lasta = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine());
		int firstb = Integer.parseInt(st.nextToken());
		int lastb = Integer.parseInt(st.nextToken());
		int mo = lasta*lastb/gcd(lasta, lastb);
		int ja = (mo/lasta*firsta)+(mo/lastb*firstb);
		System.out.println(ja/giak(mo,ja)+" "+mo/giak(mo,ja));

	}
	private static int gcd(int lasta, int lastb) {
		if (lastb==0) return lasta;
		return gcd (lastb,lasta%lastb);
	}
	
	private static int giak(int mo,int ja) {
		if(ja==0) return mo;
		return giak(ja,mo%ja);
	}
}
