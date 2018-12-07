<template>
    <v-layout row wrap>
        <v-flex xs12 align-center justify-space-between>
            <Kalendar :configuration="calendar_settings" :appointments="appointments"></Kalendar>
        </v-flex>
    </v-layout>
</template>

<script>
    import {Kalendar} from "kalendar-vue";
    import "kalendar-vue/dist/KalendarVue.css";

    export default {
        components: {
            Kalendar
        },
        data: () => ({
            appointments: [],
            calendar_settings: {
                style: "material_design", // ['flat_design', 'material_design']
                view_type: "Month", // ['Month', 'Day']
                split_value: 20, // Value % 60 === 0
                cell_height: 20, // !isNaN(Value)
                scrollToNow: true, // Boolean
                current_day: new Date() // Valid date
            }
        })
    };
</script>

<style lang="scss">

    .calendarium {

        .sticky-top {
            top: 90px;
            z-index: 1;

            &:before {
                content: '';
                position: absolute;
                bottom: 100%;
                left: 0;
                right: 0;
                height: 20px;
                background-color: #FAFAFA;
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