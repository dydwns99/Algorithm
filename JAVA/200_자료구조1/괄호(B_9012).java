import java.io.*;
import java.util.Stack;

public class B_9012 {
    public static void main(String[] args) throws IOException {
        //스택으로 (,) 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            Stack<Character> stack = new Stack<>();
            char[] c = br.readLine().toCharArray();
            for (int i = 0; i < c.length; i++) {
                stack.push(c[i]);
            }
            int n = stack.size();
            int m = stack.size();
            int a=0;
            int b=0;
            String s = "YES";
            //스택 맨위 부터 꺼내 확인
            while (n -- >0) {
                if (stack.peek().equals(')')) {
                    stack.pop();
                    a++;
                } else if (stack.peek().equals('(') && n<m) {
                    b++;
                    if (b > a) {
                        s = "NO";
                        break;
                    } else {
                        stack.pop();
                    }
                } else if (stack.peek().equals('(') && n == stack.size()) {
                    s = "NO";
                    break;
                }
            }
            if (a != b) {
                s = "NO";
            }
            bw.write(s+"\n");
            bw.flush();
        }
        bw.close();
        br.close();
    }
}

