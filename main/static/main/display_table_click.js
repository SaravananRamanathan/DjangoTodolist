
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
} 
   $('.todolist-item-delete').click(function(){
        id=$(this).data("todolist-item-id");
        //alert("testing ok. todolist-item delete button clicked, id: "+id); //-- test was ok.
        const csrftoken = getCookie('csrftoken');
            $.ajax({
                url: '/delete-todolist-item/',
                type: "POST",
                data: {
                    id:id
                },
                beforeSend: function (xhr) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                },
                success: function (data) {
                    console.log(data);
                    location.reload(true)
                },
                error: function (error) {
                    console.log(error);
                }
            });
    });
    $('#display-table > tbody > tr').click(function() {
        //alert("you are being redirected to id: "+$(this).data("display-table-id"))
        //window.location =("/id/"+$(this).data("display-table-id"));
        //alert("testing id : "+$(this).data("display-table-id"));
        if($(this).data("display-table-id")){
            //alert("testing display id");
            $('.dataid'+$(this).data("display-table-id")).collapse('toggle');
        }
        else if($(this).data("show-id")){
            window.location =("/id/"+$(this).data("show-id"));
            //alert("show clicked: "+$(this).data("show-id"));
        }
        else if($(this).data("delete-id")){
            
            
            
            id=$(this).data("delete-id");
            //alert("delete clicked: "+id); //testing ok.

            const csrftoken = getCookie('csrftoken');
            $.ajax({
                url: '/ajax/',
                type: "POST",
                data: {
                    id:id
                },
                beforeSend: function (xhr) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                },
                success: function (data) {
                    console.log(data);
                    location.reload(true)
                },
                error: function (error) {
                    console.log(error);
                }
            });

        }
        
         
    });
function loginclick(){
    //alert("testing: "+window.location.pathname);
    if(window.location.pathname == "/login/"){
        alert("you are already at login page.")
    }
    else    window.location = "/login"
}
function logoutclick(){
    window.location = "/logout"
}

window.setTimeout(function() {
    $(".alert").fadeTo(500, 0).slideUp(500, function(){
        $(this).remove();
    });
    }, 5000);

   /* $('.loginclick').click(function(){
        alert("log in clicked"); //-- test was ok.
        
    });
*/