class myCounter
{
	private var value = Int.MaxValue
	def increment(){
		value = if(value < Int.MaxValue) value+1 else value
	}
	def current() = value
}

val myCnt =  new myCounter
myCnt.increment()
println(myCnt.current)

