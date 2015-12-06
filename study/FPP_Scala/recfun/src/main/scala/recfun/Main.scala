package recfun
//import common._

object Main {
  def main(args: Array[String]) {
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(pascal(col, row) + " ")
      println()
    }
//    print (pascal(5,5))
    val aa = "hello())((()()())".toList
//    print (balance(aa))
    println (countChange(4,List(1,2)))
    println(countChange(301,List(5,10,20,50,100,200,500)))
  }

  /**
   * Exercise 1
   */
  def pascal(c: Int, r: Int): Int = {
    if (r<0 || c<0 || r<c) throw new  IllegalArgumentException("column and row abnomal!")
    else if (c==0 || c==r || r==0) 1
    else pascal(c,r-1)+pascal(c-1,r-1)
  }

  /**
   * Exercise 2
   */
  def balance(chars: List[Char]): Boolean = {
    def bal(cnt:Int, chars:List[Char]): Boolean = {
      if (chars.isEmpty) cnt==0
      else if(chars.head =='(') bal(cnt+1, chars.tail)
      else if(chars.head ==')') cnt>0 && bal(cnt-1,chars.tail)
      else bal(cnt,chars.tail)
    }
    bal(0,chars)
  }

  /**
   * Exercise 3
   */
  def countChange(money: Int, coins: List[Int]): Int = {
    println("money ="+money )
    println("coins ="+coins)
    if(money == 0) 1
    else if(money <0) 0
    else if (coins.isEmpty) 0
    else countChange(money-coins.head,coins) + countChange(money,coins.tail)
  }
}
