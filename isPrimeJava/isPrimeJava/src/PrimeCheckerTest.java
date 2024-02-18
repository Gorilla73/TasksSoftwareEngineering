import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class PrimeCheckerTest {

    @Test
    public void testIsPrime() {
        assertTrue(PrimeChecker.isPrime(2));
        assertTrue(PrimeChecker.isPrime(17));
        assertTrue(PrimeChecker.isPrime(29));
        assertTrue(PrimeChecker.isPrime(7919));

        assertFalse(PrimeChecker.isPrime(1));
        assertFalse(PrimeChecker.isPrime(4));
        assertFalse(PrimeChecker.isPrime(15));
        assertFalse(PrimeChecker.isPrime(100));
    }
}