import java.util.*;
class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0; // 소요시간
                 

        
        Queue<Integer> bridge = new LinkedList<>();
        for (int i=0; i<bridge_length; i++){
            bridge.add(0); 
        }
        
         Queue<Integer> waitTrucks = new LinkedList<>();
        for (int i=0; i<truck_weights.length; i++){
            waitTrucks.add(truck_weights[i]); 
        }
        
        
        int bridgeWeight = 0; // 다리 무게

        
        while(waitTrucks.size()>0){
            bridgeWeight -= bridge.poll();
                        
            if (waitTrucks.size()>0 && bridgeWeight + waitTrucks.peek() <= weight){ // 견딜수 있는 무게
                int truckWeight = waitTrucks.poll();
                bridge.add(truckWeight);
                bridgeWeight+=truckWeight;
            }
            else{
                bridge.add(0);
            }
            answer++;
        }
        
        
        while(bridgeWeight>0){
            bridgeWeight-=bridge.poll();
            answer++;
        }
        
        return answer;
    }
}