var socket = new WebSocket("wss://www.blockonomics.co/payment/"+ "{{addr}}");
socket.onmessage = function(event){
response = JSON.parse(event.data);
//This condition ensures that we reload only when we get a 
//new payment status and don't go into a loop
    if (response.status > '{{invoice_status}}')
    setTimeout(function(){window.location.reload() }, 1000); 
}

  

