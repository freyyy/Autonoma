<template>
  <v-layout row justify-center>
    <v-dialog v-model="dialog" persistent max-width="600px">
      <v-btn slot="activator" color="primary" dark>Open Dialog</v-btn>
      <v-card>
        <v-card-title>
          <span class="headline">Predict</span>
        </v-card-title>
        <v-form ref="form" v-model="valid" lazy-validation>
          <v-card-text>
            <v-container grid-list-md>
              <v-layout wrap>
                <v-flex xs12>
                  <v-select
                    v-model="Departments"
                    :items="['technical', 'sales', 'hr','marketing', 'IT', 'support']"
                    label="Departments"
                    :rules="dropDownRules"
                    required
                  ></v-select>
                </v-flex>
                <v-flex xs12>
                  <v-text-field
                    v-model="Work_accident"
                    label="Work Accidents"
                    :rules="numberRules"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12>
                  <v-text-field
                    v-model="average_montly_hours"
                    label="Average Monthly Hours"
                    :rules="numberRules"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12>
                  <v-text-field
                    label="Last Evaluation"
                    v-model="last_evaluation"
                    :rules="numberRules"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12>
                  <v-text-field
                    label="Number Projects"
                    v-model="number_project"
                    :rules="numberRules"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12>
                  <v-text-field
                    label="Promotion last 5 years"
                    v-model="promotion_last_5years"
                    :rules="numberRules"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12>
                  <v-text-field
                    v-model="time_spend_company"
                    label="Time spend in company"
                    :rules="numberRules"
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12>
                  <v-select
                    v-model="salary"
                    :items="['low', 'medium', 'high']"
                    label="Salary"
                    :rules="dropDownRules"
                    required
                  ></v-select>
                </v-flex>
                <v-flex xs12>
                  <div align="center" v-if="churn.data === 0">
                    <v-icon class="green--text">insert_emoticon</v-icon>
                    <h2>User seems to be happy</h2>
                    <h3>No action needed</h3>
                  </div>
                  <div align="center" v-else-if="churn.data === 1">
                    <v-icon class="red--text">sentiment_very_dissatisfied</v-icon>
                    <h2>User seems to be unhappy</h2>
                  </div>
                </v-flex>
              </v-layout>
            </v-container>
            <!-- <small>*indicates required field</small> -->
          </v-card-text>
        </v-form>
        <v-alert
          v-model="alert"
          dismissible
          v-bind:type="alertType"
          transition="scale-transition"
        >{{ alertMessage }}</v-alert>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" flat @click="close()">Close</v-btn>
          <v-btn color="blue darken-1" flat @click="predict()">Predict</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
</template>
<script>
import { HTTP } from "../config/http-common.js";
export default {
  data() {
    return {
      alert: false,
      alertType: null,
      alertMessage: null,
      valid: true,
      dialog: true,
      Departments: null,
      Work_accident: null,
      average_montly_hours: null,
      last_evaluation: null,
      number_project: null,
      promotion_last_5years: null,
      salary: null,
      time_spend_company: null,
      dropDownRules: [v => !!v || "Dropdown is required"],
      fieldRules: [v => !!v || "This field is required"],
      churn: false,
      numberRules: [
        v => !!v || "This field is required",
        v =>
          /^-?(?:0|0\.\d*|[1-9]\d*\.?\d*)$/.test(v) || "Field must be a number"
      ]
    };
  },
  methods: {
    close() {
      this.$emit("close");
    },
    async predict() {
      if (!this.$refs.form.validate()) {
        this.loading = false;
        this.alertMessage = "Please fix all errors";
        this.alertType = "error";
        this.alert = true;
        return;
      }
      this.alert = false;
      const data = {
        Departments: this.Departments,
        Work_accident: this.Work_accident,
        average_montly_hours: this.average_montly_hours,
        last_evaluation: this.last_evaluation,
        number_project: this.number_project,
        promotion_last_5years: this.promotion_last_5years,
        salary: this.salary,
        time_spend_company: this.time_spend_company
      };
      //   alert(JSON.stringify(data));
      try {
        this.churn = await HTTP.post(`predict`, data);
        // console.log(this.churn);
      } catch (err) {
        // console.log(err);
      }
    }
  }
};
</script>