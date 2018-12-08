<script>
import { Bar } from "vue-chartjs";
import { HTTP } from "../config/http-common.js";

export default {
  extends: Bar,
  async mounted() {
    // Overwriting base render method with actual data.
    const features = await HTTP.get(`features`);
    const data = [];
    data[0] = features.data.average_monthly_hours;
    data[1] = features.data.last_evaluation;
    data[2] = features.data.number_project;
    data[3] = features.data.time_spend_company;

    this.renderChart(
      {
        labels: [
          "Average Monthly Hours",
          "Last Evaluationi",
          "Number of Projects",
          "Time spend in company"
        ],
        datasets: [
          {
            label: "%",
            backgroundColor: [
              "rgb(50,205,50)",
              "rgb(255,160,122)",
              "rgba(125, 54, 137, .6)",
              "rgb(30,144,255)"
            ],
            data
          }
        ]
      },
      { responsive: true, maintainAspectRatio: false }
    );
  }
};
</script>

{
 "Departments": "product_mng",
 "Work_accident": 0,
 "average_montly_hours": 152,
 "last_evaluation": 0.48,
 "number_project": 2,
 "promotion_last_5years": 0,
 "salary": "medium",
 "time_spend_company": 3
}