import java.util.Scanner;
import java.util.Random;
// java hello world vim

public class test { 
	public static void main(String [] args) {
		String question = "";

		if (args.length == 0) {
			Scanner scan = new Scanner(System.in);

			System.out.println("Ask a yes or no question. ");

			question = scan.nextLine();
		}

		else if (args.length > 0) {
			question = args[0];
		}

		else {
			System.out.println("Abort error on input");
			System.exit(1);
		}

		System.out.println("To answer your quesiton: " + question);

		test();
	}

	public static void test() {
		Random r = new Random();

		int low, high, result;

		low = 0;
		high = 100;

		result = r.nextInt(high - low) + low;

		if (result < 25) {
			System.out.println("Don't do it");
		}

		else if (result < 50) {
			System.out.println("Well try again");
		}

		else if (result < 75) {
			System.out.println("It's probabily a good idea");
		}

		else {
			System.out.println("DO it");
		}
	}
}
