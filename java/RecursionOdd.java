//Name: Henrik Gombos
public class RecursionOdd {

	public static void main(String args[]) {
		System.out.println(RecursionOdd.countOddDigit(32897));

	}

	public static int countOddDigit(int num) {
		if (num > 0) {
			int lastDigit = num%10;
			if (lastDigit%2 != 0) {
				return 1 + countOddDigit(num/10);
			}
			return countOddDigit(num/10);
		}
		return 0;
	} 
}