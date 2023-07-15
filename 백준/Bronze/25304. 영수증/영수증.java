import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long X = Long.parseLong(br.readLine());
        long n = Long.parseLong(br.readLine());
        long total = 0;

        for(long i=1;i<=n;i++){
            StringTokenizer st = new StringTokenizer(br.readLine()," ");
            long a = Long.parseLong(st.nextToken());
            long b = Long.parseLong(st.nextToken());
            total += a*b;
        }

        if(X==total){
            System.out.println("Yes");
        }
        else System.out.println("No");
    }
}
