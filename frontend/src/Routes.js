import Vue from 'vue';
import Router from 'vue-router';

import Layout from '@/components/Layout/Layout';
import Login from '@/pages/Login/Login';
import ErrorPage from '@/pages/Error/Error';
// Core
import TypographyPage from '@/pages/Typography/Typography';

// Tables
import TablesBasicPage from '@/pages/Tables/Basic';

// Maps
import GoogleMapPage from '@/pages/Maps/Google';

// Main
import AnalyticsPage from '@/pages/Dashboard/Dashboard';

// Charts
import ChartsPage from '@/pages/Charts/Charts';

import MitrePrePage from "./pages/MitrePre/MitrePre";
import MitreMobilePage from "./pages/MitreMobile/MitreMobile";
import MitreEnterprisePage from "./pages/MitreEnterprise/MitreEnterprise";

// Ui
import IconsPage from '@/pages/Icons/Icons';
import NotificationsPage from '@/pages/Notifications/Notifications';
import NewIoC from "./pages/NewIoC/NewIoC";
import PhishTank from "./pages/PhishTank/PhishTank";


Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
    {
      path: '/error',
      name: 'Error',
      component: ErrorPage,
    },
    {
      path: '/app',
      name: 'Layout',
      component: Layout,
      children: [
        {
          path: 'dashboard',
          name: 'AnalyticsPage',
          component: AnalyticsPage,
        },
        {
          path: 'mitre-pre-attack',
          name: 'MitrePreAttack',
          component: MitrePrePage,
        },
        {
          path: 'mitre-enterprise',
          name: 'MitreEnterprise',
          component: MitreEnterprisePage,
        },
        {
          path: 'mitre-mobile',
          name: 'MitreMobile',
          component: MitreMobilePage,
        },
        {
          path: 'new-ioc',
          name: 'NewIoc',
          component: NewIoC,
        },
        {
          path: 'phish-tank-records',
          name: 'PhishTankRecords',
          component: PhishTank,
        },

        {
          path: 'typography',
          name: 'TypographyPage',
          component: TypographyPage,
        },
        {
          path: 'components/icons',
          name: 'IconsPage',
          component: IconsPage,
        },
        {
          path: 'notifications',
          name: 'NotificationsPage',
          component: NotificationsPage,
        },
        {
          path: 'components/charts',
          name: 'ChartsPage',
          component: ChartsPage,
        },
        {
          path: 'tables',
          name: 'TablesBasicPage',
          component: TablesBasicPage,
        },
        {
          path: 'components/maps',
          name: 'GoogleMapPage',
          component: GoogleMapPage,
        },
      ],
    },
  ],
});
