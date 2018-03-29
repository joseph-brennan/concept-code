
public class overlfow_catch {

	public static void main(String[] args) {
		// TODO ask for user input
		int A, B;
		int maxint = 10; // max int of ten right now
		
		A = 4;
		B = 5;
		
		halfover(A, B, maxint/2);
	}
	
	private static void halfover(int first, int second, int bar) {
		int fixA = Math.abs(first) / 2;
		int fixB = Math.abs(second) / 2;
		int sum = fixA + fixB;
		
		if (sum > bar) {
			System.out.println("error this will overflow");
			System.exit(1);
		}
	}

}
