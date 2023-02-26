import java.io.*;
import java.util.StringTokenizer;

public class B_1978 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int num=0;
        for (int j = 0; j < N; j++) {
            for (int k = 1; k <= arr[j]; k++) {
                if (arr[j] % k == 0 && k!=1 && k!=arr[j]) {
                    break;
                } else if (k == arr[j]-1) {
                    num++;
                }
            }
        }

        bw.write(String.valueOf(num));
        bw.flush();

        br.close();
        bw.close();


    }
}