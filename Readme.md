# Simple Strategy
A simple strategy for crypto arbitrage
## Run
* Market data aggregator gather data from multiple exchanges and combine them into one single message based on time. To run the subscriber to receive market data from okx and huobi:``java -jar subscriber-simple-1.0.jar``<br>
* Note that `java --version` should be 11. Rabbitmq is required. <br>
*  The source code of the of the jar is available at `https://github.com/Daniel-YH-Cai/cryptows`
## Market Data
After the Market data aggregator is started, it will push data in the following format:
```
{
  "huobi":{
    "bids":[[31405.1,0.006487],[31405.0,0.003776],[31404.4,0.048004],[31403.9,0.186597],[31403.7,2.0E-4],[31402.1,9.55E-4],[31400.8,0.287189],[31400.5,0.017107],[31400.0,0.020921],[31399.9,1.371788],[31398.9,0.025],[31397.7,0.015857],[31397.1,0.04],[31396.1,0.445874],[31395.5,0.16],[31395.4,0.2],[31394.5,0.025],[31394.3,0.560915],[31394.0,0.005172],[31393.9,0.162]],
    "asks":[[31405.2,2.841508],[31405.3,0.765607],[31405.8,6.008878],[31406.4,0.002268],[31406.6,4.505879],[31406.8,0.159556],[31407.1,0.003865],[31407.6,0.318739],[31407.7,0.010531],[31407.8,0.16],[31407.9,0.064],[31408.4,0.44],[31408.7,1.298485],[31408.9,0.05],[31409.1,0.05],[31409.4,0.235643],[31409.5,0.328256],[31409.7,0.162],[31409.9,0.002646],[31410.0,3.12811]],
    "version":155918469134,
    "ts":1654507662000
  },
  "okx":{
    "asks":[[31403.7,0.33167356,0,1],[31406.3,0.18248061,0,5],[31408.4,0,0,0],[31416.7,0.1,0,1],[31426.7,0.72206269,0,1],[31444.9,0,0,0],[31449.2,0.3,0,1],[31633.7,0,0,0]],
    "bids":[[31399,0.00007223,0,2],[31397.5,0,0,0],[31397.4,0.00802,0,1],[31397,0,0,0],[31396.9,0.06091,0,4],[31349.6,0.02057377,0,1],[31342.5,0,0,0],[31338.9,2.19031338,0,1],[31173.3,0.00133702,0,2],[31173.1,0,0,0]],
    "ts":"1654507662520"
    }
}
```
Here `"ts"` is the timestamp of the ticker in milliseconds (not the time when the message was received or sent by server).
In this example, the timestamp of huobi and okx differs by 500ms. Part of the reason is system latency. Moreover, huobi and okx push data at different rates which might also lead to timestamp misalignment.

