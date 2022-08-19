import java.io.*;
import java.util.StringTokenizer;

public class B_1712 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        int n = 0;
        int x = 0;

        if (B >= C) {
            n=-1;
        }
        else {
            x = A / (C - B);
            n = x + 1;
        }
        bw.write(String.valueOf(n));
        bw.flush();

        br.close();
        bw.close();

    }

}
