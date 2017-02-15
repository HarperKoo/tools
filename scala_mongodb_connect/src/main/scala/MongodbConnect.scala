import org.mongodb.scala.connection.ClusterSettings
import scala.collection.JavaConverters._
import org.mongodb.scala._


/**
  * Created by harperkoo on 2/10/17.
  * Not working
  */
object MongodbConnect {

  def main(args: Array[String]): Unit = {
    //  // To directly connect to the default server localhost on port 27017
//      val mongoClient: MongoClient = MongoClient()
    //
    //  // Use a Connection String
    //  val mongoClient: MongoClient = MongoClient("mongodb://10.255.11.171")

    // or provide custom MongoClientSettings
    val clusterSettings: ClusterSettings = ClusterSettings.builder().hosts(List(new ServerAddress("127.0.0.1"))
      .asJava).description("Local Server").build()
    val settings: MongoClientSettings = MongoClientSettings.builder().clusterSettings(clusterSettings).build()
    val client: MongoClient = MongoClient(settings)
    val database: MongoDatabase = client.getDatabase("test")
    val collection: MongoCollection[Document] = database.getCollection("test")

    val document: Document = Document("_id" -> 1, "x" -> 1)
    val insertObservable: Observable[Completed] = collection.insertOne(document)

    insertObservable.subscribe(new Observer[Completed] {
      override def onNext(result: Completed): Unit = println(s"onNext: $result")
      override def onError(e: Throwable): Unit = println(s"onError: $e")
      override def onComplete(): Unit = println("onComplete")
    })

  }
}
