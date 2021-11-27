//Name: Henrik Gombos

import java.util.Scanner;

public class Triangle {
	private int sideA, sideB, sideC;
	private double perimeter;
	private double theArea;

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		System.out.print("Enter side A: ");
		int a = scan.nextInt();

		System.out.print("Enter side B: ");
		int b = scan.nextInt();

		System.out.print("Enter side C: ");
		int c = scan.nextInt();

		Triangle test = new Triangle();
		test.setSides(a, b, c);
		test.calcPerimeter();
		test.calcArea();
	}

	public Triangle() {
		setSides(0,0,0);
		perimeter=0;
		theArea=0;
	}

	public Triangle(int a, int b, int c) {
		a = 3;
		b = 3;
		c = 3;
	}


	public void setSides(int a, int b, int c) {
		sideA = a;
		sideB = b;
		sideC = c;
	}

	public void calcPerimeter() {
		perimeter = (sideA + sideB+ sideC);

	}

	public void calcArea() {
		double s;
		s = (perimeter / 2);	
		theArea = (Math.sqrt(s) * (s-sideA) * (s-sideB) * (s-sideC));

	}

	public void print() {
		System.out.println("The area of this Triangle is: " + theArea);
	}
}