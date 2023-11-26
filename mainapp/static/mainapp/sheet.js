var input_count=7;
selected_subjects={};
checkList();
// check the kind of list
function getsheet(){
    document.getElementById("upload_block").style.display="flex";
}


function dropHandler(ev) {
    // console.log("File(s) dropped");
    
    // Prevent default behavior (Prevent file from being opened)
    document.getElementById("upload_block").classList.remove("active-drop");
    document.getElementById("text_drop").innerHTML="Drag and drop the file here";
    ev.preventDefault();
    file=ev.dataTransfer.files[0]
    if(file.type=="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"){
        console.log(file);
        document.getElementById("upload_block").style.display="none";
        var reader = new FileReader();
        console.log(reader);
        reader.onload = function(e) {
            var data = new Uint8Array(e.target.result);
            var workbook = XLSX.read(data, { type: 'array' });
    
            var sheetName = workbook.SheetNames[0];
            var sheet = workbook.Sheets[sheetName];
    
            var jsonData = XLSX.utils.sheet_to_json(sheet, { header: 1 });
    
            // Extract only the first 3 columns (assuming 3 columns exist)
            var extractedData = jsonData.map(function(row) {
              return row.slice(0, 3); // Extract the first 3 elements (columns)
            });
    
            extractedData.forEach(function(row) {
              var html = '<tr>';
              row.forEach(function(cell) {
                html += '<td>' + cell + '</td>';
              });
              html += '</tr>';
              console.log(html);
            //   document.getElementById('table').innerHTML += html;
            });
          };
          reader.readAsArrayBuffer(file);
    
    }else{
        alert("Please upload a valid excel file");
        return;
    }
    
  }
function dragleave(ev){
    console.log("drag leave");
    document.getElementById("upload_block").classList.remove("active-drop");
    document.getElementById("text_drop").innerHTML="Drag and drop the file here";
    
    ev.preventDefault();
}
function dragOverHandler(ev) {
    console.log("File(s) in drop zone");
    document.getElementById("upload_block").classList.add("active-drop");
    document.getElementById("text_drop").innerHTML="Leave the file here";
    // Prevent default behavior (Prevent file from being opened)
    ev.preventDefault();
  }




function checkList(){
    // get data from the server

    setRequestHeader();
    val=document.getElementById('listid').innerHTML;
    if(val=="") return;
    $.ajax({
        dataType: 'json',
        type: 'POST',
        url: "/getdata/",
        data: {
            data: 'ListType&listsubjects',
            id:val,
        },
        success: function (data) {
            // console.log(data);
            if(data['type']==false){
                selectMe(document.getElementById("partialbutton"),true);
                console.log(data['data']);
                console.log(document.getElementById('card-options').children);
                b=new Set();
                $.each(data['data'],function(index,value){
                    b.add(value.sid)
                })
                console.log(b);
                ele=document.getElementsByClassName('card');
                for(i=0;i<ele.length;i++){
                    console.log(ele[i]);
                    if(b.has(ele[i].id)){
                        addCard(ele[i]);
                        // i--;
                    }
            }
        }
            
        },
        error: function (jqXHR, textStatus, errorThrown) {
            alert("Error: " + errorThrown);
        }
    });
}

function removeDefault() {
    $("input[type=number]").on("focus", function() {
      $(this).on("keydown", function(event) {
        if (event.keyCode === 38 || event.keyCode === 40) {
          event.preventDefault();
        }
      });
    });
  }
$(document).ready(function(){removeDefault();});

// send data to the server
function UploadData(){
    list_id=document.getElementById('listid').innerHTML;
    if($('#name').val()==""){
        alert("Please enter a name for the list");
        $('#name').focus();
        $('#name').css('border-color','red');
        return;
    }
    val=false;
    setRequestHeader();
    var data1={};
    alert("Your entered will override existing data");
    ele=$('#grid-container>input[type="number"], #grid-container>input[type="text"]');
    for(i=0;i<ele.length;i+=3){
        if(ele[i].value!="" && ele[i+1].value!="" && ele[i+2].value!=""){
            data1[ele[i].value]={'name':ele[i+1].value,'class':ele[i+2].value};
        }else{
            val=true;
        }
    }
    Class="";
    if(selected==0){
        Class=$('#class').val();
    }

    data={"id":list_id,"listName":$('#name').val(),"choice":selected,'class':Class,'student':data1,"subject":selected_subjects};
    if(val){
        
        if(confirm("Half filled rows will be ignored")){
            $.ajax({
                dataType: 'json',
                type: 'POST',
                url: "/uploaddata/",
                data: {
                    data: JSON.stringify(data),
                },
                success: function (data) {
                    window.location.href="/";
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    alert("Error: " + errorThrown);
                }
            });
        }
        return;
    }
    else{
        $.ajax({
            dataType: 'json',
            type: 'POST',
            url: "/uploaddata/",
            data: {
                data: JSON.stringify(data),
            },
            success: function (data) {
                window.location.href="/";
            },
            error: function (jqXHR, textStatus, errorThrown) {
                alert("Error: " + errorThrown);
            }
        });
    }
    
}

// update the class feild when the when the class changes
function updatedClass(arg){
    index_ele=$('#grid-container>input');
    for(i=2;i<$('#grid-container>input').length;i+=3){
        index_ele[i].value=arg.selectedOptions[0].innerHTML;
    }
    // console.log(arg.selectedOptions[0].innerHTML);
    // console.log(index_ele);

}



// move through the sheet using arrow keys
function move(e){
    index_ele=$('#grid-container>input').index(e.srcElement);
    ele=$('#grid-container>input');
    len=ele.length
    // console.log(len,index_ele);
    switch (e.keyCode) { 
        case 37: 
            // str = 'Left Key pressed!'; 
            index_ele-=1;
            break; 
        case 38: 
            // str = 'Up Key pressed!'; 
            index_ele-=3;
            break; 
        case 39: 
            // str = 'Right Key pressed!'; 
            index_ele+=1;
            break; 
        case 40: 
            // str = 'Down Key pressed!'; 
            index_ele+=3;
            break; 
        default:
            return;
        
    }
    if(index_ele>=len){
        index_ele-=len;
    }
    if(index_ele<0){
        index_ele+=len;
    }
    // console.log(index_ele,ele[index_ele]);
    // if(index_ele==0 && e.srcElement.value==""){
    //     return;
    // }
    ele[index_ele].focus();

}
var selected=0;
index_ele=$('#grid-container>input');
for(i=2;i<index_ele.length;i+=3){
    index_ele[i].readOnly=true;
    index_ele[i].value=document.getElementById('class').selectedOptions[0].innerHTML;
}
function selectMe(arg,skip_promt=false){
    if(!arg.classList.contains("selected")){
    cond= skip_promt || confirm("Are you sure you want to change what the list belongs to?\nThis might result in loss of some data.");
    if(cond){
    ele=arg.parentElement.children;
    ele[0].classList.remove("selected");
    ele[1].classList.remove("selected");
    arg.classList.add("selected");
    globalThis.selected=$(arg).index();
    if(selected==0){
        document.getElementById("top-section").style.display="none";
        document.getElementById("bottom-section").style.display="none";
        document.getElementById("top-class-section").style.display="flex";
        index_ele=$('#grid-container>input');
        for(i=2;i<$('#grid-container>input').length;i+=3){
            index_ele[i].readOnly=true;
            index_ele[i].value=document.getElementById('class').selectedOptions[0].innerHTML;
        }
    }
    if(selected==1){
        document.getElementById("top-section").style.display="flex";
        document.getElementById("bottom-section").style.display="flex";
        document.getElementById("top-class-section").style.display="none";
        index_ele=$('#grid-container>input');
        for(i=2;i<$('#grid-container>input').length;i+=3){
            index_ele[i].readOnly=false;
            index_ele[i].value=document.getElementById('class').selectedOptions[0].innerHTML;
        }
    }
}
}
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
            data: 'class&subject&student',
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
        for(i=0;i<3;i++,input_count++){
            ele=document.createElement('input');
            ele.id="input"+input_count;
            if(i==0){
                ele.onchange=function(){UpdateRow(this)};
            }
            if(i==2 && selected==0){
                ele.readOnly=true;
                ele.value=document.getElementById('class').selectedOptions[0].innerHTML;
            }
            ele.classList.add("element");
            ele.type=val[i];
            arg.parentElement.appendChild(ele);
            ele.addEventListener('keyup',e=>{move(e)});
        }
        removeDefault();
        // console.log(arg.parentElement.children[arg.parentElement.children.length-3]);
        arg.parentElement.children[arg.parentElement.children.length-3].focus();
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
        // console.log(data.student);
        AddNewRow(arg);
    }
    else if($(arg).index()%4==2){
        // console.log(data.student);
        if(arg.value==""){
            console.log("Deleting row");
            
            DeleteRow(arg.parentElement.children[$(arg).index()-1]);
        }
    }
    if($(arg).index()%4==2 && selected==0){
        ele=arg.parentElement.children;
        for(i=2;i<ele.length;i+=4){
            if(ele[i].value==arg.value && ele[i]!=arg){
                alert("Roll number already exists");
                arg.value="";
                return;
            }
        }
        // console.log(data.student);
        value=null;
        for(i=0;i<data.student.length;i++){
            if(arg.value==data.student[i].rollno){
                value=data.student[i];
                break;
        }
        
    }
    if(value!=null){
        // console.log("found",data.student[i].name);
        if(value.cid!=arg.parentElement.children[$(arg).index()+2].value && selected==0){
            alert("The student you entered belongs to "+value.cid);
        }
        else{
        arg.parentElement.children[$(arg).index()+2].value=value.cid;
        arg.parentElement.children[$(arg).index()+1].value=value.name;
        }
    }
}else if($(arg).index()%4==2 && selected==1){
    ele=arg.parentElement.children;
for(i=2;i<ele.length;i+=4){
    if(ele[i].value==arg.value && ele[i]!=arg){
        alert("Roll number already exists");
        arg.value="";
        return;
    }
}
    value=null;
    for(i=0;i<data.student.length;i++){
        if(arg.value==data.student[i].rollno){
            value=data.student[i];
            break;
    }
}

console.log(value);
if(value!=null){
    arg.parentElement.children[$(arg).index()+2].value=value.cid;
    arg.parentElement.children[$(arg).index()+1].value=value.name;
}
}
}