#### 命令启动：
1.不加driver参数

  - hub：java -jar selenium-server-standalone-3.141.59.jar -role hub
  - node：java  -jar selenium-server-standalone-3.141.59.jar -role node -hub http://ip:port/grid/register/

2.加driver参数

  - hub：java -jar selenium-server-standalone-3.141.59.jar -role hub
  - node：java -Dwebdriver.chrome.driver="./drivers/chromedriver.exe" -jar selenium-server-standalone-3.141.59.jar -role node -hub http://ip:port/grid/register/
  - node：java -Dwebdriver.chrome.driver="./drivers/chromedriver.exe" -Dwebdriver.gecko.driver="./drivers/geckodriver.exe" -jar selenium-server-standalone-3.141.59.jar -role node -hub "http://ip:port/grid/register/"

##### 配置启动：

- hub: java -jar selenium-server-standalone-3.141.59.jar -role hub -hubConfig hub_config.json
- node: java -jar selenium-server-standalone-3.141.59.jar -role node -nodeConfig node_config.json

#### docker启动

  1.单个启动
  
  - hub：`docker run -d -p 4444:4444 --name selenium-hub selenium/hub`
  - node（Chrome&&Firefox）：
	  - `docker run -d --link selenium-hub:hub selenium/node-chrome`
	  - `docker run -d --link selenium-hub:hub selenium/node-firefox`
  - 停止：docker stop $(docker ps -a -q)， docker rm $(docker ps -a -q)
  
  2.组件启动
  
  - 启动：`docker-compose up -d`
  - 查看：`docker-compose ps`
  - 创建更多：`docker-compose scale chrome=5`
  - 关闭：`docker-compose down`
    
