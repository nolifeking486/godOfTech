## Class Layout

The contents of a class should go in the following order:

1. Property declarations and initializer blocks
2. Secondary constructors
3. Method declarations
4. Companion object

* **Logical Ordering:** Do not sort the method declarations alphabetically or by visibility, and do not separate regular methods from extension methods. Instead, put related stuff together, so that someone reading the class from top to bottom can follow the logic of what's happening. Choose an order (either higher-level stuff first, or vice versa) and stick to it.
* **Nested Classes:** Put nested classes next to the code that uses those classes. If the classes are intended to be used externally and aren't referenced inside the class, put them at the end, after the companion object.




```kotlin
class UserProfile(val userId: String) {
	// 1. Properties & Init blocks (The data it holds)
	var name: String = ""
	init {
		println("User created!")
	}

	// 2. Secondary Constructors (Alternative ways to build this object)
	constructor(userId: String, name: String) : this(userId) {
		this.name = name
	}

	// 3. Methods/Functions (What this class DOES)
	fun login() { ... }
	fun logout() { ... }

	// 4. Companion Object (Static stuff / factory functions)
	companion object {
		fun createGuestUser(): UserProfile = UserProfile("guest")
	}
}
```

## Interface Implementation Layout

When implementing an interface, keep the implementing members in the same order as members of the interface (if necessary, interspersed with additional private methods used for the implementation).


## Overload Layout

Always put overloads next to each other in a class.


```kotlin
// GOOD: Overloads grouped together
fun printData(text: String) { ... }
fun printData(number: Int) { ... } // Placed right below!

// BAD: Separated overloads make code hard to read
fun printData(text: String) { ... }
fun doSomethingElse() { ... }
fun printData(number: Int) { ... } // Confusing!
```

## Naming Rules

* **Package:** lower case, if multi-word then lower camel case
* **Classes and Objects:** upper camel case
* **Functions,Properties,Local Variables:** lower camel case



```kotlin

```
