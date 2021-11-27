//Name: Henrik Gombos

public class Rectangle {
	private int length;
	private int width;
	private int perimeter;

	public static void main( String[] args ) {
		Rectangle rect = new Rectangle();
		rect.setLengthWidth(2,6);
		rect.calculatePerimeter();
		rect.print();

		rect.setLengthWidth(12,5);
		rect.calculatePerimeter();
		rect.print();
		
		//add more test cases
	}

	public void setLengthWidth(int len, int wid) {
		length=len;
		width=wid;
	}

	public void calculatePerimeter() {
		System.out.println(length+length+width+width);
	}

	public void print() {
		Rectangle rect1 = new Rectangle();
		rect1.setLengthWidth(131,75);
		rect1.calculatePerimeter();
		rect1.print();
	}
}