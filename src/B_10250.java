import java.io.*;
import java.util.StringTokenizer;

public class B_10250 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = Integer.parseInt(br.readLine());
        String[] room = new String[t];

        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int H = Integer.parseInt(st.nextToken());
            int W = Integer.parseInt(st.nextToken());
            int N = Integer.parseInt(st.nextToken());
            int ho=1;
            while (true) {
                if (N > H) {
                    N -= H;
                    ho++;
                } else {
                    break;
                }
            }
            if (ho < 10) {
                room[i]=String.valueOf(N) + String.valueOf(0) + String.valueOf(ho);
            } else {
                room[i]=String.valueOf(N) + String.valueOf(ho);
            }
        }
        for (int j = 0; j < t; j++) {
            bw.write(room[j]+"\n");
            bw.flush();
        }

        br.close();
        bw.close();

    }
}

