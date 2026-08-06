import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class D05_02 {
private static List<Integer> Lista = Arrays.asList(1,2,3,4,5);
private static List<Integer> ListCalc = new ArrayList<>();
public static void main(String[] args){


    for(int i = 0; i<Lista.size() ;i++){
        int resul = 1;
        for(int y = 0; y<Lista.size();y++){
            if (i!=y){
                resul = (resul*Lista.get(y));}}
        ListCalc.add(resul);}

System.out.println(Lista);
System.out.println(ListCalc);
}}
