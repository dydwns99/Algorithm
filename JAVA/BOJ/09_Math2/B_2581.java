import java.io.*;
import java.util.ArrayList;

public class B_2581 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        ArrayList<Integer> arrayList = new ArrayList<>();

        int M = Integer.parseInt(br.readLine());
        int N = Integer.parseInt(br.readLine());

        for (int i = M; i <= N; i++) {
            for (int k = 1; k <= i; k++) {
                if (i % k == 0 && k != 1 && k != i) {
                    break;
                } else if(k==i-1){
                    arrayList.add(i);
                }
            }
        }

        if (arrayList.size()!=0) {
            int sum = 0;
            for (int j = 0; j < arrayList.size(); j++) {
                sum += arrayList.get(j);
            }

            bw.write(String.valueOf(sum) + "\n");
            bw.write(String.valueOf(arrayList.get(0)));
        } else {
            bw.write(String.valueOf(-1));
        }


        bw.flush();

        br.close();
        bw.close();

    }
}
