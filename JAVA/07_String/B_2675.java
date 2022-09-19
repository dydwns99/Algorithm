import java.util.Scanner;
public class B_2675 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        class alph{
            int a;
            String b;
            char[] b_char;
        }
        alph ap[] = new alph[t];

        for (int c = 0; c < ap.length; c++) {
            ap[c]=new alph();
            ap[c].a = sc.nextInt();
            ap[c].b = sc.next();
            ap[c].b_char = ap[c].b.toCharArray();
        }

        for (int d = 0; d < ap.length; d++) {
            for (int i = 0; i < ap[d].b_char.length; i++) {
                for (int j = 0; j < ap[d].a; j++) {
                    System.out.print(ap[d].b_char[i]);
                }
            }
            System.out.println();
        }
    }
}
