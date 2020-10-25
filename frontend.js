//https://www.w3schools.com/xml/ajax_xmlhttprequest_response.asp
function getRequest(url, cFunction){
    var xhttp;
    xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      cFunction(this.responseText); //Needed this to be this.responseText!!!
    }
 };
  xhttp.open("GET", url, true);
  xhttp.send();
}
//So this will send a request to the Bottle Server, and the bottle server will return something!
//That something will be called by cFunction

function onLoad(){
    getRequest("/display-current", displayData);
}
function displayData(lotStates){
    //let lots = JSON.parse(lotStates);
    document.getElementById("currentstate").innerHTML = lotStates;
    //So Lots is essentially a big dictionary with key:value pairs inside!
    // let str = "";
    // for (let i = 0; i < lots.length; i++){
    //     str += i(0) + ":" + i(1).toString + "\n";
    // }


}