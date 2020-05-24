<template>
  <div class="application">
    <div class="loading" v-if="overlay.show">
        <div class="overlay"></div>
        <div class="spanner">
          <div class="loader"></div>
          <p>{{ overlay.message }}</p>
        </div>
    </div>
    <router-view />
  </div>
</template>

<script>
  import axios from "axios"
  import {apiUrl} from "@/config"

  export default {
    name: 'App',
    data() {
      return {
        overlay: {show: false, message: ""}
      }
    },
    created() {
      const currentPath = this.$router.history.current.path;

      if (window.localStorage.getItem('authenticated') === 'false') {
        this.$router.push('/login');
      }

      if (currentPath === '/' || currentPath === '/app') {
        this.$router.push('/app/dashboard');
      }
    },
    async mounted() {
      try {
        this.overlay.message = "Please wait. Fetching the latest data";
        this.overlay.show = true;

        let [phishtank, enterprise, mobile, pre] = await axios.all([
          axios.get( apiUrl('/api/phishtank') ),
          axios.get( apiUrl('/api/mitre-enterprise') ),
          axios.get( apiUrl('/api/mitre-mobile') ),
          axios.get( apiUrl('/api/mitre-pre') ),
        ]);

        this.$store.commit('data/setPhishTankDatabase', phishtank.data.data);
        this.$store.commit('data/setMitreEnterprise', enterprise.data.data);
        this.$store.commit('data/setMitreMobile', mobile.data.data);
        this.$store.commit('data/setMitrePre', pre.data.data);
      } catch (e) {
        this.$swal({
          title: "Failed to fetch data",
          text: "An network error occurred while trying to fetch resources. Please reload the page to try again",
          icon: "error"
        })
      }
      this.overlay.show = false;
    }
  };
</script>

<style src="./styles/theme.scss" lang="scss" />