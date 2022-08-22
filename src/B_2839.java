import java.io.*;

public class B_2839 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int t = N/5;
        int b = N/5;
        int a = 0;

        int s =0;

        for (int i = t; i >= 0; i--) {
            if ((N - i * 5) % 3 == 0) {
                a = (N - i * 5) / 3;
                s=a+b;
                break;
            }
            else {
                s=-1;
            }
            b--;
        }

        bw.write(String.valueOf(s));
        bw.flush();

        br.close();
        bw.close();

    }
}
