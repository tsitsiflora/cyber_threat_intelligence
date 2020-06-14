<template>
  <div class="sidebar-wrapper">
    <nav
        :class="{sidebar: true, sidebarStatic, sidebarOpened}"
        @mouseenter="sidebarMouseEnter"
        @mouseleave="sidebarMouseLeave"
    >
      <header class="logo">
        <router-link to="/app"><span class="primary-word">One</span>CTI</router-link>
      </header>
      <ul class="nav">
        <NavLink
            :activeItem="activeItem"
            header="Dashboard"
            link="/app/dashboard"
            iconName="flaticon-home"
            index="dashboard"
            isHeader
        />
        <NavLink
            :activeItem="activeItem"
            header="Mitre Pre Att&ck"
            link="/app/mitre-pre-attack"
            iconName="flaticon-list"
            index="typography"
            isHeader
        />
        <NavLink
                :activeItem="activeItem"
                header="Mitre Mobile Att&ck"
                link="/app/mitre-mobile"
                iconName="flaticon-battery"
                index="typography"
                isHeader
        />
        <NavLink
                :activeItem="activeItem"
                header="Mitre Enterprise Att&ck"
                link="/app/mitre-enterprise"
                iconName="flaticon-network"
                index="typography"
                isHeader
        />
        <NavLink
                :activeItem="activeItem"
                header="Phish Tank Records"
                link="/app/phish-tank-records"
                iconName="flaticon-settings"
                index="typography"
                isHeader
        />
        <NavLink
                :activeItem="activeItem"
                header="Add IoC"
                link="/app/new-ioc"
                iconName="flaticon-add"
                index="typography"
                isHeader
        />
        <NavLink
                :activeItem="activeItem"
                header="Visualize"
                link="https://oasis-open.github.io/cti-stix-visualization/"
                iconName="flaticon-add"
                index="typography"
                isHeader
        />
      </ul>
    </nav>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import isScreen from '@/core/screenHelper';
import NavLink from './NavLink/NavLink';

export default {
  name: 'Sidebar',
  components: { NavLink },
  data() {
    return {
    };
  },
  methods: {
    ...mapActions('layout', ['changeSidebarActive', 'switchSidebar']),
    setActiveByRoute() {
      const paths = this.$route.fullPath.split('/');
      paths.pop();
      this.changeSidebarActive(paths.join('/'));
    },
    sidebarMouseEnter() {
      if (!this.sidebarStatic && (isScreen('lg') || isScreen('xl'))) {
        this.switchSidebar(false);
        this.setActiveByRoute();
      }
    },
    sidebarMouseLeave() {
      if (!this.sidebarStatic && (isScreen('lg') || isScreen('xl'))) {
        this.switchSidebar(true);
        this.changeSidebarActive(null);
      }
    },
  },
  created() {
    this.setActiveByRoute();
  },
  computed: {
    ...mapState('layout', {
      sidebarStatic: state => state.sidebarStatic,
      sidebarOpened: state => !state.sidebarClose,
      activeItem: state => state.sidebarActiveElement,
    }),
  },
};
</script>

<!-- Sidebar styles should be scoped -->
<style src="./Sidebar.scss" lang="scss" scoped/>
