<template>
    <Kalendar :configuration="calendar_settings" :appointments="appointments"></Kalendar>
</template>
<script>
    import {Kalendar} from 'kalendar-vue';
    import 'kalendar-vue/dist/KalendarVue.css';

    export default {
        components: {
            Kalendar
        },
        data: () => ({
        appointments: [],
        calendar_settings: {
            style: "material_design", // ['flat_design', 'material_design']
            view_type: 'Month', // ['Month', 'Day']
            split_value: 20, // Value % 60 === 0
            cell_height: 20, // !isNaN(Value)
            scrollToNow: true, // Boolean
            current_day: new Date(), // Valid date
        },
    })}
</script>