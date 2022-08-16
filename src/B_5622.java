import java.io.*;
import java.util.HashMap;

public class B_5622 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        HashMap<Character, Integer> map = new HashMap<>();
        int f=3;
        for (int i = 'A'; i <='M'; i+=3) {
            for (int j = 0; j < 3; j++) {
                map.put((char) (i+j), f);
            }
            f++;
        }
        for (int k = 'P'; k <= 'S'; k++) {
            map.put((char) k, 8);
        }
        for (int l = 'T'; l <= 'V'; l++) {
            map.put((char) l, 9);
        }
        for (int m = 'W'; m <= 'Z'; m++) {
            map.put((char) m, 10);
        }

        String s = br.readLine();
        String [] arr = s.split("");
        int sum=0;
        for (int n = 0; n < arr.length; n++) {
            sum += map.get(arr[n].charAt(0));
        }

        bw.write(String.valueOf(sum));
        bw.flush();

        br.close();
        bw.close();
    }
}
