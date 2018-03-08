import java.util.ArrayList;
import java.util.Scanner;

public class CubeRoot {
	private static ArrayList<Integer> check;
	private static int[] result;
	
	public static void main(String[] args) {
		int number;
		
		Scanner scan = new Scanner(System.in);
		
		System.out.println("What nubmer would you liked cube rooted?");
		
		number = scan.nextInt();
		
		scan.close();
		
		root(number, 1, 1, 1);

	}
	
	private static int[] root(int num, int x, int y, int z) {
		
		return null;
	}

}
