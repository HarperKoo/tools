package controllers

import javax.inject._

import play.api.libs.json.{JsValue, Json}
import play.api.libs.ws.WSClient
import play.api.mvc._
import play.api.db._

import scala.concurrent.Await
import scala.concurrent.duration._
import akka.stream.Materializer
import com.redis.{RedisClient, RedisClientPool}

import scala.concurrent.ExecutionContext.Implicits.global

/**
 * This controller creates an `Action` to handle HTTP requests to the
 * application's home page.

 */
@Singleton
class HomeController @Inject() (ws: WSClient,configuration: play.api.Configuration,db: Database)
                               (implicit val materializer: Materializer)extends Controller {

  /**
   * Create an Action to render an HTML page with a welcome message.
   * The configuration in the `routes` file means that this method
   * will be called when the application receives a `GET` request with
   * a path of `/`.
   */
  /** !!! This is a example of reading from a url*/

  def index = Action {
    val f = getWorkers
//    Ok(views.html.index("Your new application is ready."))
    val r = getRoutes
    Ok(r.toString())
  }
  private def getWorkers = {
    val url = "http://10.213.96.210/getWorker?campid=39&date=2016-11-11"
    getFromUrl(url)
  }

  private def getRoutes = {
    val url  = "http://10.213.96.210/getRoute?worker=11249&date=2016-11-11"
    val routes:JsValue = getFromUrl(url)
    val lat = (routes \ "route0" ).get
    lat
  }

  private def getFromUrl(url: String) = {
    val response = ws.url(url).stream().flatMap {
      res => res.body.runFold(List[String]()) { (ss, b) => ss :+ b.decodeString("UTF-8") }
    }
    val body: List[String] = Await.result(response, 60.seconds)
    Json.parse(body.mkString(""))
  }

  /**This is a example of getting data from local redis*/
  val redisHostIP:String = configuration.getString("redisHostIP").getOrElse("localhost")
  val r = new RedisClient(redisHostIP, 6379)
  val rClients = new RedisClientPool(redisHostIP, 6379)
  def getredis = Action {
    Ok(getRedisValue("126.9758_36.8920:126.7134_37.5245"))
  }
  private def getRedisValue(pair:String):String = {
    rClients.withClient{
      client => {
        client.select(2)
        client.get(pair).get.toString
      }
    }
  }

  /**This is a example of getting data from remote mysql*/

  def getmysql = Action {
    var outString = "Output is : "
    val conn = db.getConnection()

    try {
      val stmt = conn.createStatement
      val rs = stmt.executeQuery("SELECT DATE,TYPE,CODE,ENGLISH_NAME,CAR_TYPE,SIZE FROM Delivery.truck where date = '2017-01-15'; ")

      while (rs.next()) {
        outString += rs.getString("ENGLISH_NAME")
      }
    } finally {
      conn.close()
    }
    Ok(outString)
  }

}