import java.util.Iterator;
import java.util.Random;


//Iterator pode ser uma lista, um gerador, leitura de arquivo
public class D18_02{
    public static int selectRandom(Iterator<Integer> stream) {
        Random random = new Random();
        int result = 0;
        int i = 0;
        while (stream.hasNext()) {
            int value = stream.next();
            i++;
            if (random.nextInt(i) == 0) {
                result = value;
            }
        }
        return result;
    }
}
