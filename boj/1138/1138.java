import java.util.*;
import java.io.*;

public class Main {
    public static int[] result;
    public static int size;

    public static void main(String[] args) throws IOException {
        BufferedReader buf = new BufferedReader(new InputStreamReader(System.in));

        size = Integer.parseInt(buf.readLine());
        StringTokenizer string = new StringTokenizer(buf.readLine());

        result = new int[size];
        for (int i = 0; i < size; i++) {
            result[i] = Integer.parseInt(string.nextToken());
        }

        Stack<Integer> arr = new Stack<>();
        boolean[] visited = new boolean[size];

        combination(arr, visited);
    }

    public static void combination(Stack<Integer> arr, boolean[] visited) {
        if (arr.size() == size) {
            if (isResult(arr, result)) {
                for (int i = 0; i < size; i++) {
                    System.out.print(arr.get(i) + " ");
                }
                System.out.println();
                return;
            }
            return;
        }

        for (int i = 1; i <= size; i++) {
            if (visited[i - 1]) {
                continue;
            }
            arr.push(i);
            visited[i - 1] = true;

            combination(arr, visited);

            arr.pop();
            visited[i - 1] = false;
        }
    }

    public static boolean isResult(Stack<Integer> arr, int[] result) {
        for (int i = 1; i <= size; i++) {
            int count = 0;
            for (int j = 0; j < size; j++) { // arr.size()까지만 반복
                if (arr.get(j) > i) count++;
                if (arr.get(j)==i) break;
            }

            if (result[i - 1] != count)
            {
                return false;
            }
        }
        return true;
    }
}
