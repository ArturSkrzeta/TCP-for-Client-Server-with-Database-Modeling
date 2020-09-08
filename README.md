<h2>TCP for Client Server Modeling</h2>
<p>TCP is the common transport protocol that ensures reliable exchange of data betwen connected programms accross the network.</p>
<p>In the repo, I medel the connection: client - server. Data exchange between client and server will be performed with TCP.</p>

<h3>Networking</h3>
<ul>
  <li>Networking is a concept of communication between two entities/programms across the network:</li>
      <ul>
         <li>client to client</li>
         <li>client to server</li>
         <li>client to itself</li>
      </ul>
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
<h3>Sockets</h3>
<ul>
  <li>Programming concept for establishing connection in bidirectional manner from program to program across the network.</li>
  <li>Once they are connected, we can use them to send data and receive data.</li>
  <li><b>Python sockets easily handle the implementation of the common transport protocols: TCP and UDP</b></li>
</ul>

