import scala.io.Source
//import scala.collection.mutable.HashMap
import scala.collection.mutable.Map
import scala.collection.JavaConversions.mapAsScalaMap
import java.util.TreeMap

val source = Source.fromFile("news.txt").mkString
val tokens = source.split("\\s+")
val map:Map[String,Int] = new TreeMap[String,Int]
for (key <- tokens){
	map(key) = map.getOrElse(key,0)+1
}
println(map.mkString(","))

