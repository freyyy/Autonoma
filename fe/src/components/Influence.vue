<script>
    import { Line } from 'vue-chartjs'

    export default {
        extends: Line,
        mounted () {
            // Overwriting base render method with actual data.
            this.renderChart({
                labels: ["Something", "Something else", "Gugu", "Lulu"],
                datasets: [
                    {
                        label: 'aaa',
                        backgroundColor: ["rgba(125, 54, 137, .6)"],
                        data: [4,-3, 6, 12]
                    }
                ]
            }, {responsive: true, maintainAspectRatio: false})
        }
    }
</script>