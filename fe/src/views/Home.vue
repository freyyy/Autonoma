<template>
  <v-layout row wrap>
    <v-flex xs12 align-center justify-space-between>
      <v-calendar :attributes="attrs" is-expanded :theme-styles="themeStyles">></v-calendar>
    </v-flex>
  </v-layout>
</template>

<script>
import VCalendar from "v-calendar";
import Vue from "vue";
import "v-calendar/lib/v-calendar.min.css";

Vue.use(VCalendar, {
  firstDayOfWeek: 2 // Monday
});
const todos = [
  {
    description:
      "Please check Marian because it seems that he is not ok with his salary",
    isComplete: true,
    dates: new Date(2018, 11, 7),
    color: "#ff8080" // Red
  },
  {
    description: "Please check Filip",
    isComplete: false,
    dates: new Date(2018, 11, 24),
    color: "#ff8080" // Red
  },
  {
    description: "Please check Andrei",
    isComplete: false,
    dates: new Date(2018, 11, 4), // Every Friday
    color: "#ff8080" // Red
  },
  {
    description: "Please check Octavian",
    isComplete: false,
    dates: new Date(2018, 10, 29),
    color: "#ff8080" // Red
  }
];
export default {
  data() {
    return {
      themeStyles: {
        wrapper: {
          background: "linear-gradient(to bottom right, #ffffff, #ffffff)",
          color: "#00000"
        },
        headerHorizontalDivider: {
          borderTop: "solid rgba(230, 230, 255, 0.5) 1px",
          width: "100%"
        }
      },

      incId: todos.length,
      todos
    };
  },
  computed: {
    attrs() {
      return [
        // Today attribute
        {
          contentStyle: {
            fontWeight: "700",
            fontSize: ".9rem"
          },
          dates: new Date(),
          highlight: {
            backgroundColor: "#ff8080"
            // Other properties are available too, like `height` & `borderRadius`
          }
        },
        // Attributes for todos
        ...this.todos.map(todo => ({
          dates: todo.dates,

          dot: {
            backgroundColor: todo.color,
            opacity: todo.isComplete ? 0.3 : 1
          },
          highlight: {
            backgroundColor: "#ff8080"
            // Other properties are available too, like `height` & `borderRadius`
          },
          popover: {
            label: todo.description
          }
        }))
      ];
    }
  }
};
</script>

<style lang="scss">
.calendarium {
  .sticky-top {
    top: 90px;
    z-index: 1;

    &:before {
      content: "";
      position: absolute;
      bottom: 100%;
      left: 0;
      right: 0;
      height: 20px;
      background-color: #fafafa;
    }
  }

  .blocks {
    z-index: 0;
  }

  .number-date {
    @media (max-width: 768px) {
      font-size: 14px !important;
    }
  }
}
</style>