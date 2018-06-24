package array;

import java.util.Arrays;

public class P84 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(largestRectangleArea(new int[]{ 2,1,5,6,2,3  })); //E 10
		System.out.println(largestRectangleArea(new int[]{ 2,2,5,6,2,3  }));  //E 12
		

	}

	public static int largestRectangleArea(int[] heights) {
		int n = heights.length;
		int[][] minimum = new int[n][n];	
		
		int largestArea = Integer.MIN_VALUE;
		
		int max = Integer.MIN_VALUE;
		
		for(int i = 0; i< n; i++) {
			minimum[0][i] = heights[i];		
			if(max < heights[i]) {
				max = heights[i];
			}
		}
		int area = max * 1;
		
		if(largestArea < area ) {
			largestArea = area;
		}
		
		for(int i=1; i<n; i++) {
			max = Integer.MIN_VALUE;
			for(int j=0;j < n-i ; j++) {
				minimum[i][j] = Math.min(minimum[i-1][j], minimum[i-1][j+1]);
				if(max < minimum[i][j]) {
					max = minimum[i][j];
				}
			}
			area = max *(i+1);
			
			if(largestArea < area ) {
				largestArea = area;
			}
		}
		
		return largestArea;
	}
	
	/**
		def largestRectangleArea(self, height):
		    height.append(0)
		    stack = [0]
		    r = 0
		    for i in range(1, len(height)):
		        while stack and height[i] < height[stack[-1]]:
		            h = height[stack.pop()]
		            w = i if not stack else i - stack[-1] -1
		            r = max(r, w*h)
		        stack.append(i)
		    return r
	 */
	

//	public static int largestRectangleArea(int[] heights) {
//		
//		
//	}
}
