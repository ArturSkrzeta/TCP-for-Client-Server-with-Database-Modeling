<h2>TCP for Client->Server+Database Modeling</h2>
<p>TCP is the common transport protocol that ensures reliable exchange of data betwen connected programms accross the network.</p>
<p>In the repo, I medel the connection: client - server - database. Data exchange between client and server will be performed with TCP. Server saves client's data in the databse.</p>
<img src="images/tcp.gif">
<h3>Networking</h3>
<ul>
  <li>Networking is a concept of communication between two entities/programms across the network:</li>
      - client to client <br>
      - client to server <br>
      - client to itself
  <li>Where client is an end device usually interfacing with a human.</li>
  <li>Server on the other hand is a device providing a service for a client</li>
</ul>

<h3>Client - Server Model</h3>
<ul>
  <li>Server can run constantly and be available for clients to connect to at any time to receive the information clients require.</li>
  <li>Example: web browser as a client conncts Google as a server.</li>
  <li>All computers connected to a network should have IP address: 127.0.0.1</li>
  <li>Port number - slots for network card. Ports reroute the incoming data to appropriate program.</li>
</ul>

<h3>Peer-to-Peer model</h3>
<ul>
  <li>Server with services don't have to be constantluy available.</li>
  <li>Clients connect to other clients with no central server.</li>
  <li>Example: Skype or games servers.</li>
</ul>

<h3>TCP</h3>
<ul>
  <li>Reliable part within the protocol ensures if the data is lost on its course through the network, the prtocol will reorganize the data to be resent</li>
  <li>It also checks if the data is courrpted and arrives in ordered manner.</li>
  <li>The checking slows down the protocol.</li>
  <li>Applied everywhere when we need to be 100% sure the data is being completely delivered: Web Browsers, Emails, FTP...</li>
</ul>

<h3>Sockets</h3>
<ul>
  <li>Programming concept for establishing connection in bidirectional manner from program to program across the network.</li>
  <li>Once they are connected, we can use them to send data and receive data.</li>
  <li>One socket: server.py, another socket: client.py.</li>
  <li><b>Python sockets easily handle the implementation of the common transport protocols: TCP and UDP</b></li>
</ul>

<h3>Insights</h3>
<ul>
  <li>Information passsed through sockets needs to be encoded with utf-8.</li>
</ul>

<h3>SQLite database setup</h3>
<ol>
  <li>Creating a file in project folder: db_name.db.</li>
  <li>Importing sqlite3 in Python script:
    <br>
    > import sqlite3
  </li>
  <li>Conneting to db:
    <br>
    > conn = sqlite3.connect('db_name.db')<br>
    > c = conn.cursor()<br>
  </li>
  <li> Creating table:
    <br>
    > c.execute('CREATE TABLE tblTransactions(id INTEGER PRIMARY KEY AUTOINCREMENT, value TEXT)')
  </li>
  <li> Inserting values:
    <br>
    > c.execute("INSERT INTO tblTransactions VALUES(NULL, '" + row + "')")<br>
    > conn.commit()<br>
  </li>
  <li>Closing db:
    <br>
    > c.close()<br>
    > conn.close()<br>
  </li>
</ol>
