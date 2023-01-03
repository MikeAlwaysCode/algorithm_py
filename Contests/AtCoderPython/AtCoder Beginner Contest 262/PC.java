import java.util.Scanner;

public class Main {

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr= new int[n];
        for(int i=0; i<n; i++){
            arr[i] = scanner.nextInt();
        }
        
        long match = 0;
        long ans = 0;
        for(int i = 0; i < n; i ++) {
            if(arr[i] == i + 1) {
                match ++;
            } else if(arr[i] > i + 1 && arr[arr[i]-1] == i + 1) {
                ans ++;
            }
        }
        if(match >= 2) {
            ans += match * (match - 1) / 2;
        }
        
        System.out.println(ans);
    }
}
