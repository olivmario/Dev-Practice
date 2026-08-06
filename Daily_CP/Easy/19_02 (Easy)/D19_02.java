import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class D19_02 {

        private List<Integer> log;
        private int N;
        private int index;
        private int size;

    public D19_02(int N){
        this.log = new ArrayList<>(Collections.nCopies(N, null));
        this.N = N;
        this.index = 0;
        this.size = 0;
        
}
    public void record(int orderID){
        this.log.set(index, orderID);
        this.index = ((this.index+1)%N);

        if (this.size < this.N){
            this.size +=1;
        }}

        public int getLast(int i){
            if (i > this.size) {
        throw new IndexOutOfBoundsException();}

            int position = (this.index - i + this.N) % this.N;
            return this.log.get(position);


        }




    }

