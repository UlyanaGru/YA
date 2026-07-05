import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class BicycleRental {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
        /*
        Пример ввода и вывода числа n, где -10^9 < n < 10^9:
        int n = Integer.parseInt(reader.readLine());
        writer.write(String.valueOf(n));
        */
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        int N = Integer.parseInt(tokenizer.nextToken());
        int T = Integer.parseInt(tokenizer.nextToken());

        long[] diffArray = new long[T + 1];

        for (int i = 0; i < N; i++) {
            tokenizer = new StringTokenizer(reader.readLine());
            int a = Integer.parseInt(tokenizer.nextToken());
            int f = Integer.parseInt(tokenizer.nextToken());
            long s = Long.parseLong(tokenizer.nextToken());

            if (a <= T) diffArray[a] += s;
            if (f <= T) diffArray[f] -= s;
        }

        long peak = 0;
        long currentBikes = 0;

        for (int time = 0; time <= T; time++) {
            currentBikes += diffArray[time];
            if (currentBikes > peak) {
                peak = currentBikes;
            }
        }

        writer.write(String.valueOf(peak));

        reader.close();
        writer.close();
    }
}