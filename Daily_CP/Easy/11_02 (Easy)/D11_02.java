class No {
    int valor;
    No esquerda;
    No direita;

    public No(int valor) {
        this.valor = valor;
        this.esquerda = null;
        this.direita = null;
    }
}

public class D11_02 {

    static class Retorno {
        int total;
        boolean status;

        Retorno(int total, boolean status) {
            this.total = total;
            this.status = status;
        }
    }

    static Retorno helper(No no) {
        if (no == null) {
            return new Retorno(0, true);
        }

        Retorno resEsq = helper(no.esquerda);
        int cont_esquer = resEsq.total;
        boolean esq = resEsq.status;

        Retorno resDir = helper(no.direita);
        int cont_direit = resDir.total;
        boolean dir = resDir.status;

        int total = cont_esquer + cont_direit;

        if (esq && dir) {
            if (no.esquerda != null && no.valor != no.esquerda.valor) {
                return new Retorno(total, false);
            }
            if (no.direita != null && no.valor != no.direita.valor) {
                return new Retorno(total, false);
            }
            
            return new Retorno(total + 1, true);
        }

        return new Retorno(total, false);
    }

    static int cont(No raiz) {
        Retorno res = helper(raiz);
        int contar = res.total;
        return contar;
    }

    public static void main(String[] args) {
        No raiz = new No(0);

        raiz.esquerda = new No(1);
        raiz.direita = new No(0);

        raiz.direita.esquerda = new No(1);
        raiz.direita.direita = new No(0);

        raiz.direita.esquerda.esquerda = new No(1);
        raiz.direita.esquerda.direita = new No(1);

        System.out.println(cont(raiz));
    }
}