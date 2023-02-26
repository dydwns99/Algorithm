import java.io.*;
import java.util.HashMap;
import java.util.LinkedList;

public class B_1316 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        String []words = new String[n];
        int num=0;
//1.연속 문자열 삭제
// -> 여러개 케이스 입력할때 뭔가 문제!
        for (int i = 0; i < n; i++) {
            LinkedList<String> word = new LinkedList<>();
            HashMap<String, Integer> map = new HashMap<>();
            String s = br.readLine();
            String[] arr = s.split("");
            for (int j = 0; j < arr.length; j++) {
                try {
                    if (arr[j].equals(arr[j + 1]))
                        continue;
                    else
                        word.add(arr[j]);
                }catch (IndexOutOfBoundsException e) {
                    word.add(arr[j]);
                }
            }
            //2.hash이용
            for (int k = 0; k < word.size(); k++) {
                map.put(word.get(k),0);
            }
            for (int k = 0; k < word.size(); k++) {
                if (map.get(word.get(k)) == 0) {
                    map.put(word.get(k),1);
                }
                else{
                    num++;
                    break;
                }
            }
        }
        bw.write(String.valueOf(n-num));
        bw.flush();

        br.close();
        bw.close();

    }
}
