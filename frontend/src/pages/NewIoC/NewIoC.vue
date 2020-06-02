<template>
  <div class="new-ioc-page">
    <h1 class="page-title">Add a new IoC</h1>

    <form @submit.prevent="addIoC" ref="ioc_form">
      <div class="form-group">
        <label for="name">Name</label>
        <input
          id="name"
          name="name"
          placeholder="Enter name"
          type="text"
          class="form-control"
          required="required"
        />
      </div>
      <div class="form-group">
        <label for="select">Type</label>
        <select
          id="select"
          name="type"
          class="form-control"
          required="required"
        >
          <option value="">Please select</option>
          <option value="indicator">Indicator</option>
          <option value="attack-pattern">Attack Pattern</option>
          <option value="identity">Identity</option>
          <option value="location">Location</option>
          <option value="malware">Malware</option>
          <option value="threat-actor">Threat actor</option>
          <option value="tool">Tool</option>
          <option value="vulnerability">Vulnerability</option>
        </select>
      </div>
      <div class="form-group">
        <label for="patternInput">Pattern</label>
        <textarea
          id="patternInput"
          name="pattern"
          cols="40"
          rows="5"
          class="form-control"
          required="required"
        ></textarea>
      </div>
      <div class="form-group">
        <label for="labels">Labels</label>
        <textarea
          id="labels"
          name="labels"
          cols="40"
          rows="5"
          class="form-control"
          aria-describedby="labelsHelpBlock"
        ></textarea>
        <span id="labelsHelpBlock" class="form-text text-muted"
          >Please enter the labels, comma separated</span
        >
      </div>
      <div class="form-group">
        <button name="submit" type="submit" class="btn btn-primary">
          Save IoC
          <svg
            v-if="loading"
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            style="margin: auto; background: rgba(255, 255, 255, 0); display: inline-block; shape-rendering: auto;"
            width="50px"
            height="30px"
            viewBox="0 0 100 100"
            preserveAspectRatio="xMidYMid"
          >
            <rect x="15" y="30" width="10" height="40" fill="#e15b64">
              <animate
                attributeName="opacity"
                dur="1s"
                repeatCount="indefinite"
                calcMode="spline"
                keyTimes="0;0.5;1"
                keySplines="0.5 0 0.5 1;0.5 0 0.5 1"
                values="1;0.2;1"
                begin="-0.6"
              ></animate>
            </rect>
            <rect x="35" y="30" width="10" height="40" fill="#f47e60">
              <animate
                attributeName="opacity"
                dur="1s"
                repeatCount="indefinite"
                calcMode="spline"
                keyTimes="0;0.5;1"
                keySplines="0.5 0 0.5 1;0.5 0 0.5 1"
                values="1;0.2;1"
                begin="-0.4"
              ></animate>
            </rect>
            <rect x="55" y="30" width="10" height="40" fill="#f8b26a">
              <animate
                attributeName="opacity"
                dur="1s"
                repeatCount="indefinite"
                calcMode="spline"
                keyTimes="0;0.5;1"
                keySplines="0.5 0 0.5 1;0.5 0 0.5 1"
                values="1;0.2;1"
                begin="-0.2"
              ></animate>
            </rect>
            <rect x="75" y="30" width="10" height="40" fill="#abbd81">
              <animate
                attributeName="opacity"
                dur="1s"
                repeatCount="indefinite"
                calcMode="spline"
                keyTimes="0;0.5;1"
                keySplines="0.5 0 0.5 1;0.5 0 0.5 1"
                values="1;0.2;1"
                begin="-1"
              ></animate>
            </rect>
          </svg>
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import { apiUrl } from "@/config";

export default {
  name: "NewIoC",
  components: {},
  data() {
    return {
      loading: false,
    };
  },
  methods: {
    async addIoC() {
      this.loading = true;

      const data = new FormData(this.$refs.ioc_form);

      axios({
        method: "post",
        url: apiUrl("/api/ioc/create"),
        data: data,
      })
        .then((raw) => {
          let response = raw.data;

          if (response.status !== "success") throw new Error("Failed to saved");

          this.$swal({
            title: "IoC saved",
            text: "We have successfully saved your new IoC.",
            icon: "success",
          });

          this.loading = false;
        })
        .catch(() => {
          this.$swal({
            title: "Yikes!",
            text:
              "An error occured while trying to send request. Please try again",
            icon: "error",
          });

          this.loading = false;
        });
    },
  },
  computed: {},
};
</script>

<style src="./NewIoC.scss" lang="scss" />
