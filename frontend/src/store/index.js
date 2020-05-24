import Vue from 'vue';
import Vuex from 'vuex';

import layout from './layout';
import data from './data';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    layout,
    data
  },
});
