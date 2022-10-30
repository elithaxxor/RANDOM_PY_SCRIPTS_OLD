/*
StringBuilder()
Constructs a string builder with no characters in it and an initial capacity of 16 characters.
StringBuilder(CharSequence seq)
Constructs a string builder that contains the same characters as the specified CharSequence.
StringBuilder(int capacity)
Constructs a string builder with no characters in it and an initial capacity specified by the capacity argument.
StringBuilder(String str)
Constructs a string builder initialized to the contents of the specified string.
 */

public class run_time_encoding{

    public String encode(final String source){
        System.out.println("[+]--> Encoding "+ source );
        System.out.println("[+]--> Len "+ source.length());
        final StringBuilder string = new StringBuilder();
        for(int i= 0; i <= source.length(); i++ ){
            int run = 1;
            while(i+1 < source.length() && source.charAt(i) == source.charAt(i+1)){
                i++;
                run++;
            }
            string.append(i);
            string.append(source.charAt(i));
        };

        System.out.println("[+]--> Encoded "+ string);
        System.out.println("[+]--> Len "+ string.length());
        return string.toString();
    }

    public static void main (String[] args){
        int a = Integer.parseInt(args[0]);
        Object run_time_encoding = new run_time_encoding();
    }
}
