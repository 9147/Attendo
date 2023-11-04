selected_choice = "1";
selcted_class={"1":"present","2":"absent"};
function selectOne(args){
    e=args.parentElement;
    i=0;
    while(i< e.children.length){
        e.children[i].classList.remove('selected_choice');
        i++;
    }
    args.classList.add('selected_choice');
    selected_choice = args.id;
}

function updateData(args){
    var sections=document.getElementsByClassName("box_"+args.id);
    if(args.checked){
        for(i=0;i<sections.length;i++){
        sections[i].classList.remove('hide');
        }
    }else{
        for(i=0;i<sections.length;i++){
            sections[i].classList.add('hide');
            }
    }
}

function mark(arg){
    arg.classList.remove("present");
    arg.classList.remove("absent");
    arg.classList.add(selcted_class[selected_choice])
}

function allAbsent(){
    var sections=document.getElementsByClassName("present");
    for(i=0;i<sections.length;){
        sections[i].classList.remove('present');
    }
    var sections=document.getElementsByClassName("box");
    for(i=0;i<sections.length;i++){
        sections[i].classList.add('absent');
    }
}
function allPresent(){
    var sections=document.getElementsByClassName("absent");
    for(i=0;i<sections.length;){
        sections[i].classList.remove('absent');
    }
    var sections=document.getElementsByClassName("box");
    for(i=0;i<sections.length;i++){
        sections[i].classList.add('present');
    }
}

function sendAttendance(arg){
    var present_list = document.getElementsByClassName("present");
    var absent_list = document.getElementsByClassName("absent");
    var data={};
    for(i=0;i<present_list.length;i++){
        data[present_list[i].children[0].innerHTML] = "P";
    }
    for(i=0;i<absent_list.length;i++){
        data[absent_list[i].children[0].innerHTML] = "A";
    }
    console.log(data);

    setRequestHeader();

    $.ajax({
        dataType: 'json',
        type: 'POST',
        url: "/attendance/"+arg,
        data: data,
        success: function (data) {
            console.log("Success:", data);
            window.location.href = "../../";
        },
        error: function (jqXHR, textStatus, errorThrown) {
            alert("Error:", jqXHR.responseText);

        }
    });
}