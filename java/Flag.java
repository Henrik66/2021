// Name: 
public class Flag 
{
	private String stars;
	private String dashes;
	
	
	

   public Flag(String initStars, String initDashes) {

	   	stars = ("*******************");
	   	dashes = ("--------------------");
   }

   public void print() {
	   
	   System.out.println(stars);
	   System.out.println(dashes);
	   System.out.println(stars);
	   System.out.println(dashes);
	   System.out.println(stars);
	   
   }

   public void printTwoBlankLines() {
	   
	   System.out.println("\n \n");
	   
   }
   
   public static void main(String args[]) {
      //instantiate a Flag object
	   Flag coolFlag = new Flag("11111111111111111111", "___________________");
      
      //call methods to draw a flag
	   coolFlag.print();
   }
}