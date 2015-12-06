import scala.io.Source

object mytest {;import org.scalaide.worksheet.runtime.library.WorksheetSupport._; def main(args: Array[String])=$execute{;$skip(83); 
  println("Welcome to the Scala worksheet");$skip(12); 
  val x = 1;System.out.println("""x  : Int = """ + $show(x ));$skip(31); 
  def increase(i: Int) = i + 1;System.out.println("""increase: (i: Int)Int""");$skip(14); val res$0 = 
  increase(x);System.out.println("""res0: Int = """ + $show(res$0));$skip(33); 
	val y =  if (true) 1 else false;System.out.println("""y  : AnyVal = """ + $show(y ));$skip(14); 
	assert(x==1);$skip(15); val res$1 = 
	x==0 || false;System.out.println("""res1: Boolean = """ + $show(res$1));$skip(9); 
	val z=0;System.out.println("""z  : Int = """ + $show(z ));$skip(84); 
	
	val source = Source.fromFile("/Users/luobu/workspace/Hello/src/new.txt","UTF-8");System.out.println("""source  : scala.io.BufferedSource = """ + $show(source ));$skip(37); 
 	val lineIterator = source.getLines;System.out.println("""lineIterator  : Iterator[String] = """ + $show(lineIterator ));$skip(36); 
	for (l <- lineIterator) println(l)}
}
