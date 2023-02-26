import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class B_9093 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            StringBuilder sb = new StringBuilder();

            while (st.hasMoreTokens()) {
                char[] c = st.nextToken().toCharArray();
                char[] rc = new char[c.length];
                int a =0;
                for (int j = c.length-1; j >=0; j--) {
                    rc[a] = c[j]; //단어 뒤집음
                    a++;
                }
                //뒤집은 문자들을 하나의 단어로 만들고 al에 넣어 하나의 문자열 만듬
                String s = String.valueOf(rc);
                sb.append(s + " ");
            }
            bw.write(sb.toString()+"\n");
            bw.flush();
        }

        br.close();
        bw.close();

    }
}
