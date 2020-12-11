<script>
      var socket = new WebSocket("wss://www.blockonomics.co/payment/"+ "{{addr}}");
      socket.onmessage = function(event){
        response = JSON.parse(event.data);
        console.log(response);
        //This condition ensures that we reload only when we get a 
        //new payment status and don't go into a loop
          if (response.status > '{{invoice_status}}')
          setTimeout(function(){window.location.reload() }, 1000); 
        
      }
      
      {/* The current location (invoice page) is reload only upon websocket //notification of payment.There is timeout to let the invoice status //update on server via HTTP callback */}
</script>