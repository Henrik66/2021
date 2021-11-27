//Name: Henrik Gombos

import java.util.Scanner;

public class LineBreaker {
   private String line;
   private int width;

   public static void main(String args[]) {
	   Scanner scan = new Scanner(System.in);
	   
   }

    public LineBreaker() {
   	    this("",0);  // calls the constructor below and passes it two params
    }

    public LineBreaker(String str, int wid) {

    }

	public void setLineBreaker(String str, int wid)	{

	}

	public String getLine() {
		return "";
	}

	
	public String getLineBreaker() {
		String box = "/n";
		Scanner countLine = new Scanner(line);
		while (countLine.hasNext()) {
			int changeWidth = width;
			while (changeWidth > 0 && countLine.hasNext()) {
				box += countLine.next();
				changeWidth--;
			}
		}
		box += "/n";
	}
	countLine.close();
	return box;

	public void print() {
		System.out.println()
	}


