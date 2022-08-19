import java.io.*;

public class B_2292  {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int room = 0;

        for (int i = 0; i < 100000; i++) {
            int a = 3 * i * i + 3 * i + 2;
            int b = 3 * i * i + 9 * i + 8;
            if (a <= N && N < b) {
                room = i + 2;
                break;
            } else if (N == 1) {
                room+=1;
                break;
            }
        }
        bw.write(String.valueOf(room));
        bw.flush();

        br.close();
        bw.close();

    }
}
