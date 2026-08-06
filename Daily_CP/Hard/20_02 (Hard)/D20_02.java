import java.util.HashMap;
import java.util.Map;

public class D20_02{

    public static int length_longest_path(String input) {
        int max_length = 0;
        Map<Integer, Integer> path_len = new HashMap<>();
        path_len.put(0, 0); 

        for (String line : input.split("\n")) {
            int depth = line.lastIndexOf("\t") + 1;
            String name = line.substring(depth);

            int current_length = path_len.get(depth) + name.length();

            if (name.contains(".")) {
                max_length = Math.max(max_length, current_length);
            } else {
                path_len.put(depth + 1, current_length + 1); 
            }
        }

        return max_length;
    }


    public static void main(String[] args) {
        String input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n" +
                    "\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext";

        System.out.println(length_longest_path(input));
}}

