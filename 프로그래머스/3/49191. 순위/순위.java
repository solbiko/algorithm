class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        
        
        boolean[][] graph = new boolean[n][n];
        for (int[] edge: results){
            int u = edge[0]-1;
            int v = edge[1]-1;
            graph[u][v] = true;
        }
        
        
        for(int u=0; u<n; u++){
            int wins = countForward(u, graph, new boolean[n]) -1;
            int loses = countBackward(u, graph, new boolean[n]) -1;
            
            if (wins+loses+1==n){
                answer++;
            }

        }
        
        return answer;
    }
    
    private int countForward(int u, boolean[][] graph, boolean[] visited){ // 이긴 수
        int cnt = 1;
        
        for(int v=0; v<graph[u].length; v++){
            if (!graph[u][v] || visited[v]) continue;
            visited[v] = true;
            cnt+= countForward(v, graph, visited);
        }
        return cnt;
    }
    
        private int countBackward(int u, boolean[][] graph, boolean[] visited){ // 진 수
        int cnt = 1;
        
        for(int v=0; v<graph.length; v++){
            if (!graph[v][u] || visited[v]) continue;
            visited[v] = true;
            cnt+= countBackward(v, graph, visited);
        }
        return cnt;
    }
    
    
    
}