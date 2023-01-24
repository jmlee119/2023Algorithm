package backjoon;

public class n4673 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		boolean[] check =new boolean[10001];
		
		for (int i = 0; i < check.length; i++) {
			int n = d(i);
			if (n<10001) {
				check[n]=true;
			}
		}
		for (int i = 0; i < check.length; i++) {
			if(!check[i]) {
				System.out.println(i);
			}
		}
		
		
	}
	
	public static int d (int num) {
		int sum = num;
		while (num!=0) {
			sum = sum + (num%10);
			num = num/10;
		}
		return sum;
	}

}
