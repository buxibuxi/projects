class Person(private val name:String, var age:Int){
def getfirst = name.split("\\W+")(0)
def getlast = name.split("\\W+")(1)
/*
val n = name.split("\\W+")
private var firstName = n(0)
private var lastName = n(1)
def getfirst = firstName
def getlast = lastName
*/


}
