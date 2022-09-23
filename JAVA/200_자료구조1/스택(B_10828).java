import java.io.*;
import java.util.Stack;
import java.util.StringTokenizer;


public class B_10828 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Stack<Integer> stack = new Stack<>();

        int N = Integer.parseInt(br.readLine());
        while (N-- > 0) {
            String s = br.readLine();
            String[] st = s.split(" ");
            if (st[0].equals("push")) {
                int a = Integer.parseInt(st[1]);
                stack.push(a);
            } else if (st[0].equals("pop")) {
                if (stack.size() == 0) {
                    bw.write("-1" + "\n");
                    bw.flush();
                } else {
                    int b = stack.pop();
                    bw.write(String.valueOf(b) + "\n");
                    bw.flush();
                }
            } else if (st[0].equals("size")) {
                bw.write(String.valueOf(stack.size()) + "\n");
                bw.flush();
            } else if (st[0].equals("empty")) {
                if (stack.empty()) {
                    bw.write("1" + "\n");
                    bw.flush();
                } else {
                    bw.write("0" + "\n");
                    bw.flush();
                }
            } else if (st[0].equals("top")) {
                if (stack.empty()) {
                    bw.write("-1" + "\n");
                    bw.flush();
                } else {
                    int c = stack.peek();
                    bw.write(String.valueOf(c) + "\n");
                    bw.flush();
                }
            }
        }
        br.close();
        bw.close();
    }
}
