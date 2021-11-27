//Name: 

public class Perfect {
   private int number;

	  public static void main (String[] args) {
		  Perfect perfect = new Perfect();
		  System.out.println(.isPerfect());
		  // call isPerfect here or in a print method
		  // add other test cases
	  }
	//add constructors

	  public Perfect(int number) {
		  this.number = number;
	  }
	  
	  
	public int getNumber() {
		return number;
	}
	public void setNumber(int num) {
		this.number = number;
	}

	public boolean isPerfect() {
		
		return false;
	}
}