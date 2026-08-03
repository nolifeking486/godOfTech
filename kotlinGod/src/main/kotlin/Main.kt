class Solution {
	fun hammingWeight(n: Int): Int {
		var a = 1L
		var b : Long = n.toLong()
		var ans = 0
		while(a<=b){
			if(a and b != 0L){
				ans++
			}
			a = a shl 1
		}
		return ans

	}
}
fun main(){

	var sol = Solution()
	var n = readln().toInt()
	println(sol.hammingWeight(n))
}