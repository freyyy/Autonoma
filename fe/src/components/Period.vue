<script>
import { PolarArea } from "vue-chartjs";
import { HTTP } from "../config/http-common.js";
export default {
  extends: PolarArea,
  props: { years: Object },

  async mounted() {
    // Overwriting base render method with actual data.
    this.employee = await HTTP.get(`employees/${this.$route.params.userId}`);
    const years = [];
    years[0] = this.employee.data.time_spend_company;
    years[1] = this.employee.data.estimated_years_in_company;
    this.renderChart(
      {
        labels: ["Worked years in company", "Estimated years in company"],
        datasets: [
          {
            label: "Activity",
            backgroundColor: [
              "rgba(125, 54, 137, .6)",
              "rgba(23, 216, 110, .6)"
            ],
            data: years
          }
        ]
      },
      { responsive: true, maintainAspectRatio: false }
    );
  }
};
</script>