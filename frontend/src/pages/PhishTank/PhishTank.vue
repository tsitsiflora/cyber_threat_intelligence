<template>
    <div class="phish-tank-page">
        <h1 class="page-title">Phish Tank</h1>

        <v-client-table :columns="columns" v-model="phishTankDatabase" :options="options">
        </v-client-table>
    </div>
</template>

<script>
    import {mapState} from 'vuex';

    export default {
        name: 'PhishTank',
        data() {
            return {
                columns: ['name', 'description', 'pattern', 'labels'],
                options: {
                    headings: {
                        name: 'Name',
                        description: 'Description',
                        pattern: 'Pattern',
                        labels: 'Labels'
                    },
                    editableColumns: [],
                    sortable: ['name', 'labels'],
                    filterable: ['name', 'labels', 'pattern', 'description']
                }
            };
        },
        methods: {
        },
        computed: {
            ...mapState('data', ['phishTankDatabase'])
        }
    };
</script>

<style scoped src="./PhishTank.scss" lang="scss" />
