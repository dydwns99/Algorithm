import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class B_4948 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        ArrayList<Integer> arrayList = new ArrayList<>();

        while (true) {
            int m = Integer.parseInt(br.readLine());
            if (m==0) {
                break;
            }
            arrayList.add(m);
        }

        int[] sum = new int[arrayList.size()];
        for (int b = 0; b < sum.length; b++) {
            sum[b] = 0;
        }

        for (int j = 0; j < arrayList.size(); j++) {
            for (int i = arrayList.get(j)+1; i <= 2*arrayList.get(j); i++) {
                if (i == 0) {
                    break;
                }
                if (i == 1) {
                    continue;
                }
                if (i == 2 || i == 3) {
                    sum[j]++;
                }
                for (int k = 2; k <= (int) Math.sqrt(i); k++) {
                    if (i % k == 0) {
                        break;
                    } else if(k==(int) Math.sqrt(i)){
                        sum[j] += 1;
                    }
                }
            }
        }
        for (int c = 0; c < sum.length ; c++) {
            bw.write(String.valueOf(sum[c])+"\n");
            bw.flush();
        }
        br.close();
        bw.close();
    }
}
