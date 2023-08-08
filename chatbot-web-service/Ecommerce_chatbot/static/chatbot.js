const chatbot = document.getElementById('chatbot');
const conversation = document.getElementById('conversation');
const inputForm = document.getElementById('input-form');
const inputField = document.getElementById('input-field');

inputForm.addEventListener('submit', function(event) {

  event.preventDefault();

  const input = inputField.value;

  const currentTime = new Date().toLocaleTimeString([], { hour: '2-digit', minute: "2-digit" });

  let message = document.createElement('div');
  message.classList.add('chatbot-message', 'user-message');
  message.innerHTML = `<p class="chatbot-text" id="text-user" sentTime="${currentTime}">${input}</p>`;
  conversation.appendChild(message);

  fetch('/chatbot', {
    method: 'POST',
    body: JSON.stringify({inputValue: input}),
    headers: {
      'Content-Type' : 'application/json'
    }
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);
    console.log(Object.keys(data).length);
    if(Object.keys(data).length==2){
        const response = data.message_response1;
        console.log(response);
        message = document.createElement('div');
        message.classList.add('chatbot-message','chatbot');
        
        message.innerHTML = '<img src="../static/img/chatbot.png" alt="chatbot_icon" id="chatbot_icon" >'+`<p class="chatbot-text" id="text-chatbot" sentTime="${currentTime}">${response}</p>`;        
        conversation.appendChild(message);
        message.scrollIntoView({behavior: "smooth"});
      
        const response2 = data.message_response2;
        console.log(response2);
        message = document.createElement('div');
        message.classList.add('chatbot-message','chatbot', 'second-message');
        message.innerHTML = `<p class="chatbot-text" id="text-chatbot" sentTime="${currentTime}">${response2}</p>`;
        conversation.appendChild(message);
        message.scrollIntoView({behavior: "smooth"});
    }
        
    else{
        const response = data.message_response1;
        console.log(response);
        message = document.createElement('div');
        message.classList.add('chatbot-message','chatbot');
        message.innerHTML = '<img src="../static/img/chatbot.png" alt="chatbot_icon" id="chatbot_icon" >'+`<p class="chatbot-text" id="text-chatbot" sentTime="${currentTime}">${response}</p>`;
        conversation.appendChild(message);
        message.scrollIntoView({behavior: "smooth"});
    }
    
  })
  .catch(error => {
    console.error(error);
  })
    
  inputField.value='';
});