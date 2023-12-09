$(document).ready(function () {


    setInterval(function(){
        if(parseInt($(".notificationCounter").text()) > 0){
            $('#notification_new_message')[0].play();
        }
    }, 5000);

    function fetchNewMessages(){
        var employeeId = {{ request.user.id }}
        $.ajax({
            type    :"GET",
            url     : "{% url 'CSM:newMessagesNotification' %}",
            data    : {'employeeId' : employeeId},
            success : function (data){
                console.log(data);
                if(data.message.length > 0){
                    var counter = data.message.length;
                    $('.newMessages').html(counter);
                    $('.newMessages').removeClass("hidden");
                    lastCheckTime =  new Date().toISOString();
                }else{
                    $('.newMessages').addClass("hidden");
                    $('.newMessages').html(0);                 
                }
            },
            error   : function (xhr, status, error){
                console.error('Error:', error);
            }
        });
    }
    setInterval(fetchNewMessages, 5000);

});