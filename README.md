 # wallaroo-nats-connector
Konektor wallaroo source dan sink untuk nats server

[Wallaroo](https://github.com/wallaroolabs/wallaroo)

Wallaroo adalah suatu framework Stream processing seperti Apache Flink, bedanya Wallaroo menggunakan python untuk menulis logic streamingnya. Engine Wallaroo ditulis dalam pony dan sama sekali tidak bergantung dengan JVM seperti kebanyakan framework stream processing.

[NATS](https://github.com/nats-io/gnatsd)
NATS server adalah PUB-SUB server yang ringan dan berperforma tinggi. NATS memiliki karakteristik fire and forget

Langkah-langkah

1.Install dan jalankan nats server, contoh ini menggunakan flag trace and debug
` ./gnatsd -DV`

2.Install wallaroo dengan petunjuk di [sini](https://docs.wallaroolabs.com/python-installation/python-wallaroo-up-installation-guide/)

3.Jalankan source connector dengan :
`./nats_subscriber_source --application-module pass --connector ingress --ingress-subject test`

disini `test` adalah nats subject dimana sumber data akan didapatkan

4.Jalankan sink connector dengan :
`./nats_publisher_sink --application-module pass --connector egress --egress-subject test2`

dimana test2 adalah subject dimana hasil pengolahan akan di *publish*

5.Jalankan application module tester
Module `pass` disini hanya menjadikan setiap kata menjadi kapital, sekedar untuk menunjukkan fitur konnektor

`machida3 --application-module pass --metrics 127.0.0.1:5001 --control 127.0.0.1:6000 --data 127.0.0.1:6001 --name worker-name --external 127.0.0.1:5050 --cluster-initializer --ponythreads=1 --ponynoblock`

Jangan lupa set PATH dan PYTHONPATH

6.Test dengan [nats-cli](https://github.com/kvartborg/nats-cli)

subscribe output applicaiont dengan `nats test2` lalu publish data dengan `nats test hello
`





 
