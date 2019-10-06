
for intellij 
https://www.javadevjournal.com/spring-boot/spring-boot-application-intellij/

for build
https://spring.io/guides/gs/spring-boot-docker/


```
./gradlew build 
java -jar build/libs/eve-0.1.0.jar
```

https://docs.spring.io/spring-boot/docs/current/reference/html/using-boot-running-your-application.html

When developing on Kube docker
-

build on host machine e.g. with IDE (make sure the same java version is used for compilation)
```
./gradlew build 
rm ./build/libs/app.jar
cp ./build/libs/eve-0.0.1-SNAPSHOT.jar ./build/libs/app.jar
```

Run on docker or kube pod
```
java -jar /code_path/build/libs/app.jar

java -Xdebug -Xrunjdwp:server=y,transport=dt_socket,address=8007,suspend=n \
       -jar /code_path/build/libs/app.jar
```

Run on docker from local
```
kubectl exec -it -n wielder-services boot-578856f87b-7c8g4 bash 

java -jar /code_path/build/libs/app.jar ...
```