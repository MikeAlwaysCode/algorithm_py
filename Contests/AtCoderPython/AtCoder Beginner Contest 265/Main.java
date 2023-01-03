import java.util.Scanner;

public class Main {

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int p = scanner.nextInt();
        int q = scanner.nextInt();
        int r = scanner.nextInt();
        int[] arr= new int[n];
        for(int i=0; i<n; i++){
            arr[i] = scanner.nextInt();
        }
        
        int[] cnt = new int[n+1];
        int tot = 0;
        for(int i=0; i<n; i++){
            tot += arr[i];
            cnt[i+1] = tot;
        }

        boolean chk = false;

        int i = 0, j = 1;
        
        while(j < n - 1) {
            while(j < n - 1 && cnt[j] - cnt[i] != p) {
                if(cnt[j] - cnt[i] > p && i < j) {
                    i += 1;
                } else {
                    j += 1;
                }
            }
            if(j >= n - 1 || cnt[j] - cnt[i] != p) {
                break;
            }
            
            int k = j + 1;
            while(k < n && cnt[k] - cnt[j] < q) {
                k += 1;
            }
            
            if(k >= n || cnt[k] - cnt[j] != q) {
                i += 1;
                j += 1;
                continue;
            }

            int l = k + 1;
            while(l <= n && cnt[l] - cnt[k] < r) {
                l += 1;
            }

            if(l <= n && cnt[l] - cnt[k] == r) {
                chk = true;
                break;
            } else {
                i += 1;
                j += 1;
            }
        }
        if(chk) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
        scanner.close();
    }
}
