import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class B_2908 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        ArrayList<String> words = new ArrayList<>();

        while (st.hasMoreTokens()) {
            words.add(st.nextToken());
        }

        String  []a = rever(words.get(0).split(""));
        String  []b = rever(words.get(1).split(""));

        int ia = Integer.parseInt(String.join("",a));
        int ib = Integer.parseInt(String.join("",b));

        if (ia - ib > 0) {
            bw.write(String.valueOf(ia));
            bw.flush();
        } else {
            bw.write(String.valueOf(ib));
            bw.flush();
        }


        br.close();
        bw.close();

    }

    static String[] rever(String []x) {
        String tmp=null;
        tmp = x[0];
        x[0] = x[2];
        x[2] = tmp;
        return x;
    }
}


