sum = 0;  
FOR (i = 1; i <= 100; i++) {  		
    prime_Num = true;  		// Assume the number is prime
    IF (i == 1) {  
        prime_Num = false;  		// 1 is not a prime number
    }
    FOR (j = 2; j <= sqrt(i); j++) {  	// Loop through numbers from 2 to the square root of i
        IF (i % j == 0) { 			 
            prime_Num = false;  		// If divisible, i is not a prime number
            BREAK;  
        }
    }
    IF (prime_Num == true) { 
        sum = sum + i;  			// Add i to the sum
        print i, sum;  
    }
}
print sum;  



//
Initialization:

sum = 0;: A variable sum is created to store the total of prime numbers. It is initialized to 0.
Outer Loop:

FOR (i = 1; i <= 100; i++): This loop iterates through numbers from 1 to 100. For each number i, the code checks if it's a prime number.
Prime Number Check:

prime_Num = true;: Initially, assume the current number i is prime.
IF (i == 1) { prime_Num = false; }: 1 is not a prime number, so set prime_Num to false.
FOR (j = 2; j <= sqrt(i); j++): This inner loop checks for divisors of i from 2 up to the square root of i. If a divisor is found, i cannot be prime.
IF (i % j == 0) { prime_Num = false; BREAK; }: If i is divisible by j, it's not prime, so set prime_Num to false and break out of the inner loop.
Prime Number Found:

IF (prime_Num == true) { sum = sum + i; print i, sum; }: If prime_Num is still true after the inner loop, i is a prime number. Add it to the sum and print the prime number and the current sum.
Final Output:

print sum;: Print the total sum of all prime numbers found.
