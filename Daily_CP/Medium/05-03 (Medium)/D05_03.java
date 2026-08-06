import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class D05_03 {

    private static List<Integer> Lista = new ArrayList<>(Arrays.asList(2, 1, 2));


//O(N)^2
public static void main(String[] args){
    int left = 0;
    int right = 0;
    int water = 0;

    for(int i = 1; i<Lista.size(); i++){
        for (int j = i; j < i; j++){
        left = Math.max(left, Lista.get(j));}

    for (int r = i; r < Lista.size(); r++){
        right = Math.max(right, Lista.get(r));
    }

    int waterd = Math.min(left, right) - Lista.get(i);
    water += waterd;

}}}
