class Solution {
    public void rotate(int[] nums, int k) {
        System.out.println(k);
        k %= nums.length; 
      //  System.out.println(k);
        
        int prev; 
        int temp; 
        for (int i = 0; i < nums.length; i++) {
            lprevast = nums[nums.length -1];
            System.out.println("i "+nums[i]);
            for (int j = 0; j < nums.length; j++) {
                System.out.println("j "+nums[j]);
                temp = nums[j];
                nums[j] = prev; 
                temp = prev;
            }
                
            }
        }
    }




We use an extra array in which we place every element of the array at its correct position i.e. the number at index ii in the 
original array is placed at the index (i + k) \% \text{ length of array}(i+k)% length of array. Then, we copy the new array to the original one.


class Solution {
    public void rotate(int[] nums, int k) {
    	int [] arr = new int [nums.length];
    	for (int i = 0; i < nums.length; i++) {
    		System.out.println(arr[(i+k) % nums.length]);
    	}
    
    }
}



class Solution {
    public int searchInsert(int[] nums, int target) {

        for (int i = 0; i < mid; i++) {
            if (nums[i] == target) {
                return i;
            }
        }
    	for (int j = mid; j < right; j++) {
            if (nums[j] == target) {
            	return j;
            }
        }
        return ; 
    }
    }
    
    
    class Solution {
    public String reverseWords(String s) {
        
        int fast = 1; 
        StringBuilder results = new StringBuilder(); 
        
        System.out.println("string "+s);
        while (fast < s.length()) {
            int slow = 0; 

            if (s.contains(" ")) {
                String wordStart = s.substring(slow, slow + 1);
                String wordEnd =  s.substring(fast, fast +2);
                
                String swappedWord = swap(s, wordStart, wordEnd);
                results.append(swappedWord);
                
                System.out.println("swappedWord \n" + swappedWord);
                System.out.println("results arr \n" + results.toString());

            }
            fast++; 
        }
        return s;
    }
    
    
    class Solution {
    public String reverseWords(String s) {
        
        StringBuilder results = new StringBuilder(); 
        String swappedWord=" ";
        

        int fast = 1; 
        while (fast < s.length()) {
            int slow = 0; 

            if (s.contains(" ")) {
                String wordStart = s.substring(slow, slow + 1);
                String wordEnd =  s.substring(fast, fast + 1);
                
                swappedWord = swap(s, wordStart, wordEnd);
                results.insert(slow, swappedWord);

                System.out.println("swappedWord \n" + swappedWord);
                System.out.println("results arr \n" + results.toString());
                slow++;
            }
            fast++; 
        }
        return results.toString();
    }
               
public String swap(String s, String left, String right) {
    System.out.println("startin swap");
    
    String start = "";
    while (left != right) {
        
        start = left + right;  
        right = start.substring(0, start.length() - right.length());  
        start = start.substring(right.length());  
        return start;

    }
    
    return start;
}
              
 }      
 }