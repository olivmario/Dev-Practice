
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class D08_03 {
    private static List<Integer> Lista = new ArrayList<>(Arrays.asList(2, 1, 5, 7, 2, 0, 5));

    public D08_03(){}
public int cont(List<Integer> Lista){

    Collections.sort(Lista);

    int tam = Lista.size();

    if (Lista.size() % 2 != 0){
        return Lista.get(tam/2);}
        else {
        return (Lista.get(tam/2 -1) + Lista.get(tam/2))/2;
        }
}
public static void main(String[] args){

D08_03 test = new D08_03();
System.out.println(test.cont(Lista));

}

}
