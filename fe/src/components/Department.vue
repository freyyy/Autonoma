<script>
    import { Doughnut } from 'vue-chartjs'

    export default {
        extends: Doughnut,
        mounted () {
            // Overwriting base render method with actual data.
            this.renderChart({
                labels: ["asdsadsads", "Asia", "Europe", "Latin America", "North America"],
                datasets: [
                    {
                        label: "Population (millions)",
                        backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
                        data: [2478,5267,734,784,433]
                    }
                ]
            })
        }
    }
</script>