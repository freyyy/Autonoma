<template>
  <v-data-table
    :rows-per-page-items="rowsPerPageItems"
    :pagination.sync="pagination"
    :headers="headers"
    :items="employees"
    :loading="false"
    class="elevation-1"
  >
    <v-progress-linear slot="progress" color="blue" indeterminate></v-progress-linear>
    <template slot="items" slot-scope="props">
      <tr @click="goTo(`/user/${props.item.empId}`)">
        <td>{{ props.item.Name }}</td>
        <td class="text-xs-right">{{ props.item.Departments }}</td>
        <td class="text-xs-right">{{ props.item.Work_accident }}</td>
        <td class="text-xs-right">{{ props.item.average_montly_hours }}</td>
        <td class="text-xs-right">{{ props.item.number_project }}</td>
        <td class="text-xs-right">{{ props.item.salary }}</td>
        <td class="text-xs-right">{{ props.item.time_spend_company }}</td>
        <td class="text-xs-right">{{ props.item.estimated_years_in_company }}</td>
        <td class="text-xs-center">
          <v-icon class="red--text" v-if="props.item.churn === 1">sentiment_very_dissatisfied</v-icon>
          <v-icon class="green--text" v-else>insert_emoticon</v-icon>
        </td>
      </tr>
    </template>
  </v-data-table>
</template>


<script>
import { HTTP } from "../config/http-common.js";
export default {
  methods: {
    goTo(url) {
      this.$router.push(url);
    },
    async init() {
      this.employees = await HTTP.get("employees");
      this.employees = this.employees.data;
      console.log(this.employees);
    }
  },
  mounted() {
    this.init();
  },
  data() {
    return {
      rowsPerPageItems: [10, 20, 30, 40],
      pagination: {
        rowsPerPage: 20
      },
      headers: [
        {
          text: "Employee",
          align: "center",
          sortable: false,
          value: "name"
        },
        { text: "Deparment", value: "Departments", align: "right" },
        { text: "Work Accidents", value: "carbs", align: "right" },
        { text: "Average Monthly Hours", value: "carbs", align: "right" },
        { text: "Numbar of Projects", value: "fat", align: "right" },
        { text: "Salary", value: "carbs", align: "right" },
        { text: "Time spend in company", value: "protein", align: "right" },
        { text: "Estimated years in company", align: "center", value: "churn" },
        { text: "Churn", align: "center", value: "churn" }
      ],
      employees: []
    };
  }
};
</script>