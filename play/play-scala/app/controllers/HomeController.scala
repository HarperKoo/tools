package controllers

import javax.inject._

import play.api.libs.json.{Json}
import play.api.libs.ws.{WSClient}
import play.api.mvc._

import scala.concurrent.{Await}
import scala.concurrent.duration._
import akka.stream.Materializer
import scala.concurrent.ExecutionContext.Implicits.global

/**
 * This controller creates an `Action` to handle HTTP requests to the
 * application's home page.
  * !!! This is a example of reading from a url
 */
@Singleton
class HomeController @Inject() (ws: WSClient)(implicit val materializer: Materializer)extends Controller {

  /**
   * Create an Action to render an HTML page with a welcome message.
   * The configuration in the `routes` file means that this method
   * will be called when the application receives a `GET` request with
   * a path of `/`.
   */
  def index = Action {
    val f = getWorkers
//    Ok(views.html.index("Your new application is ready."))
    Ok(f.toString())
  }
  private def getWorkers = {
    val url = "http://10.213.96.210/getWorker?campid=39&date=2016-11-11"
    val response = ws.url(url).stream().flatMap {
      res => res.body.runFold(List[String]()) { (ss, b) => ss :+ b.decodeString("UTF-8") }
    }
    val body: List[String] = Await.result(response, 60.seconds)
    Json.parse(body.mkString(""))
  }


}
