import java.io.*;
import java.util.StringTokenizer;

public class B_2869 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int V = Integer.parseInt(st.nextToken());
        double x = (double) (V - A) / (A - B) ;
        double day = Math.ceil(x) ;

        bw.write(String.valueOf((int)day+1));
        bw.flush();

        br.close();
        bw.close();
    }
}
