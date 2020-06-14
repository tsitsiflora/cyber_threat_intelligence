<template>
    <div class="mitre-pre-page">
        <h1 class="page-title">Mitre Pre Attack</h1>

        <v-client-table :columns="columns" v-model="mitrePre" :options="options">
            <div slot="child_row" slot-scope="props">
                <div style="width: 100%;box-shadow:inset 0 0 4px rgba(0 0 0 / 13%);padding: 10px;">
                    <h6>External References</h6>
                    <table class="table-bordered" v-if="props.row.external_references && props.row.external_references.length > 0">
                        <thead>
                        <tr>
                            <th>External ID</th>
                            <th>Source Name</th>
                            <th>External URL</th>
                            <th>External References</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr v-for="reference in props.row.external_references">
                            <td>{{ reference.external_id || "Unset"}}</td>
                            <td>{{ reference.source_name || "Unset"}}</td>
                            <td>{{ reference.url || "Unset" }}</td>
                            <td>{{ reference.external_references || "Unset" }}</td>
                        </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </v-client-table>
    </div>
</template>

<script>
    import {mapState} from 'vuex';

    export default {
        name: 'MitrePre',
        components: {
        },
        data() {
            return {
                columns: ['id', 'type', 'description', 'external_references'],
                options: {
                    headings: {
                        id: 'ID',
                        type: 'Type',
                        description: 'Description',
                        external_references: 'External References',
                    },
                    editableColumns: [],
                    sortable: ['name', 'type'],
                    filterable: ['name', 'pattern', 'type']
                }
            };
        },
        methods: {
        },
        computed: {
            ...mapState('data', ['mitrePre'])
        }
    };
</script>

<style src="./MitrePre.scss" lang="scss" />
