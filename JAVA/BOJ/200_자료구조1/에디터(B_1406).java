import java.io.*;
import java.util.LinkedList;
import java.util.Stack;

public class B_1406 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        //문자열 입력
        String s = br.readLine();
        Stack<Character> lstack = new Stack<>();
        Stack<Character> rstack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            lstack.push(s.charAt(i));
        }
        //명령어 입력
        int n = Integer.parseInt(br.readLine());
        while (n-- > 0) {
            String command = br.readLine();
            if (command.charAt(0) == 'L') {
                if (!lstack.empty()) {
                    rstack.push(lstack.pop());
                }
            } else if (command.charAt(0) == 'D') {
                if (!rstack.empty()) {
                    lstack.push(rstack.pop());
                }
            } else if (command.charAt(0) == 'B') {
                if (!lstack.empty()) {
                    lstack.pop();
                }
            } else if (command.charAt(0) == 'P') {
                lstack.push(command.charAt(2));
            }
        }
        while (!lstack.empty()) {
            rstack.push(lstack.pop());
        }
        while (!rstack.empty()) {
            bw.write(rstack.pop());
        }
//        float beforeTime = System.currentTimeMillis();


//        float afterTime = System.currentTimeMillis(); // 코드 실행 후에 시간 받아오기
//        float secDiffTime = (afterTime - beforeTime)/1000; //두 시간에 차 계산
//        System.out.println("시간차이(m) : "+secDiffTime);

        bw.flush();

        br.close();
        bw.close();
    }

}
