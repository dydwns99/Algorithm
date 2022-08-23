import java.io.*;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class B_10757 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        BigInteger A = new BigInteger(st.nextToken());
        BigInteger B = new BigInteger(st.nextToken());

        bw.write(String.valueOf(A.add(B)));
        bw.flush();

        br.close();
        bw.close();
    }
}
