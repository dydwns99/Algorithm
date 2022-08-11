import java.util.HashMap;
import java.util.Scanner;
public class B_1157 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.next();
        word = word.toUpperCase();
        char[] arr = word.toCharArray();

        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        for (int i = 'A'; i <= 'Z'; i++) {
            map.put((char) i, 0);
        }
        for (int j = 0; j < arr.length; j++) {
            map.put(arr[j],map.get(arr[j])+1);
        }
        int max = 0;
        char output=' ';
        for (int k = 'A'; k <= 'Z'; k++) {
            if (map.get((char)k) > max) {
                max = map.get((char)k);
                output = (char)k;
            }
        }

        for (int l = 'A'; l <= 'Z'; l++) {
            if (map.get((char)l) == max && l != output) {
                output = '?';
            }
        }

        System.out.print(output);
    }
}
