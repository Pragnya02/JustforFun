package trialathon;
import java.util.Arrays;
import java.util.Scanner;

public class schedule {
    
		public static void main(String[] args)
		{
		int n,total_time[]={0,0,0,0};
		int start_time[]={0,0,0,0},finish_time[]={0,0,0,0};
		int i,completion_time=0,max=0;	
		System.out.println("Enter the total number of Racers:  ");
		Scanner sc = new Scanner(System.in);
		n=sc.nextInt();
		int oldswimming_time[]=new int[n];
		int oldbiking_time[]=new int[n];
		int oldracing_time[]=new int[n];
		int newswimming_time[]= new int[n];
		int newbiking_time[]=new int[n];
		int newracing_time[]=new int[n];

		for(i=0;i<n;i++)
		 {
			//Scanner y = new Scanner(System.in);
			System.out.println("Enter in the following order: Swimming time Biking Time Racing Time for \n  Racer: "+i);
		    oldswimming_time[i]=sc.nextInt();
		    oldbiking_time[i]=sc.nextInt() ;
		    oldracing_time[i]=sc.nextInt() ;   
		 }
		
		 //Makign a copy of Swimming Time
		for(i=0;i<n;i++)
		{
			newswimming_time[i]=oldswimming_time[i];
		}
		
		//sorting the new swimming time
			Arrays.sort(newswimming_time);
		
		
		//after sorting
		int j;
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
			if(newswimming_time[i]==oldswimming_time[j])
				{
					newbiking_time[i] = oldbiking_time[j];
					newracing_time[i] = oldracing_time[j];
				}
			}
		}
		finish_time[0]=start_time[0]+newswimming_time[0];
		System.out.println("Racer 0 Start time: "+start_time[0]+" Finish Time: "+finish_time[0]+" Swimming Time: "+newswimming_time[0]+" Biking Time: "+newbiking_time[0]+" Racing Time: "+newracing_time[0]+"\n");
		
		//finds the start_time and finish time of every racer(according to their swimming time)
		for(i=1;i<n;i++)	
		{
			start_time[i]=finish_time[i-1];
			finish_time[i]=start_time[i] + newswimming_time[i];
			System.out.println("Racer "+i+" Start time: "+start_time[i]+" Finish Time: "+finish_time[i]+" Swimming Time: "+newswimming_time[i]+" Biking Time: "+newbiking_time[i]+" Racing Time: "+newracing_time[i]+ "\n");
		}
		
		//Calculates total time taken and the Completion Time of the Scheduling
		for(i=0;i<n;i++)
				{
	total_time[i]=start_time[i]+newswimming_time[i]+newbiking_time[i]+newracing_time[i];
				if(max<total_time[i])
				{
					max=total_time[i];
				}
				completion_time=max;
				System.out.println("Total Time for Racer "+i+": "+total_time[i]);
				}
		System.out.println("\n Completion Time: "+completion_time);
	sc.close();
		}
}

