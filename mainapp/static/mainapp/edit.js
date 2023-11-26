function deletethis(arg){
    val=arg.parentElement.parentElement.children[0].children[0].href.split("/").slice(-2);
    console.log(val);
    // alert("Are you sure you want to delete this?"+val[0]+decodeURI(val[1]));
    setRequestHeader();
    $.ajax({
        dataType: 'json',
        type: 'POST',
        url: "/deletedata/",
        data: {
                id: decodeURI(val[1]),
                type: val[0],
        },
        success: function (data) {
            globalThis.data=data;
            
        },
        error: function (jqXHR, textStatus, errorThrown) {
            alert("Error: " + errorThrown);
        }
    });
}