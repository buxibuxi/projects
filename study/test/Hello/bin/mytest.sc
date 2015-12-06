import scala.io.Source

object mytest {
  println("Welcome to the Scala worksheet")       //> Welcome to the Scala worksheet
  val x = 1                                       //> x  : Int = 1
  def increase(i: Int) = i + 1                    //> increase: (i: Int)Int
  increase(x)                                     //> res0: Int = 2
	val y =  if (true) 1 else false           //> y  : AnyVal = 1
	assert(x==1)
	x==0 || false                             //> res1: Boolean = false
	val z=0                                   //> z  : Int = 0
	
	val source = Source.fromFile("/Users/luobu/workspace/Hello/src/new.txt","UTF-8")
                                                  //> source  : scala.io.BufferedSource = non-empty iterator
 	val lineIterator = source.getLines        //> lineIterator  : Iterator[String] = non-empty iterator
	for (l <- lineIterator) println(l)        //> hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| 
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| 
                                                  //| 
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| 
                                                  //| 
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| 
                                                  //| 
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| 
                                                  //| 
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| 
                                                  //| 
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| 
                                                  //| 
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| hhh, bbb, ccc
                                                  //| Output exceeds cutoff limit.
}