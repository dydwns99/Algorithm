import java.io.*;

public class B_2941 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String s = br.readLine();
        String[] arr = s.split("");

        int len = arr.length;
        int count =0;
        for (int i = arr.length-1; i >=0 ; i--) {
            try {
                if (len == 0)
                    break;
                else if (arr[i].equals("=")) {
                    if (arr[i - 1].equals("z")) {
                        if (arr[i - 2].equals("d")) {
                            len -= 3;
                            i -= 2;
                            count++;
                        } else {
                            len -= 2;
                            i -= 1;
                            count++;
                        }
                    } else {
                        len -= 2;
                        i -= 1;
                        count++;
                    }
                } else if (arr[i].equals("-")) {
                    len -= 2;
                    i -= 1;
                    count++;
                } else if (arr[i].equals("j") && (arr[i - 1].equals("l") || arr[i - 1].equals("n"))) {
                    len -= 2;
                    i -= 1;
                    count++;
                } else {
                    len -= 1;
                    count++;
                }
            }catch(IndexOutOfBoundsException e){
                if (len == 1 || len==2) {
                    count++;
                }
                break;
            }

        }

        bw.write(String.valueOf(count));
        bw.flush();

        br.close();
        bw.close();
    }
}
