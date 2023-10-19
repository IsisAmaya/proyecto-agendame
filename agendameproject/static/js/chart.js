var s1 = {
    label: 'S1',
    borderColor: '#33b5e5',    
    //tension : 0,
    fill: false,
    data : dataset
};

var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
type: 'line',
data: {
datasets: [s1]
},
options: {
legend: {
display: false
},
scales: {
xAxes: [{
type: 'time',
weight: 0,
time: {
unit: 'day'
}
}],
yAxes: [{
type: 'time',
time: {
unit: 'hour'
},
/* ticks: {
reverse: true
} */
}]
}
}
});

