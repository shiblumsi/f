console.log("ok")


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
const csrf = getCookie('csrftoken');


$('.like-btn').on('click',function(){
    let id = $(this).attr('post-id')
    console.log(id)
    $.ajax({
        type:'POST',
        url:'/like',
        data:{
            csrfmiddlewaretoken:csrf,
            id:id,
        },
        success:(res)=>{
            console.log(res.ok)
            $(`.lc${id}`).text(res.ok)
        }
    })
})







