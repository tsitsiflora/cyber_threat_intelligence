<template>
<div :class="[{root: true, sidebarClose, sidebarStatic}, 'sing-dashboard']">
  <Sidebar />
  <div class="wrap">
    <Header />
    <v-touch class="content" @swipe="handleSwipe" :swipe-options="{direction: 'horizontal'}">
      <breadcrumb-history></breadcrumb-history>
      <transition name="router-animation">
        <router-view />
      </transition>
      <footer class="contentFooter">
        Cyber Threat Intelligence Platform - &copy; 2020
      </footer>
    </v-touch>
  </div>
</div>
</template>

<script>
  import {createNamespacedHelpers} from 'vuex';
  import Sidebar from '@/components/Sidebar/Sidebar';
  import Header from '@/components/Header/Header';
  import Helper from '@/components/Helper/Helper';
  import BreadcrumbHistory from '@/components/BreadcrumbHistory/BreadcrumbHistory';

  import './Layout.scss';

  const {mapState, mapActions} = createNamespacedHelpers('layout');

  export default {
    name: 'Layout',
    components: {Sidebar, Header, Helper, BreadcrumbHistory},
    methods: {
      ...mapActions(['switchSidebar', 'handleSwipe', 'changeSidebarActive', 'toggleSidebar'],
      ),
      handleWindowResize() {
        const width = window.innerWidth;

        if (width <= 768 && this.sidebarStatic) {
          this.toggleSidebar();
        this.changeSidebarActive(null);
      }
    },
  },
  computed: {
    ...mapState(["sidebarClose", "sidebarStatic"]),
  },
  created() {
    const staticSidebar = JSON.parse(localStorage.getItem('sidebarStatic'));

    if (staticSidebar) {
      this.$store.state.layout.sidebarStatic = true;
    } else if (!this.sidebarClose) {
      setTimeout(() => {
        this.switchSidebar(true);
        this.changeSidebarActive(null);
      }, 2500);
    }

    this.handleWindowResize();
    window.addEventListener('resize', this.handleWindowResize);
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.handleWindowResize);
  }
};
</script>

<style src="./Layout.scss" lang="scss" />
