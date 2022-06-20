var ctx2 = document.getElementById("chart-line").getContext("2d");
var gradientStroke1 = ctx2.createLinearGradient(0, 230, 0, 50);
gradientStroke1.addColorStop(1, "rgba(248,113,113,0.2)");
gradientStroke1.addColorStop(0.2, "rgba(72,72,176,0.0)");
gradientStroke1.addColorStop(0, "rgba(203,12,159,0)");
var gradientStroke2 = ctx2.createLinearGradient(0, 230, 0, 50);
gradientStroke2.addColorStop(1, "rgba(74,222,128,0.2)");
gradientStroke2.addColorStop(0.2, "rgba(72,72,176,0.0)");
gradientStroke2.addColorStop(0, "rgba(20,23,39,0)");
var gradientStroke3 = ctx2.createLinearGradient(0, 230, 0, 50);
gradientStroke3.addColorStop(1, "rgba(96,165,250,0.2)");
gradientStroke3.addColorStop(0.2, "rgba(72,72,176,0.0)");
gradientStroke3.addColorStop(0, "rgba(20,23,39,0)");
new Chart(ctx2,{
    type: "line",
    data: {
        labels: ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        datasets: [{
            label: "Highly Negative",
            tension: 0.4,
            borderWidth: 0,
            pointRadius: 0,
            borderColor: "#ef4444",
            borderWidth: 3,
            backgroundColor: gradientStroke1,
            fill: true,
            data: [50, 40, 300, 220, 500, 250, 400, 230, 500],
            maxBarThickness: 6,
        }, {
            label: "least Negative",
            tension: 0.4,
            borderWidth: 0,
            pointRadius: 0,
            borderColor: "#4ade80",
            borderWidth: 3,
            backgroundColor: gradientStroke2,
            fill: true,
            data: [20, 40, 30, 20, 50, 40, 50, 60, 40],
            maxBarThickness: 6,
        }, {
            label: "Moderately Negative",
            tension: 0.4,
            borderWidth: 0,
            pointRadius: 0,
            borderColor: "#60a5fa",
            borderWidth: 3,
            backgroundColor: gradientStroke3,
            fill: true,
            data: [40, 30, 240, 200, 300, 250, 300, 230, 300],
            maxBarThickness: 6,
        }],
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                display: false,
            },
        },
        interaction: {
            intersect: false,
            mode: "index",
        },
        scales: {
            y: {
                grid: {
                    drawBorder: false,
                    display: true,
                    drawOnChartArea: true,
                    drawTicks: false,
                    borderDash: [5, 5],
                },
                ticks: {
                    display: true,
                    padding: 10,
                    color: "#b2b9bf",
                    font: {
                        size: 11,
                        family: "Open Sans",
                        style: "normal",
                        lineHeight: 2,
                    },
                },
            },
            x: {
                grid: {
                    drawBorder: false,
                    display: false,
                    drawOnChartArea: false,
                    drawTicks: false,
                    borderDash: [5, 5],
                },
                ticks: {
                    display: true,
                    color: "#b2b9bf",
                    padding: 20,
                    font: {
                        size: 11,
                        family: "Open Sans",
                        style: "normal",
                        lineHeight: 2,
                    },
                },
            },
        },
    },
});
