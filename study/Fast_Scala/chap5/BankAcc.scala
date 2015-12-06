class BankAcc{
	private var balance = 0
	def deposit(v:Int){ balance += v }
	def withdraw(v:Int) {balance -= v }
	def current() = balance
}
