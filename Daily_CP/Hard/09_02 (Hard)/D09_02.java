import java.util.ArrayList;
import java.util.List;

public class D09_02 {
    private List<String> dados = new ArrayList<>();
    private List<Integer> npx = new ArrayList<>();

    public D09_02() {
        // Inicializar vazio
    }

    public void Add(String dado) {
        int enderecoNovo = dados.size();
        int enderecoAnterior = enderecoNovo - 1;
        
        this.dados.add(dado);
        int npxNovo;
        if (enderecoNovo == 0) {
            npxNovo = -1 ^ -1; //Não utilizei 0 pois há a existência do índice 0
        } else {
            npxNovo = enderecoAnterior ^ -1; //-1 represebta vázio/nada
        }
        this.npx.add(npxNovo);
        if (enderecoAnterior >= 0) {
            int npxAtualDoAnterior = this.npx.get(enderecoAnterior);
            int novoNpxDoAnterior = npxAtualDoAnterior ^ -1 ^ enderecoNovo;
            this.npx.set(enderecoAnterior, novoNpxDoAnterior);
        }
    }

    public Integer getNpxByString(String busca) {
        for (int i = 0; i < dados.size(); i++) {
            if (busca.equals(this.dados.get(i))) {
                return this.npx.get(i);
            }
        }
        return null;
    }
    
    public void imprimirLista() {
        int atual = 0;
        int anterior = -1;
        int proximo;
        
        System.out.print("Percorrendo: ");
        while (atual != -1 && atual < dados.size()) {
            System.out.print(dados.get(atual) + " <-> ");
            
            int npxAtual = npx.get(atual);
            proximo = npxAtual ^ anterior;
            
            anterior = atual;
            atual = proximo;
        }
        System.out.println("FIM");
    }

    public static void main(String[] args) {
        D09_02 lista = new D09_02();
        lista.Add("A");
        lista.Add("B");
        lista.Add("C");
        
        // Test
        System.out.println("NPX de B: " + lista.getNpxByString("B")); // Deve ser (0 ^ 2) = 2
        lista.imprimirLista();
    }
}