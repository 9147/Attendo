a=document.getElementsByClassName('feilds');
if(a[1].classList[1]=='prof' && a[1].value!=''){
    a[0].readOnly=true;

}else if(a[1].value!=''){
    a[1].readOnly=true;
}
cid_id=document.getElementById('cid_id');
newelem=document.getElementById('cid_data');
newelem.value=cid_id.value;
cid_id.parentNode.replaceChild(newelem, cid_id);
newelem.style.display='block';

pid_id=document.getElementById('prof_id');
newelem=document.getElementById('pid_data');
newelem.value=pid_id.value;
pid_id.parentNode.replaceChild(newelem, pid_id);
newelem.style.display='block';
