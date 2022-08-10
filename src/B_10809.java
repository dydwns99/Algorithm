import java.util.HashMap;
import java.util.Scanner;
public class B_10809 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.next();
        char[] arr = word.toCharArray();

        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        for (int i = 'a'; i <= 'z'; i++) {
            map.put((char) i, -1);
        }
        for (int j = 0; j < word.length(); j++) {
            if (map.get(arr[j]) != -1) {
                continue;
            }
            map.put(arr[j], j);
        }

        for (char k = 'a'; k <= 'z'; k++) {
            System.out.print(map.get(k) + " ");
        }
    }
}
