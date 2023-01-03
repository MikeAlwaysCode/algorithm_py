import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;
import java.util.function.IntUnaryOperator;
import java.util.function.LongUnaryOperator;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class B_Also_Try_Minecraft {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int m = scn.nextInt();
        int [] arr = new int [n];
        for(int i=0; i < n; i++) {
            arr[i] = scn.nextInt();
        }
        for(int i=0; i < m; i++) {
            int s = scn.nextInt();
            int t = scn.nextInt();
            int step = s < t ? 1:-1;
            int d = 0;
            int j = s-1;
            while(j!=t-1) {
                d += Math.max(arr[j] - arr[j+step], 0);
                j += step;
            }
            System.out.println(d);
        }
    }
}
