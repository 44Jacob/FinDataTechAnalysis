const init = async () => {
    let stock_data = await ( await fetch('/api/v1.0/stock_data')).json()

    console.log(stock_data);

    document.getElementById('stocks').innerHTML = '';
    Object.keys(stock_data).forEach(stock => {
      document.getElementById('stocks').innerHTML += `<h3>${stock}</h3>`
    })

var trace1 = {
  x: Object.keys(stock_data),
  y: Object.values(stock_data),
  type: 'bar',
  text:Object.values(stock_data).map(x => Math.round(x*100)/100),
  textposition: 'auto',
  hoverinfo: 'none',
  marker: {
    color: 'rgb(158,202,225)',
    opacity: 0.6,
    line: {
      color: 'rgb(8,48,107)',
      width: 1.5
    }
  }
};

var data = [trace1];

var layout = {
  title: '<b>Average Sentiment Report</b>',
  barmode: 'stack'
};

Plotly.newPlot('chart01', data, layout);

var trace1 = {
  x: [1, 2, 3, 4],
  y: [10, 15, 13, 17],
  type: 'scatter'
};

var trace2 = {
  x: [1, 2, 3, 4],
  y: [16, 5, 11, 9],
  type: 'scatter'
};

var data = [trace1, trace2];

Plotly.newPlot('chart02', data);


};

init();

const stockSel = async () => {
  let stocks = JSON.stringify(document.getElementById('tickers').value.split(','));
  let start = document.getElementById('start').value;
  let end = document.getElementById('end').value;

  console.log(stocks);
  await fetch(`/api/v1.0/load_data/${stocks}`);
  window.location.reload();
}