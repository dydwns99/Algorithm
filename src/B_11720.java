import java.util.Scanner;
public class B_11720 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] array = new int[n];

        String str = sc.next();
        String[] arr = str.split("");

        int sum=0;

        for (int i = 0; i < n; i++) {
            sum += Integer.parseInt(arr[i]);
        }

        System.out.print(sum);
    }
}
