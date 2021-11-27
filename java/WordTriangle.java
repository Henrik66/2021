//Name: Henrik Gombos

public class WordTriangle {
	private String word;

	public static void main(String[] args) {
		// add test cases
		WordTriangle test = new WordTriangle();
		
		test.setWord();
		test.tri();
	}

	public WordTriangle() {
		word = ""; 
		this.word = word
	}

	public void tri() {
		while () {
			for (int i = 0; i <= word.length(); i++) {
				String str = word.substring(0, i);
				System.out.println(str);
			}
		}
	}
	
//	public void tri() {
//		
//		for (int i = 0; i <= word.length(); i++) {
//			String str = word.substring(0, i);
//			System.out.println(str);
//		}
//	}
	
	public void setWord() {
		word = "hippo";
	}



	public void print() {

	}
}