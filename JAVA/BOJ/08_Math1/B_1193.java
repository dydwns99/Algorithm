import java.io.*;

public class B_1193 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int X = Integer.parseInt(br.readLine());
        int fr = 0;
        int u = 0;
        int d = 0;
        for (int i = 0; i < 10000; i++) {
            int a = i * (i + 1) / 2;
            int b = (i + 1) * (i + 2) / 2;
            if (a < X && X <= b) {
                fr = i;
                break;
            }
        }
        if (fr % 2 != 0) {
            u = X - (fr + 1) * fr / 2;
            d = fr + 2 - u;
        } else if (fr % 2 == 0) {
            d = X - (fr + 1) * fr / 2;
            u = fr + 2 - d;
        }
        bw.write(String.valueOf(u) + "/" + String.valueOf(d));
        bw.flush();

        br.close();
        bw.close();
    }
}
