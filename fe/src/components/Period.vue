<script>
    import { PolarArea } from 'vue-chartjs'

    export default {
        extends: PolarArea,
        mounted () {
            // Overwriting base render method with actual data.
            this.renderChart({
                labels: ["Worked years", "Estimated years"],
                datasets: [
                    {
                        label: 'Activity',
                        backgroundColor: ["rgba(125, 54, 137, .6)","rgba(23, 216, 110, .6)"],
                        data: [4,3]
                    }
                ]
            }, {responsive: true, maintainAspectRatio: false})
        }
    }
</script>