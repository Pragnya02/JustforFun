//Executes Victor to Zues, Zues to Victor and Amy to Erica!
   
    import java.io.*;
    public class GSA {
    
 public static String[] manlist   = {"Victor", "Wyatt", "Xavier", "Yancey", "Zeus"};
 public static String[] womanlist = {"Amy", "Bertha", "Clare", "Diane", "Erika" };
 public static String[][] manpref = {{"Bertha", "Amy", "Diane", "Erika", "Clare"},
                                       		     {"Diane", "Bertha", "Amy", "Clare", "Erika"},
                                      		     {"Bertha", "Erika", "Clare", "Diane", "Amy"},
                                  		     {"Amy", "Diane", "Clare", "Bertha", "Erika"},
                                       		     {"Bertha", "Diane", "Amy", "Erika", "Clare"}};
public static String[][] womanpref = {{"Zeus", "Victor", "Wyatt", "Yancey", "Xavier"},
                                         	         {"Xavier", "Wyatt", "Yancey", "Victor", "Zeus"},
                                         	         {"Wyatt", "Xavier", "Yancey", "Zeus", "Victor"},
                                        	         {"Victor", "Zeus", "Yancey", "Xavier", "Wyatt"},
                                 	 	         {"Yancey", "Wyatt", "Zeus", "Xavier", "Victor"}};
   
public int check_pref(String womanpref[][],String currentPartner,String newPartner,int position)
   //Checks Preference of Woman
   {
        int i;
        for(i=0;i<5;i++)
        {
            if(womanpref[position][i].equals(newPartner))
            {  return 1;}
            if(womanpref[position][i].equals(currentPartner))
            {return 0;}
        }
        return -1;
   }

public int getmanindex(String man[],String woman_currentPartner)
   {
        int i;
        for(i=0;i<5;i++)
               if(man[i].equals(woman_currentPartner))
                   return i;//returns the index of Current Partner of Wife
        return -1;
   }
public int getwomanindex(String woman[],String proposed_woman)
   { 
        int i;
        for(i=0;i<5;i++)
                     if(woman[i].equals(proposed_woman))
                         return i;
        return -1;
   }
   
public void marry(String men[],String women[],String manpref[][],String womanpref[][])
   {
        int engage_count = 0,i,j,f;
        int woman_index,man_index;
        String manEngagelist[]   = {"free","free","free","free","free"};
        String womanEngagelist[] = {"free","free","free","free","free"};
        while(engage_count<5) //makes sure every man proposes only twice
         {
             for(f=0;f<5;f++)
             {
                 if(manEngagelist[f].equals("free"))
                    {  
                        break;
                    }
             }
             
             for(i=0;i<5 && manEngagelist[f].equals("free");i++)
             {
                 woman_index=getwomanindex(women,manpref[f][i]);
                 if(womanEngagelist[woman_index].equals("free"))
                 {
                     womanEngagelist[woman_index] = men[f];
                     manEngagelist[f] = manpref[f][i];
                     System.out.println(men[f]+" proposes "+manpref[f][i]+" . Accepts --> " +manpref[f][i]+" is free");
                     engage_count++;
                 }
                 else
                 { 
                     String currentPartner = womanEngagelist[woman_index];
                     if(check_pref(womanpref,currentPartner,men[f],woman_index)==1)
                     {
                         womanEngagelist[woman_index]=men[f];
                         man_index=getmanindex(men,currentPartner);
                         System.out.println(" \n"+men[f]+" proposes "+manpref[f][i] + ". Leaves " +currentPartner+ " for "+ men[f]);
                         manEngagelist[f] = manpref[f][i];
                         System.out.println(men[f]+" Marries "+manEngagelist[f]+" \n ");
                         manEngagelist[man_index] = "free";
                     }
                 }
             }
         }
         System.out.println(" ");
         System.out.println(" Final Pair : ");
         System.out.println(" ");
         for(j=0;j<5;j++)
         {System.out.println("Pair( "+womanEngagelist[j]+" , "+women[j]+" )");}
   }
    
 public static void main(String args[])throws IOException
   {
        GSA gs = new GSA();
        String r;
        System.out.println("GS Algorithm");
        System.out.println("(M / m) for order VICTOR to ZUES. \n(RM/rm) for order ZUES to VICTOR. \n(W or w) for AMY to ERICA! M/W \n");
        InputStreamReader isr=new InputStreamReader(System.in);
        BufferedReader br=new BufferedReader(isr);
        r=br.readLine();
        if(r.equals("m") || r.equals("M"))
        {gs.marry(manlist,womanlist,manpref,womanpref);}
        else if(r.equals("w") || r.equals("W"))
        {
            String reversewoman[] = womanlist;
            String reverseman[] = manlist;
            String reversewomanpref[][] =womanpref; 
            String reversemanpref[][]=manpref; 
            gs.marry(reversewoman,reverseman,reversewomanpref,reversemanpref);
         }
        else if(r.equals("rm") || r.equals("RM"))
        {
            String[] reverseman   = {"Zeus", "Yancey", "Xavier", "Wyatt","Victor"};
            String[] reversewoman = {"Erika", "Diane", "Clare","Bertha","Amy"};
            String[][] reversemanpref = {{"Bertha", "Diane", "Amy", "Erika", "Clare"},
                                         {"Amy", "Diane", "Clare", "Bertha", "Erika"},
                                         {"Bertha", "Erika", "Clare", "Diane", "Amy"},
                                         {"Diane", "Bertha", "Amy", "Clare", "Erika"},
                                         {"Bertha", "Amy", "Diane", "Erika", "Clare"}};                             
            String[][] reversewomanpref = {{"Yancey", "Wyatt", "Zeus", "Xavier", "Victor"},
                                           {"Victor", "Zeus", "Yancey", "Xavier", "Wyatt"},
                                           {"Wyatt", "Xavier", "Yancey", "Zeus", "Victor"},
                                           {"Xavier", "Wyatt", "Yancey", "Victor", "Zeus"},
                                           {"Zeus", "Victor", "Wyatt", "Yancey", "Xavier"}};
            gs.marry(reverseman,reversewoman,reversemanpref,reversewomanpref);
        }
         else
            System.out.println("Wrong Input! Exitting");
      }
 }
