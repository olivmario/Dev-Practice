public class D12_02 {

    public static int main(int[] lista) {
        int anterior2 = 0;
        int anterior = 0;

        for (int n : lista) {
            int somaAtual;
            if (anterior2 + n > anterior) {
                somaAtual = anterior2 + n;
            } else {
                somaAtual = anterior;
            }
            anterior2 = anterior;
            anterior = somaAtual;
        }
        return anterior;
    }
}