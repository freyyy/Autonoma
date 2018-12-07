<template>
    <v-container grid-list-md text-xs-center>
        <v-layout align-start justify-center row wrap>

            <v-flex xs4 class="graph-container">
                <Department/>
            </v-flex>

            <v-flex xs4 class="graph-container">
                <Department/>
            </v-flex>

            <v-flex xs4 class="graph-container">
                <Department/>
            </v-flex>

            <v-flex xs4 class="graph-container">
                <Department/>
            </v-flex>

            <v-flex xs4 class="graph-container">
                <Department/>
            </v-flex>

            <v-flex xs4 class="graph-container">
                <Department/>
            </v-flex>

            <v-flex xs4 class="graph-container">
                <Department/>
            </v-flex>

            <v-flex xs4 class="graph-container">
                <Department/>
            </v-flex>

            <v-flex xs4 class="graph-container">
                <Department/>
            </v-flex>

        </v-layout>
    </v-container>
</template>

<script>
    import Department from '../components/Department'

    export default {
        components: {
            Department,
        },
    }
</script>

<style scoped lang="scss">
    .graph-container {
        padding: 20px !important;
    }
</style>