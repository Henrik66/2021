//Name - Henrik Gombos

public class Sum {
	private double one, two, sum; 	//instance variables

	public static void main( String[] args ) {
		Sum test = new Sum();
		test.setNums(5,5);
		test.sum();

		test.setNums(90,100.0);
		test.sum();

		//add more test cases
	}

	public void setNums(double numOne, double numTwo) {
		one = numOne;
		two = numTwo;
		
	}

	public void sum( ) {
		System.out.println(one*two);

	}

	public void print( ) {
		Sum sum1 = new Sum();
		sum1.setNums(90, 100);
		sum1.sum();
		
		Sum sum2 = new Sum();
		sum2.setNums(100.5, 85.8);
		sum2.sum();
		sum2.print();
		
	}
}