selected_subjects={};
$(document).ready(function() {
    $("input[type=number]").on("focus", function() {
      $(this).on("keydown", function(event) {
        if (event.keyCode === 38 || event.keyCode === 40) {
          event.preventDefault();
        }
      });
    });
  });
// move through the sheet using arrow keys
function move(e,arg){
    console.log($('#grid-container>input').index(arg));
    switch (e.keyCode) { 
        case 37: 
            str = 'Left Key pressed!'; 
            break; 
        case 38: 
            str = 'Up Key pressed!'; 
            break; 
        case 39: 
            str = 'Right Key pressed!'; 
            break; 
        case 40: 
            str = 'Down Key pressed!'; 
            break; 
    } 

}

function selectMe(arg){
    if(!arg.classList.contains("selected")){
    if(confirm("Are you sure you want to change what the list belongs to?\nThis might result in loss of some data.")){
    ele=arg.parentElement.children;
    ele[0].classList.remove("selected");
    ele[1].classList.remove("selected");
    arg.classList.add("selected");
    selected=$(arg).index();
    if(selected==0){
        document.getElementById("top-section").style.display="none";
        document.getElementById("bottom-section").style.display="none";
        document.getElementById("top-class-section").style.display="flex";
    }
    if(selected==1){
        document.getElementById("top-section").style.display="flex";
        document.getElementById("bottom-section").style.display="flex";
        document.getElementById("top-class-section").style.display="none";
    }
}}
}


function removeCard(arg){
    // console.log("removing");
    $(arg).remove();
    delete selected_subjects[arg.id];
    $('.remove-card').remove(arg);
    // console.log(arg)
    $('#search').keyup();
    // console.log(selected_subjects);
}


function addCard(arg){
    // console.log("clicked");
    arg.classList.remove('add-card');
    arg.classList.add('remove-card');
    $( arg ).unbind("click");
    arg.onclick=function(){removeCard(arg)};
    $('#added-card').append(arg);
    selected_subjects[arg.id]=arg.innerHTML;
    // console.log(selected_subjects);
}



var data={};
// get data from the server
function getData(){

    setRequestHeader();

    $.ajax({
        dataType: 'json',
        type: 'POST',
        url: "/getdata/",
        data: {
            data: 'class&subject',
        },
        success: function (data) {
            globalThis.data=data;
            
        },
        error: function (jqXHR, textStatus, errorThrown) {
            alert("Error: " + errorThrown);
        }
    });
}

window.onload = getData();

$(".btn").on("click",function(){
    $(".input").toggleClass("inclicked");
    $(".btn").toggleClass("close");
  })

// detect when something is typing in the search bar
function updateOptions(arg){
    let result=[];
    if(arg.value.length>0){
        
        for(i=0;i<globalThis.data.subject.length;i++){
            if(selected_subjects[data.subject[i].sid]==undefined && data.subject[i].partial &&(data.subject[i].name.toLowerCase().trim().includes(arg.value.toLowerCase().trim()) || data.subject[i].sid.toLowerCase().trim().includes(arg.value.toLowerCase().trim()))){
                result.push(data.subject[i]);
            }
        }
        // console.log(result);
    }else{
        for(i=0;i<globalThis.data.subject.length;i++){
            if(data.subject[i].partial && selected_subjects[data.subject[i].sid]==undefined){
                result.push(data.subject[i]);
            }
        
        }
        // console.log(result);
    }
    value="";
    for(i=0;i<result.length;i++){
        value+='<div class="card add-card" id="'+result[i].sid+'" onclick="addCard(this)">'+result[i].name+'</div>';
    }
    $('#card-options')[0].innerHTML=value;
}


function AddNewRow(arg){
    if(arg.value!=""){
        ele=document.createElement('div')
        ele.classList.add("del");
        ele.onclick=function(){DeleteRow(this)};
        ele.innerHTML="&nbsp;-&nbsp;";
        arg.parentElement.appendChild(ele);
        val=['number','text','text']
        for(i=0;i<3;i++){
            ele=document.createElement('input');
            ele.addEventListener('keyup',e=>{move(e,ele)});
            if(i==0){
                ele.onchange=function(){UpdateRow(this)};
            }
            ele.classList.add("element");
            ele.type=val[i];
            arg.parentElement.appendChild(ele);
        }
    }
}

function DeleteRow(arg){
    if(!($(arg).index()+4==arg.parentElement.children.length) && confirm("Are you sure you want to delete this row?") ){
        i=$(arg).index()+1;
        for(j=i;j<i+3;j++){
            // console.log(arg.parentElement.children[i]);
            arg.parentElement.children[i].remove();
        }
        arg.remove();
    }
}

function UpdateRow(arg){
    len=arg.parentElement.children.length;
    i=$(arg).index();
    if(i+3==len){
        // console.log("Adding new row");
        AddNewRow(arg);
    }
    else if($(arg).index()%4==2){
        if(arg.value==""){
            // console.log("Deleting row");
            DeleteRow(arg.parentElement.children[$(arg).index()-1]);
        }
    }
}