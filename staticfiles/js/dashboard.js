document.addEventListener('DOMContentLoaded', function () {
  const lineChart = document.getElementById('myChart').getContext('2d');
  const barras = document.getElementById('barChartCol1').getContext('2d');
  const doughnutEarnings = document.getElementById('doughnutChartEarnings').getContext('2d');
  const doughnutExpenses = document.getElementById('doughnutChartExpenses').getContext('2d');
  const radarChart = document.getElementById('radarChart').getContext('2d');

  // Gráfico de linha 
  const data = {
    labels: labels,
    datasets: [
      {
        label: 'Receita',
        data: earningsList,
        data: earningsList,
        fill: false,
        borderColor: 'rgb(54, 162, 235)',
        tension: 0.1
      },
      {
        label: 'Despesa',
        data: expensesList,
        data: expensesList,
        fill: false,
        borderColor: 'rgb(255, 99, 132)',
        tension: 0.1
      }
    ]
  };

  const config = {
    type: 'line',
    data: data,
    options: {
      responsive: true,
      maintainAspectRatio: false
    }
  };

  // Gráfico de barras 
  const barCol1Data = {
    labels: labels,
    datasets: [
      {
        label: 'Despesa',
        data: expensesList,
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgb(255, 99, 132)',
        borderWidth: 1
      },
      {
        label: 'Receita',
        data: earningsList,
        backgroundColor: 'rgb(54, 162, 235, 0.2)',
        borderColor: 'rgb(54, 162, 235)',
        borderWidth: 1
      }
    ]
  };

  const barCol1Config = {
    type: 'bar',
    data: barCol1Data,
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  };

  // Gráfico de rosca receita 
  const doughnutDataEarnings = {
    labels: categoryEarnings,
    datasets: [{
      label: ['Valor'],
      data: dataEarningsCategory,
      hoverOffset: 4
    }]
  };

  const doughnutConfigEarnings = {
    type: 'doughnut',
    data: doughnutDataEarnings,
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        title: {
          display: true,
          text: 'Receitas'
        }
      }
    }
  };

  // Gráfico de rosca despesa
  const doughnutDataExpenses = {
    labels: categoryExpenses,
    datasets: [{
      label: ['Valor'],
      data: dataExpensesCategory,
      hoverOffset: 4
    }]
  };

  const doughnutConfigExpenses = {
    type: 'doughnut',
    data: doughnutDataExpenses,
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        title: {
          display: true,
          text: 'Despesas'
        }
      }
    }
  };

  // radar chart
  
  const radarChartData = {
    labels: labels,
    datasets: [{
      label: 'Despesas',
      data: expensesList,
      fill: true,
      backgroundColor: 'rgba(255, 99, 132, 0.2)',
      borderColor: 'rgb(255, 99, 132)',
      pointBackgroundColor: 'rgb(255, 99, 132)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgb(255, 99, 132)'
    }, {
      label: 'Receitas',
      data: earningsList,
      fill: true,
      backgroundColor: 'rgba(54, 162, 235, 0.2)',
      borderColor: 'rgb(54, 162, 235)',
      pointBackgroundColor: 'rgb(54, 162, 235)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgb(54, 162, 235)'
    }]
  };

  const radarChartConfig = {
    type: 'radar',
    data: radarChartData,
    options: {
      responsive: true,
      maintainAspectRatio: false,
      elements: {
        line: {
          borderWidth: 3
        }
      }
    },
  };


  new Chart(lineChart, config);
  new Chart(barras, barCol1Config);
  new Chart(doughnutEarnings, doughnutConfigEarnings);
  new Chart(doughnutExpenses, doughnutConfigExpenses);
  new Chart(radarChart, radarChartConfig);
});