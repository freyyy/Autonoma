<template>
  <v-app id="inspire">
    <predict v-if="showPredict" @close="closeModal"></predict>
    <v-navigation-drawer :clipped="$vuetify.breakpoint.lgAndUp" v-model="drawer" fixed app>
      <v-list dense>
        <template v-for="item in items">
          <v-list-tile v-if="item.icon === 'settings'" :key="item.text" @click="showPredict=true">
            <v-list-tile-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>{{ item.text }}</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
          <v-list-tile v-else :key="item.text" @click="$router.push(`/${item.href}`)">
            <v-list-tile-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>{{ item.text }}</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </template>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar :clipped-left="$vuetify.breakpoint.lgAndUp" color="blue darken-3" dark app fixed>
      <v-toolbar-title style="width: 300px" class="ml-0 pl-3">
        <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
        <span class="hidden-sm-and-down">Autonoma</span>
      </v-toolbar-title>
      <v-text-field
        flat
        solo-inverted
        hide-details
        prepend-inner-icon="search"
        label="Search"
        class="hidden-sm-and-down"
      ></v-text-field>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>apps</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>notifications</v-icon>
      </v-btn>
    </v-toolbar>
    <v-content>
      <v-container fluid fill-height>
        <router-view style="width: 100%"></router-view>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import Predict from "./components/Predict.vue";

export default {
  components: {
    Predict
  },
  methods: {
    closeModal() {
      this.showPredict = false;
    }
  },
  data: () => ({
    dialog: false,
    drawer: null,
    items: [
      { icon: "home", text: "Dashboard", href: "" },
      { icon: "contacts", text: "Team", href: "team" },
      { icon: "content_copy", text: "Departments", href: "departments" },
      { icon: "settings", text: "Predict" }
      // { icon: "chat_bubble", text: "Send feedback" },
      // { icon: "help", text: "Help" }
    ],
    showPredict: false
  }),
  props: {
    source: String
  }
};
</script>