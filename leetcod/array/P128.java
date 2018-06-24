package array;

import java.util.HashMap;
import java.util.Map;

public class P128 {

	//record boundry of each discovery. when length increased, increase the length at boundry. 
    public static int longestConsecutive(int[] nums) {
    	 if(nums.length == 0){
             return 0;
         }
     	int max = Integer.MIN_VALUE;
         Map<Integer, Integer[]> lookup = new HashMap<Integer, Integer[]>();
         
         for(int a : nums) {
        	if(null != lookup.get(a)) {
        		continue;
        	}
        	 
         	int length = 1;
         	Integer[] aa = new Integer[3];
         	         	
         	int before = a-1;        	
         	Integer[] b = lookup.get(before);
         	
         	if(null != b) {
         		length += b[0];
         		aa[1] = before;
         		if(null != b[1]) {
         			aa[1] = b[1];
         		}
         	}
         	
         	int after = a+1;
         	Integer[] c = lookup.get(after);
         	if(null != c) {
         		length += c[0];
         		aa[2] = after;
         		if(null != c[2]) {
         			aa[2] = c[2];
         		}
         	}
         	
         	
         	aa[0] = length;        	
         	        	
         	lookup.put(a, aa);        	
         	
         	Integer[] left = lookup.get(aa[1]);
         	if(left != null) {
         		left[0] = length;
         		left[2] = aa[2]!=null?Math.max(a, aa[2]):a;
         		lookup.put(aa[1], left);
         	}
         	
         	Integer[] right = lookup.get(aa[2]);
         	if(right != null) {
         		right[0] = length;
         		right[1] = aa[1]!=null?Math.min(a, aa[1]):a;
         		lookup.put(aa[2], right);
         		
         	}
         	
         	if(length > max) { 
         		max = length;
         	}
         }
         
         return max; 
     }
 
    
	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		System.out.println(longestConsecutive(new int[]{4, 1, 3, 2}));
//		System.out.println(longestConsecutive(new int[]{4, 1, 3, 2, 5}));
//		System.out.println(longestConsecutive(new int[]{1,2,0,1}));
//		System.out.println(longestConsecutive(new int[]{0, 3, 2, 1}));
//		System.out.println(longestConsecutive(new int[]{0, 3, 2, 4 }));
//		System.out.println(longestConsecutive(new int[]{0, 3, 2, 4, 1}));
		System.out.println(longestConsecutive(new int[]{0,3,7,2,5,8,4,6,0,1 })); //Expected 9
	}

}
