import java.io.*;
//import java.util.ArrayList;
//import java.util.Collections;
//import java.util.HashMap;

public class B_9020 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        boolean[] tst = new boolean[10001];
        tst[1]=true;
        for (int i = 2; i <= 100; i++) {
            if(tst[i]) continue;
            for (int j = i * i; j <= 10000; j += i) {
                tst[j]=true;
            }
        }

        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            int i = n / 2;
            int j = n / 2;
            while (true) {
                if (!tst[i] && !tst[j]) {
                    bw.write(String.valueOf(i) + " " + String.valueOf(j) + "\n");
                    break;
                }
                i--;
                j++;
            }
        }
        bw.flush();
//        int t = Integer.parseInt(br.readLine());
//        int[] n = new int[t];
//        for (int i = 0; i < t; i++) {
//            n[i] = Integer.parseInt(br.readLine());
//        }
//
//        decimal dec = new decimal();
//        ArrayList<Integer> arrayList = new ArrayList<>();
//        HashMap<Integer, Integer> hashMap = new HashMap<>();
//        for (int m = 0; m < t; m++) {
//            for (int i = 2; i <= n[m]; i++) {
//                if (i == 2 || i == 3) {
//                    arrayList.add(i);
//                }
//                if (dec.func(i)&& i!=2 && i!=3) {
//                    arrayList.add(i);
//                }
//            }
//            for (int j = 0; j < arrayList.size(); j++) {
//                //나머지 다른 한 소수
//                int a = n[m] - arrayList.get(j);
//                //두 소수의 차이
//                int b = a-arrayList.get(j);
//                if (dec.func(a)&&b>=0) {
//                    hashMap.put(b,arrayList.get(j));
//                }
//            }
//            Integer min_value = Collections.min(hashMap.keySet());
//            bw.write(String.valueOf(hashMap.get(min_value)) + " " + String.valueOf(n[m] - hashMap.get(min_value))+"\n");
//            bw.flush();
//        }
        br.close();
        bw.close();
    }
}
//class decimal {
//    boolean result;
//    public boolean func(int num) {
//        if (num == 2 && num==3) {
//            result=true;
//        }
//        for (int k = 2; k <= (int) Math.sqrt(num); k++) {
//            if (num % k == 0 && num!=4) {
//                this.result=false;
//                break;
//            } else if(k==(int) Math.sqrt(num)){
//                this.result=true;
//            }
//        }
//        return result;
//    }
//}
