import java.io.*;
import java.util.ArrayList;

public class B_2775 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ArrayList<Integer> k = new ArrayList<>();
        ArrayList<Integer> n = new ArrayList<>();

        int tc = Integer.parseInt(br.readLine());

        for (int t = 0; t < tc; t++) {
            k.add(Integer.parseInt(br.readLine()));
            n.add(Integer.parseInt(br.readLine()));
        }


        int[][] apt = new int[15][14];

        for (int t = 0; t < apt[0].length; t++) {
            apt[0][t] = t + 1;
        }
        for (int t = 0; t < apt.length; t++) {
            apt[t][0] = 1;
        }

        for (int i = 1; i < apt.length; i++) {
            for (int j = 1; j < 14; j++) {
                apt[i][j] = apt[i][j - 1] + apt[i - 1][j];
            }
        }

        for (int t = 0; t < tc; t++) {
            bw.write(String.valueOf(apt[k.get(t)][n.get(t)-1])+"\n");
            bw.flush();
        }

        br.close();
        bw.close();
    }


}

