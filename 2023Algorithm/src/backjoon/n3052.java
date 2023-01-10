package backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class n3052 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int[] arr = new int[10];
        boolean bl;
        int count = 0;
        
        for(int i=0; i<arr.length; i++) {
        	arr[i] = Integer.parseInt(br.readLine())%42;
        }
        
        for(int i=0; i<10; i++) {
        	bl = false;
            for(int j=i+1; j<arr.length; j++) {
            	if(arr[i] == arr[j]) {
                	bl = true;
                    break;
               	}
            }
            if(bl==false) {
            	count++;
            }
        }
        System.out.println(count);
    
	}
	
}
