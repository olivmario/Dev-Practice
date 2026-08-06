public class D08_02 {
    //supondo que trocamos o nome da classe de "cons" para "D08_02"
    private int one, two;
    public D08_02(int one, int two){
        this.one = one;
        this.two = two;
    }
    public int car(){
        return this.one;
    }
    
    public int cdr(){
        return this.two;
    }

public static void main(String[] args){
    D08_02 cons = new D08_02(3, 4);
    System.out.println(cons.car());
    System.out.println(cons.cdr());



} 
}
