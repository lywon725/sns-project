
  
//const timeContainer = document.querySelector(".time"),
//    nowHour = timeContainer.querySelector("#hour"),
//    nowMin = timeContainer.querySelector("#minutes"),
//    nowSec = timeContainer.querySelector("#seconds"),
//    nowAmpm = timeContainer.querySelector("#period");
//const dayContainer = document.querySelector(".date"),
//    nowDay = dayContainer.querySelector("#dayname"),
//    nowMonth = dayContainer.querySelector("#month"),
//    nowDate = dayContainer.querySelector("#daynum"),
//    nowYear = dayContainer.querySelector("#year");

function getTime(){
    const now = new Date();
    const minutes = now.getMinutes();
    let hours = now.getHours();
    const seconds = now.getSeconds();
   
    if(hours >= 12){
        document.getElementById("period").firstChild.nodeValue = "PM";
    }
    if (hours==0){
        hours = 12;
    }
    if (hours > 12){
        hours = hours - 12;
    }
 
    //html에 text 넣기
    //nowHour.innerHTML = hours<10 ? `0${hours}`:hours;
    //nowMin.innerHTML = minutes<10 ? `0${minutes}`: minutes; 
    //nowSec.innerHTML = seconds<10 ? `0${seconds}`: seconds;
    
    //과제 for문으로 바꾸기
    let ids = ["hour","minutes", "seconds"];
    let values = [hours, minutes, seconds];
    for(let i =0; i<ids.length; i++){
        document.getElementById(ids[i]).firstChild.nodeValue = values[i]<10?`0${values[i]}`:values[i];
    }
}

function getCalender() {
    const now = new Date();
    const day = now.getDay(); // 요일
    const month = now.getMonth(); // 월
    const date = now.getDate(); // 일
    const year = now.getFullYear(); // 년
    
    let week = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ];
    
    //월-> 영문풀네임으로 나타내기 
    let month_name = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ];

    //nowDay.innerText = week[day];
    //nowMonth.innerText = month;
    //nowDate.innerText = date;
    //nowYear.innerText = year;
    let ids = ["dayname","month","daynum","year"];
    let values = [week[day], month_name[month], date, year];
    for(let i =0; i<ids.length; i++){
        if (values[i] == date)
            document.getElementById(ids[i]).firstChild.nodeValue = values[i]<10?`0${values[i]}`:values[i];
        else
            document.getElementById(ids[i]).firstChild.nodeValue = values[i];
    }
}

function init() {
    getTime();
    getCalender();
    setInterval(getTime,1000);
}
init();
