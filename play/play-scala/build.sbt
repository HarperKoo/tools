name := """play-scala"""

version := "1.0-SNAPSHOT"

lazy val root = (project in file(".")).enablePlugins(PlayScala)

scalaVersion := "2.11.8"

libraryDependencies += jdbc
libraryDependencies += cache
libraryDependencies += ws
libraryDependencies += "org.scalatestplus.play" %% "scalatestplus-play" % "1.5.1" % Test
libraryDependencies += "com.typesafe.play" % "play-ws_2.11" % "2.5.10"
libraryDependencies += "net.debasishg" %% "redisclient" % "3.1"
libraryDependencies += "mysql" % "mysql-connector-java" % "5.1.36"