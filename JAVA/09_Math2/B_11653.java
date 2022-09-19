import java.io.*;

public class B_11653 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        for (int i = 1; i <= N; i++) {
            while (true) {
                if (N % i == 0 && i != 1 && i != N) {
                    bw.write(String.valueOf(i)+"\n");
                    bw.flush();
                    N /= i;
                } else if (i == N && i!=1) {
                    bw.write(String.valueOf(i));
                    bw.flush();
                    break;
                } else {
                    break;
                }
            }
        }
        br.close();
        bw.close();
    }
}
