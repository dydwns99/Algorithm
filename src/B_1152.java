import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class B_1152 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        ArrayList<String> words = new ArrayList<>();

        while (st.hasMoreTokens()) {
            words.add(st.nextToken());
        }
        bw.write(String.valueOf(words.size()));
        bw.flush();

        bw.close();
        br.close();
    }
}
