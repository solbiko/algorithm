import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        
        long start = 1;
        long end =(long)times[times.length-1] * n;
        
        while (start < end){
            long t = (start + end) / 2;
            if (isValid(t,n,times)){
                 end = t;
            }else{
                start = t+1;
            }
        }    
        return start;
    }
    
    private boolean isValid(long t, int n, int[] times){
        long c = 0;
        for (int time: times){
            c+=t/time;
        }
        return c>=n;
    }
}