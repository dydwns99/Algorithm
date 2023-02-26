import java.io.*;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class B_10845 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        LinkedList<Integer> ll = new LinkedList<>();
        int ft = 0;
        int bk = -1;
        while (n-- > 0) {
            String[] s = br.readLine().split(" ");
            if (s[0].equals("push")) {
                ll.add(Integer.parseInt(s[1]));
                bk++;
            }
            if (s[0].equals("pop")) {
                if (bk == -1) {
                    bw.write("-1\n");
                    bw.flush();
                } else {
                    bw.write(String.valueOf(ll.get(ft))+"\n");
                    bw.flush();
                    ll.remove(ft);
                    bk--;
                }
            }
            if (s[0].equals("size")) {
                bw.write(String.valueOf(ll.size())+"\n");
                bw.flush();
            }
            if (s[0].equals("empty")) {
                if (bk == -1) {
                    bw.write("1\n");
                    bw.flush();
                } else {
                    bw.write("0\n");
                    bw.flush();
                }
            }
            if (s[0].equals("front")) {
                if (bk == -1) {
                    bw.write("-1\n");
                    bw.flush();
                } else {
                    bw.write(String.valueOf(ll.get(ft))+"\n");
                    bw.flush();
                }
            }
            if (s[0].equals("back")) {
                if (bk == -1) {
                    bw.write("-1\n");
                    bw.flush();
                } else {
                    bw.write(String.valueOf(ll.get(bk))+"\n");
                    bw.flush();
                }
            }
        }
        br.close();
        bw.flush();
    }
}

