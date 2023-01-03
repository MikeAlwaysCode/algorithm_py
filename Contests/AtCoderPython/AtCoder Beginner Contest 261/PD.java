import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt(), m = scanner.nextInt();
        int[] x = new int[n];
        int[] bonus = new int[n+1];

        for(int i=0; i<n; i++){
            x[i] = scanner.nextInt();
        }
        for(int i=0; i<m; i++){
            int c = scanner.nextInt(), y = scanner.nextInt();
            bonus[c] = y;
        }

        long[] dp = new long[n+1];
        long res = 0;
        for(int i=1; i<=n; i++){
            long[] dp1 = new long[n+1];
            dp1[0] = res;
            for(int j=1; j<=i; j++){
                dp1[j] = dp[j-1]+x[i-1]+bonus[j];
                res = Math.max(res, dp1[j]);
            }
            dp = dp1;
        }
        System.out.println(res);
    }
}
