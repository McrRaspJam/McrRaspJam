public class HelloWorldSquareNumber
{
	public static int squareOf(int number)
	{
		int squareNumber = number * number;
		return squareNumber;
	}


	public static void main(String[] args)
	{
		for(int i=0; i<10; i++)
		{
			System.out.println(squareOf(i));
		}
	}
}
