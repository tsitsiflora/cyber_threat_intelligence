<template>
  <div class="dashboard-page">
    <h1 class="page-title">Dashboard</h1>
  </div>
</template>

<script>
import Widget from '@/components/Widget/Widget';
import BigStat from './components/BigStat/BigStat';
import mock from './mock';

import { Chart } from 'highcharts-vue';

export default {
  name: 'Dashboard',
  components: {
  },
  data() {
    return {
      mock
    };
  },
  methods: {
  },
  computed: {
  }
};
</script>

<style src="./Dashboard.scss" lang="scss" />
