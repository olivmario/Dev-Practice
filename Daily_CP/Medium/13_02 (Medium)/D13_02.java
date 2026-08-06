import java.util.concurrent.*;

public class D13_02{

    public static void schedule(Runnable f, int n) {
        ScheduledExecutorService scheduler = Executors.newSingleThreadScheduledExecutor();
        scheduler.schedule(() -> {
            f.run();
            scheduler.shutdown();
        }, n, TimeUnit.MILLISECONDS);
    }

    public static void main(String[] args) {
        Runnable f = () -> System.out.println("Executado após delay");
        int n = 2000;
        schedule(f, n);
    }
}
