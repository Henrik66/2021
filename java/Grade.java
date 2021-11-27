import java.util.Scanner;

//Name:

public class Grade {
	private int numGrade;
	 

	public static void main(String[] args) {
		Scanner numGrade = new Scanner(System.in);
		System.out.println("Enter a number grade: ");
		String grade = numGrade.nextLine();
		
	}

	public Grade() {
		
	}

	public Grade(int grade) {

	}

	public void setGrade(int grade) {

	}

	public String getLetterGrade() {
		String letGrade = "";
		if (grade >= 90) {
			return "A"
		}

		elif grade <= 90 and => 80 {
			return "B"
		}

		return letGrade;
	}

	public String toString() {
		return numGrade + " is a " + getLetterGrade() + "\n";
		
	}
}




