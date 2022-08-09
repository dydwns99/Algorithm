import java.util.Scanner;

public class B_1065 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        hansu hs = new hansu(N);
        System.out.print(hs.func());
    }
}

class hansu {
    private int num;
    public hansu(int a) {
        this.num = a;
    }

    public int func() {
        int n=0;

        if (num < 100) {
            n=num;
        } else if (num >= 100) {
            for (int i = 100; i <= num; i++) {
                int a=i/100;
                int b=i%100/10;
                int c=i%100%10;
                if ((a - b) == (b - c)) {
                    n+=1;
                }
            }
            n+=99;
        }
        return n;
    }
}
