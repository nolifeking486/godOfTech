## Variables
* **val** : immutable, read-only local variables
* **var** : mutable

**Note -> Nullable type:**
By default variables are not null in kotlin -> suffix with '?' to allow null values


```kotlin
val languageName: String? = null
```

## Data Types

### Integer Types

| Type | Size (bits) | Min value | Max value |
|---|---|---|---|
| Byte | 8 | -128 | 127 |
| Short | 16 | -32768 | 32767 |
| Int | 32 | -2,147,483,648 (-2^31) | 2,147,483,647 (2^31 - 1) |
| Long | 64 | -9,223,372,036,854,775,808 (-2^63) | 9,223,372,036,854,775,807 (2^63 - 1) |



```kotlin
// Use underscores to improve readability
val oneBillion: Long = 1_000_000_000
val hexBytes: Int = 0x7F_EC_DE_5E
val bytes: Int = 0b01010010_01101001_10010100_10010010

//nullable
val maybeAbsent: Int? = null
```

### Floating Point Types

| Type | Size (bits) | Significant bits | Exponent bits | Decimal digits |
|---|---|---|---|---|
| Float | 32 | 24 | 8 | 6-7 |
| Double | 64 | 53 | 11 | 15-16 |

By default double is inferred, use 'f' at end to infer as float


```kotlin
val pi = 3.14 // Double
val eFloat = 2.7182817f // Float
val maybeAbsent: Double? = null
```

### Unsigned Integer Types

| Type | Size (bits) | Min value | Max value |
|---|---|---|---|
| UByte | 8 | 0 | 255 |
| UShort | 16 | 0 | 65,535 |
| UInt | 32 | 0 | 4,294,967,295 (2^32 - 1) |
| ULong | 64 | 0 | 18,446,744,073,709,551,615 (2^64 - 1) |



```kotlin
val a1 = 42u // UInt: no expected type provided, constant fits in UInt
val a2 = 0xFFFF_FFFF_FFFFu // ULong: no expected type provided, constant doesn't fit in UInt
val a = 1UL // ULong, even though no expected type provided and the constant fits into UInt
```

### Char
* uses UTF16
*


```kotlin
val letter: Char = 'a'
// Kotlin infers Char because the values are written in single quotes
val digit = '1'

val invalid = 'AB' // Error coz multi char single quotes
val invalidEmpty = '' // Error coz empty
val maybeAbsent: Char? = null

//using Unicode
val unicodeNumber = '\u0031' // Equals '1'
```
