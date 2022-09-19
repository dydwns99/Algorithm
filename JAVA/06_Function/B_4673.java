import java.util.*;

public class B_4673 {
    public static void main(String[] args) {
        for (int n = 1; n < 10000; n++) {
            func fc = new func(n);
            int output = fc.selfnum();
            if (output != 0) {
                System.out.println(output);
            }

        }
    }
}

class func {
    private int num;
    public func(int a) {
        this.num = a;
    }

    public int selfnum() {
        int sn=0;
        for (int a = 0; a < 10; a++) {
            for (int b = 0; b < 10; b++) {
                for (int c = 0; c < 10; c++) {
                    for (int d = 0; d < 10; d++) {
                        if (num == 1001 * a + 101 * b + 11 * c + 2 * d) {
                            return 0;
                        } else if (num != 1001 * a + 101 * b + 11 * c + 2 * d && a == 9 && b == 9 && c == 9 && d == 9) {
                            sn = num;
                        }
                    }
                }

            }
        }
        return sn;
    }
}