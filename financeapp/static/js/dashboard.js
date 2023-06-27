document.addEventListener('DOMContentLoaded', function () {
    const lineChart = document.getElementById('myChart').getContext('2d');
    const barras = document.getElementById('barChartCol1').getContext('2d');
    const doughnutReceita = document.getElementById('doughnutChart').getContext('2d');
    const doughnutDespesa = document.getElementById('doughnutChart2').getContext('2d');

    // Gráfico de linha 
    const data = {
        labels: labels,
        datasets: [
            {
                label: 'Receita',
                data: earningSum,
                fill: false,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1
            },
            {
                label: 'Despesa',
                data: expenseSum,
                fill: false,
                borderColor: 'rgb(255, 99, 132)',
                tension: 0.1
            }
        ]
    };

    const config = {
        type: 'line',
        data: data,
    };

    // Gráfico de barras 
    const barCol1Data = {
        labels: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
        datasets: [
          {
            label: 'Despesa',
            data: [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000],
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgb(75, 192, 192)',
            borderWidth: 1
          },
          {
            label: 'Receita',
            data: [50, 100, 200, 150, 300, 250, 400, 350, 500, 450, 600, 550],
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgb(255, 99, 132)',
            borderWidth: 1
          }
        ]
      };
  
      const barCol1Config = {
        type: 'bar',
        data: barCol1Data,
        options: {
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      };

    // Gráfico de rosca receita 
      const doughnutDataReceita = {
        labels: ['Receita', 'Despesa'],
        datasets: [{
          label: 'My First Dataset',
          data: [300, 50, 100],
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgb(75, 192, 192)',
          ],
          hoverOffset: 4
        }]
      };
  
      const doughnutConfigReceita = {
        type: 'doughnut',
        data: doughnutDataReceita,
        options: {}
      };
    
    // Gráfico de rosca despesa
    const doughnutDataDespesa = {
        labels: ['Receita', 'Despesa'],
        datasets: [{
          label: 'My First Dataset',
          data: [300, 50, 100],
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgb(75, 192, 192)',
          ],
          hoverOffset: 4
        }]
      };
  
      const doughnutConfigDespesa = {
        type: 'doughnut',
        data: doughnutDataReceita,
        options: {}
      };

    new Chart(lineChart, config);
    new Chart(barras, barCol1Config);
    new Chart(doughnutReceita, doughnutConfigReceita);
    new Chart(doughnutDespesa, doughnutConfigDespesa);
});