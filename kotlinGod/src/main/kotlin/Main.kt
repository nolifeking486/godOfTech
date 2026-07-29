import kotlin.math.abs

class Solution {
	fun isUgly(n: Int): Boolean {
		var t = abs(n)

		while (t % 5 == 0 && t != 0) {
			t /= 5;
		}
		while (t % 3 == 0 && t != 0) {
			t /= 3;
		}
		while (t % 2 == 0 && t != 0) {
			t /= 2;
		}
		if (t == 1) {
			return true
		}
		return false;

	}
}

fun main() {
	var solution = Solution()
	var n = readln().toInt()
	println(solution.isUgly(n))
}