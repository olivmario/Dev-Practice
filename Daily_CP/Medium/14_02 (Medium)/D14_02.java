import java.util.*;

class Node {
    Map<Character, Node> children = new HashMap<>();
    boolean isEnd = false;
}

public class D14_02{
    private Node root = new Node();

    public void insert(String word) {
        Node node = root;
        for (char c : word.toCharArray()) {
            node.children.putIfAbsent(c, new Node());
            node = node.children.get(c);
        }
        node.isEnd = true;
    }

    public List<String> search(String s) {
        List<String> result = new ArrayList<>();
        Node node = root;

        for (char c : s.toCharArray()) {
            if (!node.children.containsKey(c)) {
                return result;
            }
            node = node.children.get(c);
        }

        dfs(node, s, result);
        return result;
    }

    private void dfs(Node node, String prefix, List<String> result) {
        if (node.isEnd) {
            result.add(prefix);
        }

        for (Map.Entry<Character, Node> entry : node.children.entrySet()) {
            dfs(entry.getValue(), prefix + entry.getKey(), result);
        }
    }
//exemplo
    public static void main(String[] args) {
        D14_02 autocomplete = new D14_02();
        List<String> words = Arrays.asList("dog", "deer", "deal");

        for (String word : words) {
            autocomplete.insert(word);
        }

        System.out.println(autocomplete.search("de"));
    }
}
