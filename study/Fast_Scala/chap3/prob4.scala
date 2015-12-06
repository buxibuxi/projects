object prob4
{
def main(args:Array[String]) {
    val a = Array(1,-2,3,-4,5);
	a.foreach(println)
	val b = reorder(a);
	b.foreach(println);
}

def reorder(arr: Array[Int]):Array[Int] = {
	val pos =  arr.filter(_ > 0)
	val neg = arr.filter(_ <= 0)
	pos ++ neg
	}
}
