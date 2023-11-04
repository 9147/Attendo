next_address = '';
function openWindow(arg,sid=0){
    console.log(arg);
    document.getElementById('blur_layer').classList.add('blur-layer');
    document.getElementById('window').style.display = 'flex';
    if(arg==0){
        next_address = '/attendance/'+sid;
        document.getElementById('1').innerHTML = 'Swapy';
        console.log("value"+document.getElementById('1').innerHTML);
        document.getElementById('2').innerHTML = 'Mark';
    }
}

function closeWindow(){
    document.getElementById('blur_layer').classList.remove('blur-layer');
    document.getElementById('window').style.display = 'none';
    document.getElementById('submit').href="";
    // document.getElementById('window_content').innerHTML = '';
}
selected_choice = NaN;
function selectMe(arg){
    e=arg.parentElement;
    i=0;
    while(i< e.children.length){
        e.children[i].classList.remove('selected_choice');
        i++;
    }
    arg.classList.add('selected_choice');
    selected_choice = arg.id;
    // console.log(selected_choice);
}

function openNewWindow(){
    if(isNaN(selected_choice)){
        alert('Please select an option');
        return;
    }
    document.location="/"+selected_choice+next_address;
    console.log(selected_choice);
}