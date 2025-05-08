# Java Final Exam - 80 Questions with Answers

## Java Basics

1. Answer: public static void main(String[] args)
   Question: What is the correct signature for the main method in Java?

2. Answer: String
   Question: Which data type should be used to store text in Java?

3. Answer: double
   Question: What primitive data type in Java is commonly used to store decimal numbers?

4. Answer: ==
   Question: Which operator is used to compare two values for equality in Java?

5. Answer: final
   Question: Which keyword is used to declare a constant in Java?

6. Answer: break
   Question: What statement is used to exit a loop prematurely in Java?

7. Answer: .length()
   Question: How do you find the length of a String in Java?

8. Answer: Integer.parseInt()
   Question: Which method is used to convert a String to an int in Java?

9. Answer: &&
   Question: What is the logical AND operator in Java?

10. Answer: arr.length
    Question: How do you get the length of an array named 'arr' in Java?

## Java Methods

11. Answer: Method overloading
    Question: What is it called when a class has multiple methods with the same name but different parameters?

12. Answer: return
    Question: Which keyword is used to specify the value a method should return?

13. Answer: static
    Question: What keyword allows a method to be called without creating an instance of the class?

14. Answer: It's called recursively until a base case is reached
    Question: How does a recursive method typically work?

15. Answer: public, protected, default (package-private), private
    Question: List the four access modifiers in Java from most to least restrictive.

## Java Classes

16. Answer: A blueprint for creating objects
    Question: In object-oriented programming, what is a class?

17. Answer: new
    Question: Which keyword is used to create an instance of a class?

18. Answer: super()
    Question: What method call is used to invoke a superclass constructor?

19. Answer: To hide the internal details of how an object functions
    Question: What is the main purpose of encapsulation in Java?

20. Answer: extends
    Question: Which keyword is used to define a subclass in Java?

21. Answer: An object can be treated as an instance of its superclass
    Question: What is the principle of polymorphism in Java?

22. Answer: private
    Question: Which access modifier should be used for encapsulating class attributes?

23. Answer: To define a class within another class
    Question: What is the purpose of inner classes in Java?

24. Answer: abstract
    Question: Which keyword is used to declare a method that has no body?

## Java Advanced Topics

25. Answer: interface
    Question: What keyword is used to define a completely abstract class in Java?

26. Answer: A special class used to define a collection of constants
    Question: What is an Enum in Java?

27. Answer: Scanner
    Question: Which class is commonly used for reading user input in Java?

28. Answer: java.time.LocalDate
    Question: Which class from the Java 8 Date and Time API represents a date without time?

29. Answer: An ordered collection that allows duplicate elements
    Question: What is an ArrayList in Java?

30. Answer: O(1)
    Question: What is the time complexity for adding an element to the end of an ArrayList?

31. Answer: Collections.sort()
    Question: Which method can be used to sort a List in Java?

32. Answer: A collection that stores key-value pairs
    Question: What is a HashMap in Java?

33. Answer: To remove elements from a collection while iterating
    Question: What is the primary use of an Iterator in Java?

34. Answer: try, catch, finally
    Question: What are the three main blocks used in exception handling in Java?

35. Answer: ^[a-zA-Z0-9_]+$
    Question: Write a regular expression that matches alphanumeric strings including underscores.

36. Answer: implements Runnable
    Question: How can a class be made into a thread without extending the Thread class?

37. Answer: (parameters) -> expression
    Question: What is the general syntax for a lambda expression in Java?

## Java File Handling

38. Answer: FileWriter
    Question: Which class is commonly used for writing text files in Java?

39. Answer: new File("filename.txt")
    Question: How do you create a new File object in Java?

40. Answer: FileReader
    Question: Which class is used for reading character files in Java?

41. Answer: file.delete()
    Question: How do you delete a file in Java using the File class?

42. Answer: try-with-resources
    Question: What feature in Java ensures that a resource is closed after the try block finishes?

## More Advanced Java Concepts

43. Answer: To allow multiple inheritance of type
    Question: What is the main purpose of interfaces in Java?

44. Answer: volatile
    Question: Which keyword in Java is used to indicate that a variable's value may be modified by multiple threads?

45. Answer: synchronized
    Question: What keyword is used to make a method thread-safe in Java?

46. Answer: It doesn't allow null keys or values
    Question: How does a Hashtable differ from a HashMap in Java?

47. Answer: Generics
    Question: What feature in Java allows you to write code that can work with different types while providing compile-time type safety?

48. Answer: Thread.sleep()
    Question: Which method is used to pause the execution of a thread for a specified time?

49. Answer: To create immutable objects
    Question: What is the main use of the 'final' keyword when applied to a class?

50. Answer: Inheritance, Encapsulation, Polymorphism, Abstraction
    Question: List the four main principles of Object-Oriented Programming.

## Java 8+ Features

51. Answer: A way to add new methods to interfaces with a default implementation
    Question: What are default methods in Java interfaces?

52. Answer: To perform operations on elements of a stream
    Question: What is the purpose of the Stream API in Java?

53. Answer: Optional
    Question: Which class introduced in Java 8 is used to handle null values more gracefully?

54. Answer: A function that takes another function as an argument or returns a function
    Question: What is a higher-order function in Java?

55. Answer: Method reference
    Question: What is the :: operator used for in Java 8?

## Java Design Patterns

56. Answer: Singleton
    Question: Which design pattern ensures a class has only one instance and provides a global point of access to it?

57. Answer: Factory Method
    Question: Which design pattern defines an interface for creating an object, but lets subclasses decide which class to instantiate?

58. Answer: Observer
    Question: Which design pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically?

59. Answer: Decorator
    Question: Which design pattern attaches additional responsibilities to an object dynamically?

60. Answer: Model-View-Controller (MVC)
    Question: Which architectural pattern separates an application into three main components: Model, View, and Controller?

## Java Memory Management

61. Answer: Garbage Collection
    Question: What is the automatic memory management system in Java called?

62. Answer: OutOfMemoryError
    Question: What error is thrown when the Java Virtual Machine cannot allocate an object due to lack of memory?

63. Answer: To suggest that the garbage collector should run
    Question: What is the purpose of the System.gc() method in Java?

64. Answer: Strong, Soft, Weak, Phantom
    Question: List the four types of references in Java, from strongest to weakest.

## Java Testing

65. Answer: JUnit
    Question: What is the most widely used testing framework for Java?

66. Answer: To verify that a certain condition is true
    Question: What is the purpose of assertions in Java testing?

67. Answer: @Test
    Question: Which annotation is used to mark a method as a test method in JUnit?

68. Answer: To run setup code before each test method
    Question: What is the purpose of the @Before annotation in JUnit?

## Java Build Tools and Dependency Management

69. Answer: Maven
    Question: Which popular build automation tool for Java projects uses a pom.xml file for configuration?

70. Answer: To manage and download project dependencies
    Question: What is the primary purpose of Gradle in Java projects?

## Java Web Development

71. Answer: Servlet
    Question: What is the core component for creating web applications in Java?

72. Answer: Java Server Pages (JSP)
    Question: Which technology allows you to create dynamically generated web pages based on HTML, XML, or other document types?

73. Answer: To map URLs to specific handlers or controllers
    Question: What is the purpose of the @RequestMapping annotation in Spring MVC?

74. Answer: To inject dependencies automatically
    Question: What is the purpose of the @Autowired annotation in Spring?

## Java Performance

75. Answer: To improve the performance of code that is executed frequently
    Question: What is the purpose of the JIT (Just-In-Time) compiler in Java?

76. Answer: To allow multiple threads to execute concurrently
    Question: What is the purpose of the ForkJoinPool in Java?

77. Answer: A memory leak
    Question: What do you call it when objects are no longer used by an application but the Garbage Collector is unable to remove them from memory?

## Java Security

78. Answer: To restrict the actions that Java code can perform
    Question: What is the purpose of the Security Manager in Java?

79. Answer: To generate a fixed-size hash for any size of input data
    Question: What is the purpose of the MessageDigest class in Java's security API?

80. Answer: SQL Injection
    Question: What type of security vulnerability can occur when user input is not properly sanitized before being used in SQL queries?
