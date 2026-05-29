// LC 384. Shuffle an Array
import java.util.Random;

public final class Sol {
    private final int[] original;
    private final Random rng;

    public Sol(int[] nums) {
        this.original = nums.clone();
        this.rng = new Random();
    }

    public int[] reset() {
        return original.clone();
    }

    public int[] shuffle() {
        int[] arr = original.clone();
        // Durstenfeld: i descends from n-1 down to 1; nextInt(i + 1) draws
        // uniformly from [0, i] inclusive. The +1 is the entire algorithm.
        for (int i = arr.length - 1; i > 0; i--) {
            int j = rng.nextInt(i + 1);
            int tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
        }
        return arr;
    }
}
