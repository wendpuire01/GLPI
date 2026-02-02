<script>
  // Fetch the data from the Django view
  fetch("/api/machines-par-mois/")
  .then(response => response.json())
  .then(data => {
      const ctx = document.getElementById("myAreaChart").getContext('2d');
      const myAreaChart = new Chart(ctx, {
          type: 'line',
          data: {
              labels: data.labels,  // Mois des acquisitions
              datasets: [{
                  label: 'Nombre de machines acquises',
                  data: data.data,  // Nombre de machines par mois
                  backgroundColor: 'rgba(78, 115, 223, 0.05)',
                  borderColor: 'rgba(78, 115, 223, 1)',
                  pointRadius: 3,
                  pointBackgroundColor: 'rgba(78, 115, 223, 1)',
                  pointBorderColor: 'rgba(78, 115, 223, 1)',
                  pointHoverRadius: 3,
                  pointHoverBackgroundColor: 'rgba(78, 115, 223, 1)',
                  pointHoverBorderColor: 'rgba(78, 115, 223, 1)',
                  pointHitRadius: 10,
                  pointBorderWidth: 2,
                  fill: true,
              }],
          },
          options: {
              maintainAspectRatio: false,
              scales: {
                  xAxes: [{
                      time: {
                          unit: 'month'
                      },
                      gridLines: {
                          display: false,
                          drawBorder: false
                      },
                      ticks: {
                          maxTicksLimit: 12
                      }
                  }],
                  yAxes: [{
                      ticks: {
                          maxTicksLimit: 5,
                          padding: 10,
                      },
                      gridLines: {
                          color: "rgb(234, 236, 244)",
                          zeroLineColor: "rgb(234, 236, 244)",
                          drawBorder: false,
                          borderDash: [2],
                          zeroLineBorderDash: [2]
                      }
                  }],
              },
          }
      });
  });
</script>