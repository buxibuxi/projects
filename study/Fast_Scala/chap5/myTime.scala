class myTime(val h:Int, val m:Int){
private var hours = h
private var minutes = m
def checkTime {
	println(hours.toString + " : "+minutes.toString)
	}
def before(other:myTime):Boolean = {
	other match {
	case _ if (other.hours < hours) => true
	case _ if (other.hours == hours && other.minutes < minutes) => true 
	case _ => false
	}
	}
} 

