package array;

public class P611 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(triangleNumber(new int[]{ 2,2,3,4  })); //E 3
	}

	/**
	 * Time Limit Exceeded
	 * 
	 * @param nums
	 * @return
	 */
	public static int triangleNumber(int[] nums) {
		int count = 0;
        for(int i=0;i<nums.length;i++) {
        	for(int j=i+1;j<nums.length;j++) {
        		for(int k=j+1;k<nums.length;k++) {
                	if(isValidTriangle(nums[i], nums[j], nums[k])) {
                		count++;
                	}
                }
            }
        }   
        return count;
    }
	
	public static boolean isValidTriangle(int a, int b, int c) {
		if( a + b > c && b+c > a && a + c > b) {
			return true;
		}		
		return false;
	}
}
