import java.util.*;

public class greater {

	/**
	 * @param args
	 */
	
	public static int replace(int number,int[] a,int digit1,int digit2)
	{
		for(int i=0;i<a.length;i++)
		{
			
			if(a[i]==digit1)
				a[i]=digit2;
			else if(a[i]==digit2)
				a[i]=digit1;
		
				
		}
		number=makeNum(a);
		return number;
	}
	
	public static int makeNum(int[] a)
	{	
		int number=0;
		for(int i=0;i<a.length;i++){
			number=number*10+a[i];
		}
		return number;
	}
		
		
		
	
	
	public static void main(String[] args) {
		int digit=534976,i,min=0,changedNum,temp=9;
		int pR=0,pL = 0;
		int a[]=new int[(Integer.toString(digit)).length()];
		
		int num=digit;
		int len = ((Integer.toString(digit)).length());
		for(i=len-1;i>=0;i--)
		{
			a[i] = digit%10;
			digit=digit/10;
		}
		digit=num;	
		for(i=len-1;i>0;i--)
		{
			if(a[i]>a[i-1])
			{
				pR=a[i];
				pL=a[i-1];
				break; //Stop for the 1st pair.
			}
			
		}
		System.out.println("Pair : ("+pL+","+pR+")");
		
		//Find the number greater than pL but lesser than other digits in the right
		
		for(int j=i;j<len;j++)
		{
			if(a[j]>pL && a[j]<temp)
			{		
				temp=a[j];	
			}
		}
		
		changedNum = replace(num,a,temp,pL);
		//System.out.println(changedNum);
		/*for(int j=i;j<a.length-1;j++)
		{
			System.out.println("a[j] "+a[j]+" a[j+1] "+a[j+1]);
			if(a[j+1]<a[j])
			{
				System.out.println("YEs");
				int t=a[j];
				a[j]=a[j+1];
				a[j+1]=t;
			}
		}*/
		int tempArr[]=new int[len];
		int ithArr[] =new int[i];
		for(int j=i;j<a.length;j++){
			tempArr[j]=a[j];
			//System.out.println(tempArr[j]);
			
		}
		for(int j=0;j<i;j++)
		{
			ithArr[j]=a[j];
		}
		Arrays.sort(tempArr);
		//Append sorted array to 1st i values of original array.
		int ithNum=makeNum(ithArr);
		int tempNum=makeNum(tempArr);
		
		changedNum = Integer.parseInt(Integer.toString(ithNum).concat(Integer.toString(tempNum))); 
		System.out.println(changedNum);
	}
	}
	
/*	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int digit=534976,newNum=999999,changedNum;
		int a[]=new int[6];
		int num=digit;
		for(int i=5;i>=0;i--)
		{
			a[i]=digit%10;
			digit=digit/10;
						
		}
		System.out.println(a[0]+" "+a[1]+" "+a[2]+" "+a[3]+" "+a[4]+" "+a[5]);
		int Number=num;
		changedNum=num;
		for(int i=4;i>=0;i--)
		{
			for(int j=i-1;j>=0;j--)
			{
				//Case1
			
			int maximum=0;
			maximum=Math.max(a[i],a[j]);
			System.out.println("Max between "+a[i]+" "+a[j]+" is "+maximum);
			changedNum=replace(num,a,a[j],maximum);
			System.out.println("Changed Number"+changedNum);
			if(changedNum>num)
			{
				System.out.println("Changed Number > digit");
				if(changedNum<newNum)
				{
					System.out.println("Changed Number < New num");
					newNum=changedNum;
					System.out.println("New Number"+newNum);
				}
			
					
			digit=newNum;		
			}
			
			
		}
		}
		System.out.println(digit);
	}
	

}
*/