import java.util.*;
import java.util.stream.Collectors;


class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        
        
        int[][] graph = new int[n][n];
        for (int[] edge: results){
            int u = edge[0]-1;
            int v = edge[1]-1;
            graph[u][v] = 1;
            graph[v][u] = -1;
        }
        
        
        for(int k=0; k<n; k++){
            for (int s =0; s<n; s++){
                for (int e=0; e<n; e++){
                    if (graph[s][k]==1 && graph[k][e]==1){
                        graph[s][e]=1;
                        graph[e][s]=-1;
                    }
                }
            }
        }

        for(int[] row : graph){
            List<Integer> intList= Arrays.stream(row).boxed().collect(Collectors.toList());
            int numOfZero = Collections.frequency(intList, 0);
            if (numOfZero == 1)
                answer += 1;
        }
        
        return answer;
    }

    
}