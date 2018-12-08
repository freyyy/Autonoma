<template>
  <v-layout row wrap>
    <v-flex xs12>
      <h1>
        <v-btn icon class="light-blue white--text">
          <v-icon>accessibility_new</v-icon>
        </v-btn>
        <span>{{ employee.Name}}</span>
      </h1>

      <v-layout row wrap>
        <v-flex xs7 class="user-details">
          <div v-if="employee.churn === 0">
            <v-icon class="green--text">insert_emoticon</v-icon>
            <h2>User seems to be happy</h2>
            <h3>No action needed</h3>
          </div>
          <div v-else-if="employee.churn === 1">
            <v-icon class="red--text">sentiment_very_dissatisfied</v-icon>
            <h2>User seems to be unhappy</h2>
            <h3>Meeting created. Please check your appointment dashboard.</h3>
          </div>
        </v-flex>

        <v-flex xs5 class="graph-container">
          <Period :years="employee"/>
        </v-flex>
      </v-layout>
    </v-flex>

    <v-flex xs12 class="bottom-graph">
      <Influence/>
    </v-flex>
  </v-layout>
</template>


<script>
import Period from "../components/Period";
import Influence from "../components/Influence";
import { HTTP } from "../config/http-common.js";

export default {
  methods: {
    goTo(url) {
      this.$router.push(url);
    },
    async init() {
      this.employee = await HTTP.get(`employees/${this.$route.params.userId}`);
      this.employee = this.employee.data;
      console.log(this.employee);
    }
  },
  mounted() {
    this.init();
  },
  components: {
    Period,
    Influence
  },
  data() {
    return {
      employee: {}
    };
  }
};
</script>


<style scoped lang="scss">
h1 {
  padding-bottom: 10px;
  margin-bottom: 10px;
  border-bottom: 1px solid #dfdfdf;
}

.user-details {
  .v-icon {
    font-size: 180px;
    display: block;
    text-align: center;
  }

  h2,
  h3 {
    text-align: center;
  }
}
</style>