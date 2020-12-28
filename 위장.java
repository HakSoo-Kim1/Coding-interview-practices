import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        Hashtable<String,Integer> table = new Hashtable<>();
        for (int i = 0; i < clothes.length; i++){
            if (table.get(clothes[i][1]) == null){

                table.put(clothes[i][1],1);
            }
            else {
                table.put(clothes[i][1],table.get(clothes[i][1])+1);
            }
        }
        int answer = 0;
        Integer[] arr = table.values().toArray(new Integer[table.size()]);
        for (int i = 0; i<arr.length ; i++){
            for (int j = i; j<arr.length; j++){
                if (i != j)
                    answer += arr[i] * arr[j];
                else
                    answer += arr[i];
            }
        }
        return answer;
    }
}