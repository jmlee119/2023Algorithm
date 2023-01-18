package backjoon;

import java.util.Scanner;

public class n4344 {
	public static void main(String[] args) {
		 Scanner sc = new Scanner(System.in);

	        int C = sc.nextInt();
	        int n;
	        int total = 0;
	        int count = 0;
	        double avg;
	        int scores[] = new int[1000];

	        for(int i=0; i<C; i++) {
	            n = sc.nextInt();
	            for(int j=0; j<n; j++) {
	                scores[j] = sc.nextInt();
	                total += scores[j];
	            }
	            avg = (double) total / n;

	            for(int j=0; j<n; j++) {
	                if(scores[j] > avg) {
	                    count++;
	                }
	            }
	            System.out.printf("%.3f", 100.0 * count / n);
	            System.out.println("%");
	        }
	        sc.close();
	}
}
